import os
import shutil

def divide_folder_into_subfolders(source_folder, num_subfolders, destination_folder=None):
    # Use the source folder as the destination if no destination is provided
    if destination_folder is None:
        destination_folder = source_folder

    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)
    
    # Get all files in the source folder
    all_files = [f for f in os.listdir(source_folder) if os.path.isfile(os.path.join(source_folder, f))]
    
    # Calculate the number of files per subfolder
    files_per_folder = len(all_files) // num_subfolders
    remainder = len(all_files) % num_subfolders

    # Track the index of the files as they are moved
    file_index = 0

    for i in range(num_subfolders):
        # Create subfolder name in the specified destination
        subfolder_name = os.path.join(destination_folder, f'subfolder_{i+1}')
        os.makedirs(subfolder_name, exist_ok=True)
        
        # Determine the number of files for this subfolder
        current_folder_size = files_per_folder + (1 if i < remainder else 0)
        
        # Move files to the subfolder
        for j in range(current_folder_size):
            file_path = os.path.join(source_folder, all_files[file_index])
            shutil.move(file_path, subfolder_name)
            file_index += 1

    print(f"Folder '{source_folder}' has been divided into {num_subfolders} subfolders in '{destination_folder}'.")

# Example usage:
source_folder = r"E:\Yolo_data\total image"  # Replace with the path to your source folder
destination_folder = r"E:\Yolo_data\gr of images"  # Replace with the path to your destination folder
num_subfolders = 20
divide_folder_into_subfolders(source_folder, num_subfolders, destination_folder)
"-----------------------------------------------------------------------------------------------------------------------------------------------------------"

def move_missing_files(source_folder, folder1, folder2, folder3):
    # Ensure folder3 exists
    os.makedirs(folder3, exist_ok=True)

    # Get a set of all files in folder1 and folder2
    files_in_folder1 = {f for f in os.listdir(folder1) if os.path.isfile(os.path.join(folder1, f))}
    files_in_folder2 = {f for f in os.listdir(folder2) if os.path.isfile(os.path.join(folder2, f))}
    
    # Combine the sets of files from folder1 and folder2
    all_files_in_folders = files_in_folder1.union(files_in_folder2)

    # Check each file in the source folder
    for file_name in os.listdir(source_folder):
        source_file_path = os.path.join(source_folder, file_name)
        
        # Check if it's a file and not in folder1 or folder2
        if os.path.isfile(source_file_path) and file_name not in all_files_in_folders:
            # Move the file to folder3
            shutil.move(source_file_path, os.path.join(folder3, file_name))
            print(f"Moved: {file_name} to {folder3}")

# Example usage
#source_folder = "G:/My Drive/YOLO data/total_image"  # Replace with your source folder path
#folder1 = "G:/My Drive/YOLO data/images/train"             # Replace with your folder1 path
#folder2 = "G:/My Drive/YOLO data/images/val"              # Replace with your folder2 path
#folder3 = "G:/My Drive/Labering_images"             # Replace with your folder3 path
#move_missing_files(source_folder, folder1, folder2, folder3)