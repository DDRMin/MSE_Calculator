# Mean Squared Error (MSE) Image Comparison

This project provides a simple Python script to calculate the Mean Squared Error (MSE) between two images. MSE is a common metric used to measure the difference between two images, often used in image processing and computer vision tasks.

## Features
- Supports most common image formats (JPEG, PNG, BMP, TIFF, WebP, etc.)
- Automatically resizes the second image to match the first image's dimensions if needed
- Simple command-line usage

## Requirements
- Python 3.x
- OpenCV (`cv2`)
- NumPy

Install dependencies with:
```bash
pip install -r requirements.txt
```

## Usage
Place your images in the project directory. By default, the script compares `github image.jpeg` and `gitlab image.webp`:

```bash
python mse_cal.py
```

You can modify the image filenames in `mse_cal.py` to compare other images.

## Output
The script prints the Mean Squared Error value between the two images.

## Notes
- Both images must be readable by OpenCV. Unsupported or corrupted files will cause an error.
- Images are compared after resizing the second image to match the first image's size.

## License
This project is provided for educational purposes.

## Owner
DDRMin
