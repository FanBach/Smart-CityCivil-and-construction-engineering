import os
import random
import shutil

def copy_random_jpg_images(source_folder, destination_folder, num_images):
    print("Starting.. taking path..")
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # List all JPG files in the source folder
    jpg_files = [f for f in os.listdir(source_folder) if f.lower().endswith('.jpg')]

    print("Checking the num of jpg...")
    
    # Check if there are enough images to copy
    if len(jpg_files) < num_images:
        print(f"Not enough JPG images in the source folder. Found: {len(jpg_files)}, Requested: {num_images}")
        return
    print("Selecting images...")
    
    # Randomly select the specified number of images
    selected_images = random.sample(jpg_files, num_images)
    print("Copying....")

    # Copy selected images to the destination folder
    for image in selected_images:
        source_path = os.path.join(source_folder, image)
        destination_path = os.path.join(destination_folder, image)
        shutil.copy(source_path, destination_path)
        print(f"Copied: {image} to {destination_folder}")
    print("DONE!!!!")


# Example usage
source_folder = r"G:\My Drive\rubbish\rubbish"
destination_folder = r"E:\Yolo_data\total image"
num_images_to_copy = 1000

copy_random_jpg_images(source_folder, destination_folder, num_images_to_copy)