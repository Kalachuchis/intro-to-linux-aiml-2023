import os
import random
import string

def random_string(stringLength=10):
    """Generate a random string with the combination of lowercase and uppercase letters """
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))

def create_folders_and_files(num_folders, num_files_per_folder):
    """Create a specified number of random folders and files inside each folder"""
    for i in range(num_folders):
        folder_name = "folder_" + str(i)
        os.makedirs(folder_name)
        for j in range(num_files_per_folder):
            file_name = random_string() + ".txt"
            with open(os.path.join(folder_name, file_name), "w") as file:
                file.write("This is a random file")

# Example usage: create 10 folders and 5 files inside each folder
create_folders_and_files(5, 5)
