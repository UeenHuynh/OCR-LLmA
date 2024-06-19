import os
import shutil

def split_folder(source_folder, target_folders, split_size):
    """Split source_folder into multiple target_folders with split_size each."""
    files = os.listdir(source_folder)
    total_files = len(files)

    for i, target_folder in enumerate(target_folders):
        os.makedirs(target_folder, exist_ok=True)
        start_index = i * split_size
        end_index = min(start_index + split_size, total_files)

        for j in range(start_index, end_index):
            source_file = os.path.join(source_folder, files[j])
            target_file = os.path.join(target_folder, files[j])
            shutil.move(source_file, target_file)

if __name__ == "__main__":
    source_folder = "E:/Angel Hack/OCR-LLmA/FULL [Heineken Vietnam] Developer Resources"  # Update this with the path to your source folder
    target_folders = ["E:/Angel Hack/OCR-LLmA/folder1", "E:/Angel Hack/OCR-LLmA/folder2", "E:/Angel Hack/OCR-LLmA/folder3"]  # Update these with your desired target folder names
    split_size = 500  # Number of files per target folder (1500 / 3 = 500)

    split_folder(source_folder, target_folders, split_size)
