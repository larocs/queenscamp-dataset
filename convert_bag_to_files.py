import os
import rosbag
import csv
import cv2
import numpy as np
import argparse
from cv_bridge import CvBridge
from scipy.spatial.transform import Rotation as R
from depth_utils import *
from visualization import *
from utils import *

def pose_to_matrix(pose):
    # Convert a Pose message to a pose Matrix
    position = [pose.position.x, pose.position.y, pose.position.z]
    quat = [pose.orientation.x, pose.orientation.y, pose.orientation.z, pose.orientation.w]
    rot_mat = R.from_quat(quat).as_matrix()
    pose_mat = np.eye(4)
    pose_mat[:3, :3] = rot_mat
    pose_mat[:3, 3] = position
    return pose_mat

def convert_bag_to_files(args):
    bag = rosbag.Bag(args.bag_file)
    print("Converting bag file: {} to trajectory file: {} and image folder: {}".format(args.bag_file, args.trajectory_file, args.image_folder))
    bridge = CvBridge()
    os.makedirs(args.image_folder, exist_ok=True)
    os.makedirs(args.depth_folder, exist_ok=True)

    if(args.depth_topic is not None):    
        depth_camera_info = None
        for topic, msg, t in bag.read_messages(topics=[args.depth_topic.replace('image_rect_raw', 'camera_info')]):
            depth_camera_info = msg
            K_depth = camera_info_to_matrix(depth_camera_info)
            if(K_depth is not None):
                break
    
    color_camera_info = None
    for topic, msg, t in bag.read_messages(topics=[args.image_topic.replace('image_raw/compressed', 'camera_info')]):
        color_camera_info = msg
        K_color = camera_info_to_matrix(color_camera_info)
        if(K_color is not None):
            break

    tf_static = None
    for topic, msg, t in bag.read_messages(topics=['/tf_static']):
        tf_static = msg
        Rt = tf_static_to_Rt(tf_static, "tarot2_color_frame", "tarot2_depth_frame")
        if Rt is not None:
            break

    timestamps = []
    imgs_count = 0
    skip = args.skip
    if(args.save_as_video):
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
        out = cv2.VideoWriter(os.path.join(args.image_folder, args.video_file), fourcc, args.video_fps, (1920, 1080))

    if(args.pose_topic != None):
        poses = []
    
        writer = csv.writer(open(args.trajectory_file, 'w'), delimiter=' ')

        for topic, msg, t in bag.read_messages(topics=[args.pose_topic]):
            tstamp = msg.header.stamp.secs+msg.header.stamp.nsecs*1e-9
            poses.append(msg.pose)
            timestamps.append(tstamp)
        
        print('Found {} poses '.format(len(timestamps)))
        first_pose = pose_to_matrix(poses[0].pose)
        print('first pose: ', first_pose)
        target_rot = R.from_quat([0, 0, 0, 1]).as_matrix()
        target_pose = np.eye(4)
        target_pose[:3, :3] = target_rot
        print('target pose: ', target_pose)
        transformation = np.linalg.inv(first_pose) @ target_pose
        print('transformation: ', transformation)

    tstamps_file = open(os.path.join(args.timestamps_file), 'w+')
    depth_msgs = []
    depth_timestamps = []
    if(args.depth_topic is not None):
        for topic, msg, t in bag.read_messages(topics=[args.depth_topic]):
            depth_tstamp = msg.header.stamp.secs + msg.header.stamp.nsecs * 1e-9
            depth_msgs.append(msg)
            depth_timestamps.append(depth_tstamp)

    for topic, msg, t in bag.read_messages(topics=[args.image_topic]):
        if(skip > 0):
          skip -= 1
          continue
        #find approximate match between image timestamp and pose timestamp
        tstamp = msg.header.stamp.secs+msg.header.stamp.nsecs*1e-9
        
        if args.pose_topic is not None:
            # Find the closest pose timestamp
            pose_idx = min(range(len(timestamps)), key=lambda i: abs(timestamps[i] - tstamp))
            pose = poses[pose_idx]

            # Convert pose relative to first pose
            pose_mat = pose_to_matrix(pose.pose)
            transformed_pose = transformation @ pose_mat

            # Convert pose to translation and rotation
            translation = transformed_pose[:3, 3]
            rotation = R.from_matrix(transformed_pose[:3, :3]).as_quat()

            # Write to CSV file
            writer.writerow([tstamp, translation[0], translation[1], translation[2], rotation[0], rotation[1], rotation[2], rotation[3]])
            tstamps_file.write(str(tstamp) + '\n')

            # Find the closest depth timestamp
            depth_idx = min(range(len(depth_timestamps)), key=lambda i: abs(depth_timestamps[i] - tstamp))
            depth_msg = depth_msgs[depth_idx]
            depth_img = depth_to_image(depth_msg)

            #get image
            img = bridge.compressed_imgmsg_to_cv2(msg, desired_encoding="passthrough")     
            
            if(args.depth_topic != None):
                img, depth_img = align_images(img, depth_img, K_depth, K_color, Rt[:3, :3], Rt[:3, 3])
            
            if(args.visualize):
                display_images(img, depth_img, 0.9)

            #write image
            print("Writing image: {}.png. {}/{}".format(tstamp, imgs_count, args.max_imgs))
            #write depth
            if(args.depth_topic != None):
                cv2.imwrite(os.path.join(args.depth_folder, "{}.png".format(tstamp)), depth_img)
            if(args.save_as_video):
                out.write(img)
            else:
                cv2.imwrite(os.path.join(args.image_folder, "{}.png".format(tstamp)), img)
            imgs_count += 1
            if imgs_count >= args.max_imgs:
                break
    tstamps_file.close()
    bag.close()
    print("Done.")


if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("bag_file", help="Input bag file")
    args.add_argument("--trajectory_file", help="Output trajectory file", default=None)
    args.add_argument("--image_folder", help="Image folder", default='images')
    args.add_argument("--depth_folder", help="Depth folder", default='depths')
    args.add_argument("--timestamps_file", help="Output trajectory file", default=None)
    args.add_argument("--image_topic", help="Image topic", default='rgb/image_raw/compressed')
    args.add_argument("--depth_topic", help="Depth topic", default='depth/image_raw')
    args.add_argument("--pose_topic", help="Pose topic", default=None)
    args.add_argument("--max_imgs", help="Maximum number of images to convert", default=800, type=int)
    args.add_argument("--skip", help="N first images to skip", default=0, type=int)
    args.add_argument("--save_as_video", help="Save images as video", default=False, action='store_true')
    args.add_argument("--video_file", help="Output video file", default='output.avi')
    args.add_argument("--video_fps", help="Output video fps", default=15, type=int)
    args.add_argument("--visualize", help="Visualize images", default=False, action='store_true')

    args = args.parse_args()
    convert_bag_to_files(args)
