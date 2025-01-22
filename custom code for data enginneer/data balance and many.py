import os
import shutil
from collections import defaultdict
import random

def create_balanced_dataset(label_dir, output_dir, train_ratio=0.7, val_ratio=0.2):
    # Create output directories
    os.makedirs(os.path.join(output_dir, 'train'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'val'), exist_ok=True)
    os.makedirs(os.path.join(output_dir, 'test'), exist_ok=True)
    print("Create dir folder done!")
    # Dictionary to hold counts of each class and their files
    class_files = defaultdict(list)
    
    # Read all label files and group them by class
    print("Reading files...")
    label_files = [f for f in os.listdir(label_dir) if f.endswith('.txt')]
    
    for label_file in label_files:
        class_id = None
        with open(os.path.join(label_dir, label_file), 'r') as f:
            for line in f:
                class_id = line.split()[0]  # Assuming class ID is the first element
                break  # We only need to know the class for this label file
        class_files[class_id].append(label_file)
    print("Planing for balance obj...")
    # Initialize counters for train, val, and test datasets
    train_class_counts = defaultdict(int)
    val_class_counts = defaultdict(int)
    test_class_counts = defaultdict(int)

    # Shuffle and split files for each class
    for class_id, files in class_files.items():
        random.shuffle(files)
        total_files = len(files)

        # Calculate the number of files for each dataset based on the ratios
        train_count = int(total_files * train_ratio)
        val_count = int(total_files * val_ratio)
        test_count = total_files - train_count - val_count  # Remaining files for test

        # Select files for each split
        train_files = files[:train_count]
        val_files = files[train_count:train_count + val_count]
        test_files = files[train_count + val_count:]

        print("Copying files...")
        # Move files to corresponding directories and count objects
        for file in train_files:
            shutil.copy(os.path.join(label_dir, file), os.path.join(output_dir, 'train', file))
            train_class_counts[class_id] += 1
        
        for file in val_files:
            shutil.copy(os.path.join(label_dir, file), os.path.join(output_dir, 'val', file))
            val_class_counts[class_id] += 1
        
        for file in test_files:
            shutil.copy(os.path.join(label_dir, file), os.path.join(output_dir, 'test', file))
            test_class_counts[class_id] += 1

    # Print the counts and percentages
    print("Dataset creation complete!")
    
    # Total counts
    total_train = sum(train_class_counts.values())
    total_val = sum(val_class_counts.values())
    total_test = sum(test_class_counts.values())

    print("\nClass distribution in Train set:")
    for class_id, count in train_class_counts.items():
        print(f"Class {class_id}: {count} ({(count / total_train) * 100:.2f}%)")
    
    print("\nClass distribution in Validation set:")
    for class_id, count in val_class_counts.items():
        print(f"Class {class_id}: {count} ({(count / total_val) * 100:.2f}%)")
    
    print("\nClass distribution in Test set:")
    for class_id, count in test_class_counts.items():
        print(f"Class {class_id}: {count} ({(count / total_test) * 100:.2f}%)")

# Example usage
#create_balanced_dataset(r"E:\Yolo_data\base_labels", r"E:\Yolo_data\labels")
"------------------------------------------------------------------------------------------------------------------------"
import os
from collections import Counter

def analyze_yolo_labels(label_folder, num_classes):
    class_counter = Counter()
    
    # Iterate through all files in the label folder
    for filename in os.listdir(label_folder):
        if filename.endswith('.txt'):  # Check for YOLO label files
            file_path = os.path.join(label_folder, filename)
            with open(file_path, 'r') as file:
                for line in file:
                    class_index = int(line.split()[0])  # Get the class index from the line
                    class_counter[class_index] += 1
    
    # Calculate total number of labels
    total_labels = sum(class_counter.values())
    
    # Prepare output including missing classes
    class_percentage = {}
    for cls in range(num_classes):
        count = class_counter.get(cls, 0)
        percentage = (count / total_labels * 100) if total_labels > 0 else 0
        class_percentage[cls] = {
            'count': count,
            'percentage': percentage
        }
    
    return class_percentage

# Example usage:
label_folder_path = r"G:\My Drive\New_data\fixed laber\val"
num_classes = 9  # Change this to the total number of classes you expect
#class_info = analyze_yolo_labels(label_folder_path, num_classes)

# Print results
#for cls, info in class_info.items():
    #print(f"Class {cls}: Count = {info['count']}, Percentage = {info['percentage']:.2f}%")
"----------------------------------------------------------------------------------------------------------------------"
import os
import shutil

def move_labeled_images(images_folder, labels_folder, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)
    
    # Initialize a counter for the number of images moved
    moved_count = 0
    
    # Iterate through the images folder
    for image in os.listdir(images_folder):
        # Get the base name without extension
        base_name, ext = os.path.splitext(image)
        
        # Construct the expected label file name
        label_file = f"{base_name}.txt"
        
        # Check if the label file exists in the labels folder
        if label_file in os.listdir(labels_folder):
            # Construct full file paths
            src_path = os.path.join(images_folder, image)
            dest_path = os.path.join(output_folder, image)
            
            # Move the image to the output folder
            shutil.move(src_path, dest_path)
            moved_count += 1
    
    # Print out the number of images moved
    print(f"Moved {moved_count} images to the output folder.")
# Example usage
images_folder = r"E:\Yolo_data\base_images"
labels_folder = r"E:\Yolo_data\labels\train"
output_folder = r"E:\Yolo_data\images\train"

move_labeled_images(images_folder, labels_folder, output_folder)


#"G:\My Drive\Fixed_data\images"
#"E:\fixing_labels"