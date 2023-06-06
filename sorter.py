import os

root_path = input("Directorio a organizar: ")
dirs = os.listdir(root_path)

delete = input("Desea eliminar las carpetas vacias? (Y/N): ").upper()


def sort():
    try:
        os.mkdir(f"{root_path}/.pics/")
        os.mkdir(f"{root_path}/.vids/")
        os.mkdir(f"{root_path}/.auds/")
        os.mkdir(f"{root_path}/.gifs/")
        os.mkdir(f"{root_path}/.docs/")
        os.mkdir(f"{root_path}/.docs/.pdfs")
    except OSError:
        print("Carpeta ya existente")

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
            os.rename(f"{root_path}\\{file}", f"{root_path}/.pics/{file}")
            PIC_COUNT += 1
        if ext in [".mp4", ".mpeg", ".webm", ".avi", ".mov"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/.vids/{file}")
            VID_COUNT += 1
        if ext in [".mp3", ".wav", ".asd", ".m4a", ".ogg"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/.auds/{file}")
            AUD_COUNT += 1
        if ext in [".gif"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/.gifs/{file}")
            GIF_COUNT += 1
        if ext in [".doc", ".docx"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/.docs/{file}")
            DOC_COUNT += 1
        if ext in [".pdf"]:
            os.rename(f"{root_path}\\{file}", f"{root_path}/.docs/.pdfs/{file}")
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
