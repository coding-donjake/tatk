import os

def list_folders(path):
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    count = 0
    
    for folder in folders:
        count += 1
        print(f'[{count}] {folder}')
        
    return folders


def select_folder(path, label):
    folders = list_folders(path)
    
    if len(folders) <= 0:
        print(f'No {label} found.')
        return None
    
    index = int(input(f'Select {label}:')) - 1
    
    return folders[index]
