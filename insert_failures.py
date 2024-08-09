'''
Adds the failures to the given sequence of images.
The failure can either be created from math operations or using injected template images.
The template images were copied from the repo: github.com/francescosecci/Python_Image_Failures
'''
import cv2
import os
import tqdm
import logging
import glob
import numpy as np
from argparse import ArgumentParser 

FAILURES = {'underexposure': 2, 'overexposure': 0.5, 'blur': 35, 'breakage': 1.0,  'rain': 0.75, 'condensation': 1.0, 'dirt': 0.65} 

def overlay_images(image, template, alpha=0.5):
    '''
        Overlays the template image on the original image with the given alpha value
    '''
    image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
    template = cv2.resize(template, (image.shape[1], image.shape[0]))
    template_rgb = template[:, :, :3]
    alpha_channel = (template[:, :, 3] / 255.0)*alpha
    for c in range(0, 3):
        image[:, :, c] = (1.0 - alpha_channel) * image[:, :, c] + alpha_channel * template_rgb[:, :, c]
    return image

def blur_image(image, kernel_size):
    '''
        Blurs the image using Gaussian blur
    '''
    return cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)

def gamma_correction(img, gamma):
    '''
        Under and over exposure can be simulated by gamma correction
    '''
    img = (img/255.)**(gamma) #apply gamma
    return np.uint8(img*255)

def insert_failures(sequence_path, failure_type, output_path):
    '''
        Inserts the failure to the given sequence of images and saves it to the output path
    '''
    if not os.path.exists(sequence_path):
        logging.error('Sequence path does not exist')
        return
    
    logging.info('Inserting failures %s to the sequence %s and saving to %s', failure_type, sequence_path, output_path)
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
            template_path = np.random.choice(glob.glob(templates_path + '/*.png')) #if more than one template is present, choose randomly
            template = cv2.imread(template_path, cv2.IMREAD_UNCHANGED)
            image = overlay_images(image, template, FAILURES[failure_type])
            cv2.imwrite(output_path + '/' + os.path.basename(image_path), image)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("--sequence_path", type=str, help="Path to the sequence folder")
    parser.add_argument("--output_path", type=str, help="Path to the output folder")
    parser.add_argument("--failure_type", type=str, help="Type of the failure to be inserted")
    args = parser.parse_args()

    if(args.failure_type not in FAILURES):
        logging.error('Invalid failure type, choose from %s', list(FAILURES.keys()))
        exit()
    insert_failures(args.sequence_path, args.failure_type, args.output_path)