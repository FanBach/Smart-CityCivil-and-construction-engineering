import os

def remove_and_adjust_labels(input_folder, output_folder, classes_to_remove):
   
    # Sort classes to remove for consistent mapping
    classes_to_remove = sorted(classes_to_remove)
    
    # Create a mapping from old class indices to new class indices
    class_mapping = {}
    new_index = 0
    for old_index in range(max(classes_to_remove) + 1 + len(classes_to_remove)):
        if old_index not in classes_to_remove:
            class_mapping[old_index] = new_index
            new_index += 1
    
    # Ensure output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Process each label file
    for file_name in os.listdir(input_folder):
        if file_name.endswith(".txt"):
            input_path = os.path.join(input_folder, file_name)
            output_path = os.path.join(output_folder, file_name)
            
            with open(input_path, 'r') as infile, open(output_path, 'w') as outfile:
                for line in infile:
                    parts = line.split()
                    class_index = int(parts[0])  # First value is the class index
                    
                    # Skip lines with classes to remove
                    if class_index in classes_to_remove:
                        continue
                    
                    # Adjust class index and write the line
                    parts[0] = str(class_mapping[class_index])
                    outfile.write(' '.join(parts) + '\n')

# Example usage:
# Remove class 1 (B) and class 3 (D), adjust indices accordingly
remove_and_adjust_labels(
    input_folder=r"G:\My Drive\New_data\fixed_yolo_data\labels\test",
    output_folder=r"G:\My Drive\New_data\fixed laber\test",
    classes_to_remove=[1,2,4,5]
)

#--------------------------------------------------------------------------------------

import os
import shutil

def move_images_by_class(label_folder, image_folder, output_folder, target_classes, valid_extensions=None):
    print("start moving relabel images")
    index = 0
    # Default valid extensions if none are provided
    if valid_extensions is None:
        valid_extensions = [".jpg", ".jpeg", ".png", ".bmp", ".tiff"]

    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Iterate through label files
    for label_file in os.listdir(label_folder):
        if label_file.endswith(".txt"):
            label_path = os.path.join(label_folder, label_file)
            base_name = os.path.splitext(label_file)[0]

            # Find the corresponding image file by checking valid extensions
            image_path = None
            for ext in valid_extensions:
                potential_image = os.path.join(image_folder, base_name + ext)
                if os.path.exists(potential_image):
                    image_path = potential_image
                    break

            # Skip if no corresponding image is found
            if image_path is None:
                print(f"No image found for label: {label_file}")
                index +=1
                continue
            
            # Check if any target class is present in the label file
            with open(label_path, 'r') as file:
                for line in file:
                    class_id = int(line.split()[0])  # First value is the class ID
                    if class_id in target_classes:
                        # Move the image to the output folder
                        shutil.move(image_path, os.path.join(output_folder, os.path.basename(image_path)))
                        break  # No need to check further, move to the next label file
    print("moving relabel images done! ", index)

# Example usage:
# Move images with classes 1 or 3 to a new folder for re-labeling
#move_images_by_class(
    #label_folder=r"G:\My Drive\New_data\fixed_yolo_data\labels\val",
    #image_folder=r"G:\My Drive\New_data\fixed_yolo_data\images\val",
    #output_folder=r"E:\relabel_data\val",
    #target_classes=[1,2,4,5]
#)

