import cv2
import numpy as np

def depth_to_point_cloud(depth_img, fx, fy, cx, cy):
    height, width = depth_img.shape
    x, y = np.meshgrid(np.arange(width), np.arange(height))
    x3d = (x - cx) * depth_img / fx
    y3d = (y - cy) * depth_img / fy
    z3d = depth_img
    point_cloud = np.stack((x3d, y3d, z3d), axis=-1)
    return point_cloud

def transform_point_cloud(point_cloud, R, t):
    transformed_points = np.tensordot(point_cloud, R, axes=([2], [0])) + t
    return transformed_points

def project_point_cloud_to_image(point_cloud, fx, fy, cx, cy):
    x3d, y3d, z3d = point_cloud[..., 0], point_cloud[..., 1], point_cloud[..., 2]
    x = (x3d * fx / z3d + cx).astype(np.integer)
    y = (y3d * fy / z3d + cy).astype(np.integer)
    return x, y, z3d

def align_images(rgb_image, depth_img, K_depth, K_rgb, R, t):
    fx_d, fy_d, cx_d, cy_d = K_depth[0,0], K_depth[1,1], K_depth[0,2], K_depth[1,2]
    fx_rgb, fy_rgb, cx_rgb, cy_rgb = K_rgb[0,0], K_rgb[1,1], K_rgb[0,2], K_rgb[1,2]
    scale_x = depth_img.shape[1] / rgb_image.shape[1]
    scale_y = depth_img.shape[0] / rgb_image.shape[0]
    fx_rgb, fy_rgb, cx_rgb, cy_rgb = fx_rgb * scale_x, fy_rgb * scale_y, cx_rgb * scale_x, cy_rgb * scale_y
    rgb_image = cv2.resize(rgb_image, (depth_img.shape[1], depth_img.shape[0]))

    point_cloud = depth_to_point_cloud(depth_img, fx_d, fy_d, cx_d, cy_d)
    transformed_point_cloud = transform_point_cloud(point_cloud, R, t)
    # Project transformed point cloud onto the RGB image plane
    x, y, z = project_point_cloud_to_image(transformed_point_cloud, fx_rgb, fy_rgb, cx_rgb, cy_rgb)
    
    # Create an empty image to hold the aligned depth values
    aligned_depth_img = np.zeros((rgb_image.shape[0], rgb_image.shape[1]), dtype=np.uint16)
    
    # Copy the depth values from the transformed point cloud to the aligned depth image
    valid_points = (x >= 0) & (x < depth_img.shape[1]) & (y >= 0) & (y < depth_img.shape[0]) & (z > 0)
    
    aligned_depth_img[y[valid_points], x[valid_points]] = z[valid_points]
    
    return rgb_image, aligned_depth_img


def depth_to_image(depth_msg):
    w = depth_msg.width
    h = depth_msg.height
    depth_img = np.zeros((h, w), dtype=np.uint16)

    for i in range(w):
        for j in range(h):
            depth_img[j, i] = int.from_bytes(depth_msg.data[(j*w + i)*2:(j*w + i)*2 + 2], byteorder='little')
    return depth_img