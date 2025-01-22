import os
import glob

def create_missing_labels(folder1, folder2):
    i = 0
    # Get all image files in folder1 (you can modify the extensions as needed)
    image_extensions = ['*.jpg', '*.jpeg', '*.png', '*.gif', '*.bmp']
    image_files = []
    for ext in image_extensions:
        image_files.extend(glob.glob(os.path.join(folder1, ext)))
    
    # Check each image file and create a corresponding label.txt if it doesn't exist
    for image_file in image_files:
        # Get the base name of the image file (without extension)
        base_name = os.path.splitext(os.path.basename(image_file))[0]
        # Construct the corresponding label file path
        label_file_path = os.path.join(folder2, f"{base_name}.txt")  # Changed to .txt

        # Check if the label file exists
        if not os.path.exists(label_file_path):
            # Create a blank label file
            with open(label_file_path, 'w') as label_file:
                label_file.write('')  # Write an empty string to create a blank file
            print(f"Created: {label_file_path}")
            i +=1
        else:
            print(f"Label file already exists: {label_file_path}")

    print(f"Total label files created: {i}")

# Example usage
folder1 = r"E:\Yolo_data\images" # Replace with your folder1 path
folder2 = r"E:\Yolo_data\labels" # Replace with your folder2 path
create_missing_labels(folder1, folder2)