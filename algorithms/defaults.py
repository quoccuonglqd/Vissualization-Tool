import numpy as np
import cv2

DEFAULT_FILTER = np.ones((3,3), np.float32) / 9.0

KERNEL_ITENSITY = np.array([[0,0,0], [0,1,0], [0,0,0]])

KERNEL_3x3 = np.ones((3,3), np.float32) / 9.0

KERNEL_5x5 = np.ones((5,5), np.float32) / 25.0

# DEFAULT_DIM = (600,400)

DEFAULT_INTERPOLATION = cv2.INTER_AREA

VALID_ALGORITHMS = {
        'Convolution2D',
        'Color_space_convert',
        'Bluring',
        'Sharpening',
        'Embossing',
        'Enbossing_advance',
        'Erosion_dilation',
        'Vignette_filter',
        'Vifnette_gaussian',
        'Enhancing_contrast',
        'Enhancing_constrast2',
        'Translation',
        'Rotation',
        'Scale',
        'Vertical_wave',
        'Horizontal_wave',
        'Double_wave',
        'Concave_effect',
        'GaussianBlur',
        'BilateralBlur'
}

SIZE_BLURING = 15

KERNEL_SHAPEN = {
        '1':np.array(
                        [[-1,-1,-1],
                        [-1,9,-1],
                        [-1,-1,-1]]
        ),
        '2':np.array(
                        [[1,1,1],
                        [1,-7,1],
                        [1,1,1]]
        ),
        '3':np.array(
                        [[-1,-1,-1,-1,-1],
                        [-1,2,2,2,-1],
                        [-1,2,8,2,-1],
                        [-1,2,2,2,-1],
                        [-1,-1,-1,-1,-1]]) / 8.0,
        }
