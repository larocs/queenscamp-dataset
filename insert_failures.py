'''
Adds the failures to the given sequence of images.
The failure can either be created from math operations or using injected template images.
The template images were copied from the repo: github.com/francescosecci/Python_Image_Failures
'''
import cv2
import os
import tqdm
import glob
import numpy as np
from argparse import ArgumentParser 

FAILURES = {'underexposure': 2, 'overexposure': 0.5, 'blur': 5, 'breakage': 0.5,  'rain': 0.35, 'ice': 0.2}

def overlay_images(image, template, template_alpha=0.5):
    if image.shape[2] == 3:
        image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    template = cv2.resize(template, (image.shape[1], image.shape[0]))
    # img_height, img_width = image.shape[:2]
    # tpl_height, tpl_width = template.shape[:2]
    # if tpl_height > img_height:
    #     start_y = (tpl_height - img_height) // 2
    #     template = template[start_y:start_y + img_height, :]
    
    # if tpl_width > img_width:
    #     start_x = (tpl_width - img_width) // 2
    #     template = template[:, start_x:start_x + img_width]

    # pad_top = max(0, (img_height - tpl_height) // 2)
    # pad_bottom = max(0, img_height - tpl_height - pad_top)
    # pad_left = max(0, (img_width - tpl_width) // 2)
    # pad_right = max(0, img_width - tpl_width - pad_left)

    # if pad_top > 0 or pad_bottom > 0 or pad_left > 0 or pad_right > 0:
    #     template = cv2.copyMakeBorder(template, pad_top, pad_bottom, pad_left, pad_right, cv2.BORDER_CONSTANT, value=(0,0,0,0))

    print(image.shape, template.shape)
    result = cv2.addWeighted(image, 1, template, template_alpha, 0)

    return result

def blur_image(image, kernel_size):
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def gamma_correction(img, gamma):
    img = (img/255.)**(gamma) #apply gamma
    return np.uint8(img*255)

def insert_failures(sequence_path, failure_type, output_path):
    print('Insert failure %s to sequence %s' % (failure_type, sequence_path))
    images = glob.glob(sequence_path + '/*.png')

    os.makedirs(output_path, exist_ok=True)
    for image_path in tqdm.tqdm(images):
        image = cv2.imread(image_path)
        
        if(failure_type == 'underexposure' or failure_type == 'overexposure'):
            image = gamma_correction(image, FAILURES[failure_type])
            cv2.imwrite(output_path + '/' + os.path.basename(image_path), image)
        elif(failure_type == 'blur'):
            image = blur_image(image, FAILURES[failure_type])
            cv2.imwrite(output_path + '/' + os.path.basename(image_path), image)
        else:
            templates_path = 'failures/' + failure_type
            template_path = np.random.choice(glob.glob(templates_path + '/*.png'))
            template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
            image = overlay_images(image, template, template_alpha=FAILURES[failure_type])
            cv2.imwrite(output_path + '/' + os.path.basename(image_path), image)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--sequence_path", type=str, help="Path to the sequence folder")
    parser.add_argument("--output_path", type=str, help="Path to the output folder")
    parser.add_argument("--failure_type", type=str, help="Type of the failure to be inserted")
    args = parser.parse_args()

    if(args.failure_type not in FAILURES):
        print("Invalid failure type. Choose one of the following: ", FAILURES)
        exit()
    insert_failures(args.sequence_path, args.failure_type, args.output_path)