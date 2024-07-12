import os
from PIL import Image

def resize_images_in_folder(folder_path, output_folder, size=(800, 800)):
    """
    Resize all images in the specified folder and save them to the output folder.
    
    Parameters:
    folder_path (str): Path to the folder containing images to resize.
    output_folder (str): Path to the folder to save resized images.
    size (tuple): Desired size for resizing the images (width, height).
    """
    os.makedirs(output_folder, exist_ok=True)
    
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            image_path = os.path.join(folder_path, filename)
            with Image.open(image_path) as img:
                img_resized = img.resize(size, Image.LANCZOS)
                img_resized.save(os.path.join(output_folder, filename))
    
    print(f"Images in {folder_path} have been resized and saved to {output_folder}")

# Define the size for resizing images
resize_size = (800, 800)  # You can change this to the desired size

# Define source and destination directories
source_folders = [
    'folder1',
    'folder2',
    'folder3'
]

output_folders = [
    'resized_folder1',
    'resized_folder2',
    'resized_folder3'
]

# Resize images in each folder
for source_folder, output_folder in zip(source_folders, output_folders):
    resize_images_in_folder(source_folder, output_folder, size=resize_size)
