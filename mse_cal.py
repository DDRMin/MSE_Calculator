import cv2
import numpy as np

def calculate_mse(image1_path, image2_path):
    # Read images
    img1 = cv2.imread(image1_path)
    img2 = cv2.imread(image2_path)

    # Check if images are loaded
    if img1 is None or img2 is None:
        raise ValueError("One or both image paths are invalid or images cannot be loaded.")

    # Resize images to the same size if needed
    if img1.shape != img2.shape:
        img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

    # Calculate MSE
    mse = np.mean((img1.astype("float") - img2.astype("float")) ** 2)
    return mse

if __name__ == "__main__":
    image1_path = "github image.webp"
    image2_path = "gitlab image.webp"
    mse = calculate_mse(image1_path, image2_path)
    print(f"Mean Squared Error: {mse}")
