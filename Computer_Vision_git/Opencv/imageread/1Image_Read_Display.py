import cv2

# Load an image
image_path = r"C:\Users\HP\OneDrive\Pictures\Tiger.jpeg"
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is not None:
    # Display the image
    cv2.imshow("Loaded Image", image)
    
    # Add a delay and wait for a key press
    cv2.waitKey(0)
    
    # Close all windows and release resources
    cv2.destroyAllWindows()
else:
    print("Failed to load the image.")
