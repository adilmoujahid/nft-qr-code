'''
title           : make_qr_code.py
description     : Generate a version 3 (29x29) QR code with ECC level H. 
				  Take out the pixels from the middle of the QR code and replace them with 
				  a pixelated version of the word “NFT”. 
				  Save the QR code as PNG.
author          : Adil Moujahid
date_created    : 20210504
date_modified   : 20210504
version         : 1.0
usage           : python make_qr_code.py http://bit.ly/hellonfts
python_version  : 3.6.8
References      : [1] https://www.qrcode.com/en/about/version.html
'''

import sys
import qrcode
import numpy as np
from PIL import Image as im

def make_qr_code(url):

	#Make a QR code that encodes the value of url
	qr = qrcode.QRCode(version=3, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=1, border=0)
	qr.add_data(url)
	qr.make(fit=True)

	#Making the QR image
	img_qr = qr.make_image(fill_color="black", back_color="white")
	#Converting img_qr to numpy array 
	img_qr_array = np.array(img_qr)

	#Creating a pixelated version of the word “NFT” as a numpy array
	nft = np.array([[True, True,  True, True, True, True, True, True, True, True, True, True, True, True, True],
	                [True, False, True, True, False, True, False, False, False, False, True, False, False, False, True],
	                [True, False, False, True, False, True, False, True, True, True, True, True, False, True, True],
	                [True, False, True, False, False, True, False, False, False, True, True, True, False, True, True],
	                [True, False, True, True, False, True, False, True, True, True, True, True, False, True, True], 
	                [True, False, True, True, False, True, False, True, True, True, True, True, False, True, True], 
	                [True, True,  True, True, True, True, True, True, True, True, True, True, True, True, True]])
	# Changing the middle of the QR code with pixelated version of the word “NFT” 
	img_qr_array[12:19, 7:22] = nft

	nft_qr_img = im.fromarray(img_qr_array)
	return nft_qr_img

if __name__ == '__main__':

	url = str(sys.argv[1])
	nft_qr_img = make_qr_code(url)
	nft_qr_img.save('nft_qr.png')

