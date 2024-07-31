import cv2
import os

# Specify the image file paths
image_path1 = r'C:\Users\CPCM\OneDrive\Desktop\opencv\backgroundRemoval\images\hey.jpg'
image_path2 = r'C:\Users\CPCM\OneDrive\Desktop\opencv\backgroundRemoval\images\2.jpg'

# Check if the files exist
if os.path.exists(image_path1) and os.path.exists(image_path2):
    print(f"Files '{image_path1}' and '{image_path2}' exist.")
    
    # Try to read the image files
    img1 = cv2.imread(image_path1)
    img2 = cv2.imread(image_path2)
    
    if img1 is not None and img2 is not None:
        print(f"Images '{image_path1}' and '{image_path2}' were read successfully.")
        
        # Display the images
        cv2.imshow('Image 1', img1)
        cv2.imshow('Image 2', img2)
        
        # Wait for a key press and then close all OpenCV windows
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    else:
        print(f"Error: Unable to read one or both image files '{image_path1}' and '{image_path2}'.")
else:
    print(f"One or both files '{image_path1}' and '{image_path2}' do not exist.")