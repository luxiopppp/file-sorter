import os
import msvcrt

root_path = input("Root directory: ")
dirs = os.listdir(root_path)

print("""
        If you don't want any of these folders, simply press 'Enter'.
        If a folder already exists for any of these files, please provide the name of that folder.
    """
      )

folder_names = [
    "images",
    "videos",
    "audios",
    "gifs",
    "documents",
    "zip",
    "setup",
    "code"
]

folder_list = {}

for name in folder_names:
    folder = input(f"Name for the {name} folder: ")
    if folder:
        folder_list[name] = folder

delete = input(
    "Do you want to remove the empty folders on the root? (Y/N): ").upper()

count = 0
no_ord = 0
del_COUNT = 0

extensions = {
    "images": [".jpg", ".jpeg", ".png", ".psd", ".webp"],
    "videos": [".mp4", ".mpeg", ".webm", ".avi", ".mov"],
    "audios": [".mp3", ".wav", ".asd", ".m4a", ".ogg"],
    "gifs": [".gif"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "setup": [".msi", ".exe"],
    "code": [".py", ".js", ".html", ".css", ".c", ".cpp", ".php", ".C", ".CPP"]
}


def create_folders():
    try:
        if all(folder == "" for folder in list(folder_list.values())):
            print("At least one folder is needed!")

        for name, folder in folder_list.items():
            if folder != "":
                folder_path = os.path.join(root_path, folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path, exist_ok=True)
                    if name in extensions and name != folder:
                        extensions[folder] = extensions[name]
                        del extensions[name]
    except OSError:
        print("There was an error creating the folders. Please check if there is enough space available in the directory.")


def sort(file, folder_list):
    for key, exts in extensions.items():
        for ext in exts:
            if file.endswith(ext):
                return folder_list[key]
    return None


def sorting(file, count, no_ord):
    dist = sort(file, folder_list)
    if dist:
        try:
            os.rename(os.path.join(root_path, file),
                      os.path.join(root_path, dist, file))
            count += 1
        except:
            no_ord += 1
    return count, no_ord


create_folders()

for file in dirs:
    count, no_ord = sorting(file, count, no_ord)

if delete == "Y":
    for root, dire, files in os.walk(root_path, topdown=False):
        if not os.listdir(root):
            os.rmdir(root)
            del_COUNT += 1

print(
    f"""
        Organized: {count}
        Not organized: {no_ord}
        Removed folders: {del_COUNT}
    """
)

msvcrt.getch()
