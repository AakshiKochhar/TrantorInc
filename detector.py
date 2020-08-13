""" This program will detect a template from an image and draw a square around it. """

import cv2  

TEMPLATE_PATH = 'template.jpg'  # Path to template image.
IMAGE_PATH = 'img.jpg'  # Path to real image.
verbose = False  
canny_t1, canny_t2 = 50, 200  # Thresholds for canny edge detection.

image = cv2.imread(IMAGE_PATH)  
template = cv2.imread(TEMPLATE_PATH) 
height, width, _ = template.shape  
template = cv2.Canny(template, canny_t1, canny_t2)  # Perform canny edge detection to improve detection.


# If there is a possibility that the template/image was resized, try to make the detector edge invariant.
best_val, best_coord, best_scale = None, None, None

for i in range(25):  # Makes 25 scales.
    scale = 1 - 3*i/80  # Calculate scale -- ranges from 1 to 0.1.
    img_resized = cv2.resize(image, (int(image.shape[1]*scale), int(image.shape[0]*scale)))  
    if img_resized.shape[0] < height or img_resized.shape[1] < width:  
        break                                                          

    img_resized = cv2.Canny(img_resized, canny_t1, canny_t2)  # Canny edge detection for the resized image.
    ratio = image.shape[1] / img_resized.shape[1]  # Keep track of the ratio of the resized image to the original image.
                                                   
    result = cv2.matchTemplate(img_resized, template, cv2.TM_CCOEFF_NORMED)  
    minv, maxv, minc, maxc = cv2.minMaxLoc(result)  

    if verbose: 
        cv2.rectangle(img_resized, maxc, (maxc[0]+width, maxc[1]+height), 255, 2)  # Draw a rectangle around the match.
        cv2.imshow(f'Step {i+1}', img_resized)  
        cv2.waitKey(0)  

    if best_val is None or maxv>best_val:  # If initial step, or found a better match, store values.
        best_val = maxv  
        best_coord = maxc
        best_scale = ratio


left_top = (int(best_coord[0] * best_scale), int(best_coord[1] * best_scale))  
bottom_right = (int((best_coord[0] + width) * best_scale), int((best_coord[1] + height) * best_scale))  
print(f'Match found between {left_top}, {bottom_right}')
cv2.rectangle(image, left_top, bottom_right, 255, 2)  
cv2.imshow('Detected', image)  # Display the image with the match.
cv2.waitKey(0)

