import sys
import os
import argparse
import cv2
from defaults import *

# Imort all functions we have
from algorithm import Algorithm

def process(image, name_algorithm: str, args):
    """
    @day: 11-03-2020
    @author: Tien Nguyen
    @parameters:
        - image(image object).
        - name_algorithm (string): The name of alogorithm apply on the image.
        - *arg: some optional arguments.
    @return value:
        - An image object applied the alogithms/operation
    """
    if not name_algorithm in VALID_ALGORITHMS:
        print("The name algorithm is not valid !")
        exit(2)

    if name_algorithm == 'Convolution2D':
        output = Algorithm.Convolution2D(image)
    if name_algorithm == 'Bluring':
        size_bluring = int(args.size_bluring)
        output = Algorithm.Bluring(image=image, size=size_bluring)
    if name_algorithm == 'Sharpening':
        kernel_sharpen = str(args.kernel_sharpen)
        output = Algorithm.Sharpening(image=image, selected_kernel_sharpen=kernel_sharpen)
    if name_algorithm == 'Color_space_convert':
        src_cs = args.src_cs
        dst_cs = args.dst_cs
        output = Algorithm.Color_space_convert(image=image, src_cs = src_cs, dst_cs = dst_cs)
    if name_algorithm == 'Translation':
        dx = int(args.dx)
        dy = int(args.dy)
        output = Algorithm.Translation(img=image,dx=dx,dy=dy)
    if name_algorithm == 'Rotation':
        angle = int(args.angle)
        output = Algorithm.Rotation(img=image,angle=angle)
    if name_algorithm == 'Scale':
        fx = float(args.fx)
        fy = float(args.fy)
        output = Algorithm.Scaling(img=image,fx=fx,fy=fy)
    if name_algorithm == 'Vertical_wave':
        dx = int(args.dx)
        output = Algorithm.Vertical_wave(img=image,dx=dx)
    if name_algorithm == 'Horizontal_wave':
        dy = int(args.dy)
        output = Algorithm.Horizontal_wave(img=image,dy=dy)
    if name_algorithm == 'Double_wave':
        dx = int(args.dx)
        dy = int(args.dy)
        output = Algorithm.Double_wave(img=image,dx=dx,dy=dy)
    if name_algorithm == 'Concave_effect':
        output = Algorithm.Concave_effect(img=image)
    if name_algorithm == 'GaussianBlur':
        kernel_size = int(args.kernel_size_gauss)
        devitation = int(args.devitation)
        output = Algorithm.Gaussian_blur(img=image,kernel_size=kernel_size,devitation=devitation)
    if name_algorithm == 'BilateralBlur':
        diameter = int(args.diameter)
        sigma_color = int(args.sigma_color)
        sigma_space = int(args.sigma_space)
        output = Algorithm.Bilateral_blur(img=image,diameter=diameter,sigma_color=sigma_color,sigma_space=sigma_space)


    return output

def main(args):
    path_image = args.path
    operation = args.operation
    # If the path of image and operation is valid
    if not os.path.isfile(path_image):
        print("The path of image is not exist !")
        sys.exit(1)

    # otherwise
    image = cv2.imread(path_image)
    output = process(image=image, name_algorithm=operation, args=args)
    while True:
        cv2.imshow('Origin', image)
        cv2.imshow('Output', output)
        c = cv2.waitKey()
        if c == 27:
            break
    cv2.destroyAllWindows()
    print("Thank you for your using !")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help="the path of image", default="test.png")
    parser.add_argument("--source_cs", help="color space source", default='RGB')
    parser.add_argument("--destination_cs", help="color space destination", default='GRAY')
    parser.add_argument("--operation", help="operation apply in image", default="Convolution2D")
    parser.add_argument("--size_bluring", help="size of kernel bluring", default=SIZE_BLURING)
    parser.add_argument("--kernel_sharpen", help="The kernel sharpening", default=1)
    parser.add_argument("--dx", help= "distance along x-axis", default =0)
    parser.add_argument("--dy", help = "distance along y-axis", default =0)
    parser.add_argument("--fx", help= "ratio along x-axis", default =0)
    parser.add_argument("--fy", help = "ratio along y-axis", default =0)
    parser.add_argument("--angle", help = "angle", default = 0)
    parser.add_argument("--kernel_size_gauss", help = "kernel size for GaussianBlur", default = 5)
    parser.add_argument("--devitation", help = "devitaion for GaussianBlur", default = 0)
    parser.add_argument("--diameter",help = "diameter for BilateralBlur",default = 9)
    parser.add_argument("--sigma_color",help = "sigmacolor for BilateralBlur",default = 75)
    parser.add_argument("--sigma_space",help = "sigmaspace for BilateralBlur",default = 75)
    args = parser.parse_args()
    print(args)
    main(args)
