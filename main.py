import os
import shutil

def organize_pdfs(root_folder):
    # Dictionary to store PDFs based on their prefixes
    pdf_dict = {}

    # Iterate through all directories and files recursively
    for root, dirs, files in os.walk(root_folder):
        for file in files:
            if file.endswith('.pdf'):
                # Extract the prefix (3 letters) from the file name
                prefix = file[:3]
                # Create a directory in the pdf_dict if not already present
                if prefix not in pdf_dict:
                    pdf_dict[prefix] = []
                # Append the file path to the corresponding prefix key
                pdf_dict[prefix].append(os.path.join(root, file))

    # Create directories for each prefix in the root folder
    for prefix, file_paths in pdf_dict.items():
        prefix_folder = os.path.join(root_folder, prefix)
        os.makedirs(prefix_folder, exist_ok=True)
        # Move PDF files to their corresponding prefix folders
        for file_path in file_paths:
            shutil.move(file_path, prefix_folder)

# Example usage
root_folder = '/path/to/root/folder'
organize_pdfs(root_folder)
