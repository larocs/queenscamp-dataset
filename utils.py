from scipy.spatial.transform import Rotation as R
import numpy as np

def camera_info_to_matrix(camera_info):
    # Convert a CameraInfo message to a camera matrix
    fx = camera_info.K[0]
    fy = camera_info.K[4]
    cx = camera_info.K[2]
    cy = camera_info.K[5]
    return np.array([[fx, 0, cx], [0, fy, cy], [0, 0, 1]])

def pose_to_matrix(pose):
    # Convert a Pose message to a pose Matrix
    position = [pose.translation.x, pose.translation.y, pose.translation.z]
    quat = [pose.rotation.x, pose.rotation.y, pose.rotation.z, pose.rotation.w]
    rot_mat = R.from_quat(quat).as_matrix()
    pose_mat = np.eye(4)
    pose_mat[:3, :3] = rot_mat
    pose_mat[:3, 3] = position
    return pose_mat

def tf_static_to_Rt(tf_static, frame_id1, frame_id2):
    tf1_to_parent = None
    tf2_to_parent = None
    tf2_to_tf1 = None
    for transform in tf_static.transforms:
        if(transform.child_frame_id == frame_id1):
            tf1_to_parent = transform.transform
        if(transform.child_frame_id == frame_id2):
            tf2_to_parent = transform.transform
    if(tf1_to_parent is not None and tf2_to_parent is not None):
        tf2_to_tf1 = np.dot(pose_to_matrix(tf1_to_parent), np.linalg.inv(pose_to_matrix(tf2_to_parent)))
    return tf2_to_tf1