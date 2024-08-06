'''
Adds the failures to the given sequence of images.
The failure can either be created from math operations or using injected template images.
The template images were copied from the repo: github.com/francescosecci/Python_Image_Failures
'''

import os
import tqdm
import glob
import numpy as np
from skimage import io
from argparse import ArgumentParser 

FAILURES = ['underexposure', 'overexposure', 'breakage', 'blur', 'rain']

def gamma_correction(img, gamma):
    img = (img/255.)**(gamma) #apply gamma
    return np.uint8(img*255)

def insert_failures(sequence_path, failure_type, output_path):
    print('Insert failure %s to sequence %s' % (failure_type, sequence_path))
    images = glob.glob(sequence_path + '/*.png')

    os.makedirs(output_path, exist_ok=True)
    for image_path in tqdm.tqdm(images):
        image = io.imread(image_path)

        if(failure_type == 'underexposure'):
            gamma = 2
            image = gamma_correction(image, gamma)
            io.imsave(output_path + '/' + os.path.basename(image_path), image)
        elif(failure_type == 'overexposure'):
            gamma = 0.5
            image = gamma_correction(image, gamma)
            io.imsave(output_path + '/' + os.path.basename(image_path), image)


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