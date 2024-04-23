
![wynik](https://github.com/MBurdziej/numpy_image_blending/assets/108184079/4dc6dedb-79a2-4077-accc-636ad475258d)


This program contains a set of functions for image manipulation using numpy libraries in Python. The functions include resizing images, increasing their resolution, merging images, and blending with images containing an alpha channel.

Functions
1. resize(image) - This function reduces the size of the image by 1/3 using a 3x3 window for smoothing.
2. resize_alpha(image) - Similar to the previous function, but preserves the alpha channel if the image has one.
3. upscale(image, height2, width2) - This function increases the size of the image to the specified height and width.
4. merge(image, image2) - Merges two images by calculating the average pixel value for each channel.
5. merge_alpha(image, image2) - Similar to the previous function, but takes into account the alpha channel of the second image.
