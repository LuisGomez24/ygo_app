#! /usr/bin/env python

"""_summary_"""
import cv2

SRC_DIR  = 'card_img/'

def save_img(card_name, response_img):
    """_summary_

    Args:
        card_name (string):Card's name searched
        response_img (json): Data obtained by API
    """

    card_path = f'{SRC_DIR}{card_name}.jpg'

    with open(card_path, 'wb') as file:
        for chunk in response_img.iter_content(1024):
            file.write(chunk)

    image = cv2.imread(card_path, 1)
    cv2.imshow(card_name, image)
    cv2.waitKey(0)
