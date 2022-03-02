#!/usr/bin/python3
#Python3 program to convert imgage to pdf.
#im2pdf v b0.01

import img2pdf
from PIL import Image
import os
import time

#path to image dir.
img_dir = input('Path to image dir: ')

# variable created for time count. can be activated.
# t = 0

# creating empty list
img_lst = []

# loop for localize every jpg img inside dir
for i in os.listdir(img_dir):
	if i.endswith('.jpg'):
		# t += 1
		
		# option to resize images half on width and heighht
		# img = Image.open(img_dir + '/' + i)
		# new_img = img.resize((round(img.width * 0.5), round(img.height * 0.5)))
		# new_img.save(img_dir + '/new_' + i)
		# img_lst.append(img_dir + '/new_' + i)
		
		img_lst.append(img_dir + '/' +i)
		print(f'Added file {i} to page list.')

# sorting file list, can be removed if u dont need pages in order
print('sorting list...')
img_lst.sort()
# time.sleep(t/100)
print('sorting finished...')

# creating PDF file.
print('\n\ncreating file...\n\n')
with open(img_dir + '/file.pdf', 'wb') as f:
	f.write(img2pdf.convert(img_lst))

print('file created.')
