import os
from concurrent.futures import ThreadPoolExecutor

def get_files_in_dir(dir_path):
    for file_name in os.listdir(dir_path):
        yield os.path.join(dir_path, file_name)

def sort_files_by_extension(files):
    file_groups = {}
    for file in files:
        extension = file.split(".")[-1]
        if extension not in file_groups:
            file_groups[extension] = []
        file_groups[extension].append(file)

    for extension, files in file_groups.items():
        for file in files:
            yield file

def move_file(file_path, dest_dir):
    os.rename(file_path, os.path.join(dest_dir, os.path.basename(file_path)))

def process_dir(dir_path, dest_dir):
    files = get_files_in_dir(dir_path)
    for file in sort_files_by_extension(files):
        move_file(file, dest_dir)

def main():
    src_dir = "Хлам"
    dest_dir = "Впорядкований хлам"

    # Create a ThreadPoolExecutor with 4 worker threads
    with ThreadPoolExecutor(max_workers=4) as executor:
        # Iterate through directories and submit tasks for processing
        for dir_path, _, _ in os.walk(src_dir):
            executor.submit(process_dir, dir_path, dest_dir)

if __name__ == "__main__":
    main()
