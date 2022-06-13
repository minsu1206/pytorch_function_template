import numpy as np
import cv2


def minsu_padding(image):
	h, w = image.shape[:2]
	maxhw = np.max([h, w])
	pad_h = int((maxhw - h) / 2)
	pad_v = int((maxhw - w) / 2)
	return cv2.copyMakeBorder(image, pad_h, pad_h, pad_v, pad_v, cv2.BORDER_CONSTANT)


if __name__ == "__main__":
	example = cv2.imread('ex.jpg', cv2.IMREAD_COLOR)

	padded = minsu_padding(example)

	cv2.imshow('r', padded)
	cv2.waitKey(0)
