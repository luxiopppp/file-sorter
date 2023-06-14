import os

root_path = input("Directorio a organizar: ")
dirs = os.listdir(root_path)

print("Si no desea alguna carpeta, solo presione enter.")
pic_folder = input("Nombre para la carpeta de imagenes: ")
vid_folder = input("Nombre para la carpeta de videos: ")
aud_folder = input("Nombre para la carpeta de audios: ")
gif_folder = input("Nombre para la carpeta de gifs: ")
doc_folder = input("Nombre para la carpeta de documentos: ")
zip_folder = input("Nombre para la carpeta de archivos comprimidos: ")
set_folder = input("Nombre para la carpeta de instaladores: ")
pro_folder = input("Nombre para la carpeta de programas (ej: .py): ")

delete = input("Desea eliminar las carpetas vacias? (Y/N): ").upper()

count = 0
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
        if pic_folder != "":
            os.mkdir(f"{root_path}/{pic_folder}/")
            extentions[pic_folder] = extentions["images"]
            del extentions["images"]
        if vid_folder != "":
            os.mkdir(f"{root_path}/{vid_folder}/")
            extentions[vid_folder] = extentions["videos"]
            del extentions["videos"]
        if aud_folder != "":
            os.mkdir(f"{root_path}/{aud_folder}/")
            extentions[aud_folder] = extentions["audios"]
            del extentions["audios"]
        if gif_folder != "":
            os.mkdir(f"{root_path}/{gif_folder}/")
            extentions[gif_folder] = extentions["gifs"]
            del extentions["gifs"]
        if doc_folder != "":
            os.mkdir(f"{root_path}/{doc_folder}/")
            extentions[doc_folder] = extentions["documents"]
            del extentions["documents"]
        if zip_folder != "":
            os.mkdir(f"{root_path}/{zip_folder}/")
            extentions[zip_folder] = extentions["zip"]
            del extentions["zip"]
        if set_folder != "":
            os.mkdir(f"{root_path}/{set_folder}/")
            extentions[set_folder] = extentions["setup"]
            del extentions["setup"]
        if pro_folder != "":
            os.mkdir(f"{root_path}/{pro_folder}/")
            extentions[pro_folder] = extentions["programs"]
            del extentions["programs"]
        os.mkdir(f"{root_path}/other")
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
    global count
    count = 0

    for file in dirs:
        name, ext = os.path.splitext(root_path + file)
        dist = sort(file)
        if dist:
            count += 1
            try:
                os.rename(f"{root_path}/{file}",
                          f"{root_path}/{dist}/{file}")
            except:
                print(file + " error")
        else:
            try:
                os.rename(f"{root_path}/{file}",
                          f"{root_path}/{dist}/other")
            except:
                print(file + " error")


sorting()

if delete == "Y":
    for root, dire, files in os.walk(root_path, topdown=False):
        if not os.listdir(root):
            os.rmdir(root)
            del_COUNT += 1

print(
    f"""
        Archivos organizados: {count}
        Carpetas eliminadas: {del_COUNT}
    """
)
