import os
import msvcrt

root_path = input("Directorio a organizar: ")
dirs = os.listdir(root_path)

print("""
        Si no desea alguna carpeta, solo presione enter.
        Si ya existe una carpeta para alguno de estos archivos, proporcione el nombre de esa carpeta.
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
    "programs"
]

folder_list = {}

for name in folder_names:
    folder = input(f"Nombre para la carpeta de {name}: ")
    if folder:
        folder_list[name] = folder

delete = input("Desea eliminar las carpetas vacias? (Y/N): ").upper()

del_COUNT = 0

extensions = {
    "images": [".jpg", ".jpeg", ".png", ".psd", ".webp"],
    "videos": [".mp4", ".mpeg", ".webm", ".avi", ".mov"],
    "audios": [".mp3", ".wav", ".asd", ".m4a", ".ogg"],
    "gifs": [".gif"],
    "documents": [".pdf", ".docx", ".csv", ".xlsx", ".pptx", ".doc", ".ppt", ".xls"],
    "zip": [".zip", ".tgz", ".rar", ".tar"],
    "setup": [".msi", ".exe"],
    "programs": [".py", ".c", ".cpp", ".php", ".C", ".CPP"]
}


def create_folders():
    try:
        if all(folder == "" for folder in list(folder_list.values())):
            print("Debe crear al menos una carpeta")

        for name, folder in folder_list.items():
            if folder != "":
                folder_path = os.path.join(root_path, folder)
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path, exist_ok=True)
                    if name in extensions and name != folder:
                        extensions[folder] = extensions[name]
                        del extensions[name]
    except OSError:
        print("Ha aparecido un error al crear las carpetas, revise el directorio")


def sort(file):
    for key, exts in extensions.items():
        for ext in exts:
            if file.endswith(ext):
                return key
    return None


def sorting():
    global count, no_ord
    count = 0
    no_ord = 0

    for file in dirs:
        name, ext = os.path.splitext(file)
        dist = sort(file)
        if dist:
            try:
                os.rename(os.path.join(root_path, file),
                          os.path.join(root_path, dist, file))
                count += 1
            except:
                no_ord += 1


create_folders()
sorting()

if delete == "Y":
    for root, dire, files in os.walk(root_path, topdown=False):
        if not os.listdir(root):
            os.rmdir(root)
            del_COUNT += 1

print(
    f"""
        Archivos organizados: {count}
        Archivos sin organizar: {no_ord}
        Carpetas eliminadas: {del_COUNT}
    """
)

msvcrt.getch()
