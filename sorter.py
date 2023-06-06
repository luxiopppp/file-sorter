import os

root_path = input("Directorio a organizar: ")
dirs = os.listdir(root_path)

print("Si no desea alguna carpeta, solo presione enter.")
pic_folder = input("Nombre para la carpeta de imagenes: ")
vid_folder = input("Nombre para la carpeta de videos: ")
aud_folder = input("Nombre para la carpeta de audios: ")
gif_folder = input("Nombre para la carpeta de gifs: ")
doc_folder = input("Nombre para la carpeta de documentos: ")
pdf_folder = input("Nombre para la carpeta de pdf: ")

delete = input("Desea eliminar las carpetas vacias? (Y/N): ").upper()


def create_folders():
    try:
        if pic_folder != "":
            os.mkdir(f"{root_path}/{pic_folder}/")
        if vid_folder != "":
            os.mkdir(f"{root_path}/{vid_folder}/")
        if aud_folder != "":
            os.mkdir(f"{root_path}/{aud_folder}/")
        if gif_folder != "":
            os.mkdir(f"{root_path}/{gif_folder}/")
        if doc_folder != "":
            os.mkdir(f"{root_path}/{doc_folder}/")
        if pdf_folder != "":
            os.mkdir(f"{root_path}/{pdf_folder}/")
    except OSError:
        print("Carpeta ya existente")


def sort():
    create_folders()

    PIC_COUNT = 0
    VID_COUNT = 0
    AUD_COUNT = 0
    GIF_COUNT = 0
    DOC_COUNT = 0
    PDF_COUNT = 0
    DEL_COUNT = 0

    for file in dirs:
        # print(file)
        name, ext = os.path.splitext(root_path + file)

        if ext in [".jpg", ".jpeg", ".png", ".psd", ".webp"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/{pic_folder}/{file}")
            PIC_COUNT += 1
        if ext in [".mp4", ".mpeg", ".webm", ".avi", ".mov"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/{vid_folder}/{file}")
            VID_COUNT += 1
        if ext in [".mp3", ".wav", ".asd", ".m4a", ".ogg"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/{aud_folder}/{file}")
            AUD_COUNT += 1
        if ext in [".gif"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/{gif_folder}/{file}")
            GIF_COUNT += 1
        if ext in [".doc", ".docx"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/{doc_folder}/{file}")
            DOC_COUNT += 1
        if ext in [".pdf"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/{pdf_folder}/{file}")
            PDF_COUNT += 1

    if delete == "Y":
        for root, dire, files in os.walk(root_path, topdown=False):
            if not os.listdir(root):
                os.rmdir(root)
                DEL_COUNT += 1

    print(
        f"""
            Cantidad de imagenes: {PIC_COUNT}
            Cantidad de videos: {VID_COUNT}
            Cantidad de audios: {AUD_COUNT}
            Cantidad de gif: {GIF_COUNT}
            Cantidad de documentos: {DOC_COUNT}
            Cantidad de pdf: {PDF_COUNT}
            Carpetas eliminadas: {DEL_COUNT}
        """
    )


sort()
