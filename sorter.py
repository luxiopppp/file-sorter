import os
import msvcrt

root_path = input("Directorio a organizar: ")
dirs = os.listdir(root_path)

print("""
        Si no desea alguna carpeta, solo presione enter.
        Si ya existe una carpeta para alguno de estos archivos, proporcione el nombre de esa carpeta.
    """
      )
pic_folder = input("Nombre para la carpeta de imagenes: ")
vid_folder = input("Nombre para la carpeta de videos: ")
aud_folder = input("Nombre para la carpeta de audios: ")
gif_folder = input("Nombre para la carpeta de gifs: ")
doc_folder = input("Nombre para la carpeta de documentos: ")
zip_folder = input("Nombre para la carpeta de archivos comprimidos: ")
set_folder = input("Nombre para la carpeta de instaladores: ")
pro_folder = input("Nombre para la carpeta de programas (ej: .py): ")

delete = input("Desea eliminar las carpetas vacias? (Y/N): ").upper()

del_COUNT = 0

extentions = {
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
        folder_list = {
            pic_folder: "images",
            vid_folder: "videos",
            aud_folder: "audios",
            gif_folder: "gifs",
            doc_folder: "documents",
            zip_folder: "zip",
            set_folder: "setup",
            pro_folder: "programs"
        }
        if all(folder == "" for folder in list(folder_list.keys())):
            print("Debe crear al menos una carpeta")

        for folder, ext in folder_list.items():
            if folder != "":
                os.mkdir(f"{root_path}/{folder}/")
                extentions[folder] = extentions[ext]
                del extentions[ext]
    except OSError:
        print("Ha aparecido un error al crear las carpetas, revisa el directorio para asegurarte que haya espacio")


create_folders()


def sort(file):

    keys = list(extentions.keys())
    for key in keys:
        for ext in extentions[key]:
            if file.endswith(ext):
                return key


def sorting():
    global count, no_ord
    count = 0
    no_ord = 0

    for file in dirs:
        name, ext = os.path.splitext(root_path + file)
        dist = sort(file)
        if dist:
            try:
                os.rename(f"{root_path}/{file}", f"{root_path}/{dist}/{file}")
                count += 1
            except:
                no_ord += 1


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
