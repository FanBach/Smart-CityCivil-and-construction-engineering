import os
import shutil
import random

def select_and_copy_images(base_folder, train_folder, val_folder, output_folder, num_files=100):
    # Create output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Define a list of image file extensions to consider
    image_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.jng')

    # Get list of all image files in the base folder
    base_files = [f for f in os.listdir(base_folder) if f.lower().endswith(image_extensions)]
    
    # Get list of all image files in train and val folders
    train_files = {f for f in os.listdir(train_folder) if f.lower().endswith(image_extensions)}
    val_files = {f for f in os.listdir(val_folder) if f.lower().endswith(image_extensions)}
    
    # Combine train and val files into a set for quick lookup
    excluded_files = train_files.union(val_files)
    
    # Filter out files that are in train or val folders
    available_files = [f for f in base_files if f not in excluded_files]

    # Randomly select num_files from available_files
    selected_files = random.sample(available_files, min(num_files, len(available_files)))

    # Copy selected files to the output folder
    for file in selected_files:
        shutil.copy(os.path.join(base_folder, file), os.path.join(output_folder, file))

    print(f"Copied {len(selected_files)} files to {output_folder}")

# Example usage
base = r"G:\My Drive\rubbish\rubbish"
train = r"G:\My Drive\New_YOLO_data\images\train"
val = r"G:\My Drive\New_YOLO_data\images\val"
output = r"G:\My Drive\Test_data\test\images"
select_and_copy_images(base, train, val, output)