import argparse
import cv2
import os

def process_images(inputdir, outputdir, scale_percent):
    for filename in os.listdir(inputdir):
        img = cv2.imread(os.path.join(inputdir, filename))

        width = int(img.shape[1] * int(scale_percent) / 100)
        height = int(img.shape[0] * int(scale_percent) / 100)
        dim = (width, height)

        # Resize image
        resized_img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

        cv2.imwrite(os.path.join(outputdir, filename), resized_img)


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--inputdir", type=str, default="input", required="true", help="path to input directory")
ap.add_argument("-o", "--outputdir", type=str, default="output", required="true", help="path to output directory")
ap.add_argument("-p", "--percent", type=str, default="25", required="true", help="percent size reduction")
args = vars(ap.parse_args())

process_images(args["inputdir"], args["outputdir"], args["percent"])


