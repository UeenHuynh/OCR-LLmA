import os
import cv2
import easyocr
from matplotlib import pyplot as plt

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

def ocr_image(image_path):
    """Perform OCR on a single image and return the results."""
    try:
        results = reader.readtext(image_path)
        return results
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

def ocr_images_in_folder(folder_path):
    """Perform OCR on all images in a folder and return the results."""
    ocr_results = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            file_path = os.path.join(folder_path, filename)
            print(f"Processing {file_path}...")
            results = ocr_image(file_path)
            if results:
                ocr_results[file_path] = results
    return ocr_results

def annotate_image_with_boxes(image_path, ocr_results):
    """Annotate an image with bounding boxes and text from OCR results."""
    mat = cv2.imread(image_path)
    for result in ocr_results:
        bbox, text, score = result
        top_left = tuple(map(int, bbox[0]))
        bottom_right = tuple(map(int, bbox[2]))
        cv2.rectangle(mat, top_left, bottom_right, (0, 255, 0), 2)
        cv2.putText(mat, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)
    mat = cv2.cvtColor(mat, cv2.COLOR_BGR2RGB)
    return mat

def process_folders(folder_paths):
    """Process multiple folders and perform OCR on the images within."""
    for folder_path in folder_paths:
        ocr_results = ocr_images_in_folder(folder_path)
        for file_path, results in ocr_results.items():
            print(f"Text extracted from {file_path}:")
            for result in results:
                print(result[1])
            print()

            # Annotate the image
            annotated_image = annotate_image_with_boxes(file_path, results)
            plt.imshow(annotated_image)
            plt.axis('off')  # Hide the axis
            plt.title(f"OCR Results for {os.path.basename(file_path)}")
            plt.show()

# Define the paths to the folders
folder_paths = [
    'folder1',
    'folder2',
    'folder3'
]

# Process the folders
process_folders(folder_paths)



