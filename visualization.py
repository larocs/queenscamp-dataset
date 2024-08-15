
import cv2
import numpy as np

def display_images(rgb_image, depth_image=None, window_scale=0.5):
    normalized_depth = cv2.normalize(depth_image, None, 0, 255, cv2.NORM_MINMAX)
    if depth_image is not None:
        depth_colormap = cv2.applyColorMap(normalized_depth.astype(np.uint8), cv2.COLORMAP_JET)
        rgb_image_resized = cv2.resize(rgb_image, depth_colormap.shape[:2][::-1])
        overlayed_image = cv2.addWeighted(rgb_image_resized, 0.6, depth_colormap, 1 - 0.6, 0)
        
        # Resize windows based on the window_scale
        resized_rgb = cv2.resize(rgb_image_resized, None, fx=window_scale, fy=window_scale)
        resized_depth = cv2.resize(depth_colormap, None, fx=window_scale, fy=window_scale)
        resized_overlay = cv2.resize(overlayed_image, None, fx=window_scale, fy=window_scale)
        
        cv2.imshow("RGB Image", resized_rgb)
        cv2.imshow("Depth Image", resized_depth)
        cv2.imshow("Overlay Image", resized_overlay)
    else:
        resized_rgb = cv2.resize(rgb_image, None, fx=window_scale, fy=window_scale)
        cv2.imshow("RGB Image", resized_rgb)

    cv2.waitKey(1)
