import os

def compare_folders(folder1, folder2):
    # Ensure the paths are valid
    if not os.path.exists(folder1):
        print(f"Error: {folder1} does not exist")
        return
    if not os.path.exists(folder2):
        print(f"Error: {folder2} does not exist")
        return

    # Get the list of files in both folders
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))

    # Find missing files in folder2 and extra files in folder2
    missing_files = files1 - files2
    extra_files = files2 - files1

    # Output the results
    print("Missing files in", folder2, ":")
    for file in missing_files:
        print(file)

    print("\nExtra files in", folder2, ":")
    for file in extra_files:
        print(file)

# Set the folder paths
folder1 = r"C:\Sinan-Files\personal-projects\python-projects\Folder 1"
folder2 = r"C:\Sinan-Files\personal-projects\python-projects\Folder 2"

# Run the comparison
compare_folders(folder1, folder2)
