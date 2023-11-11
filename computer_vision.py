import os
import cv2

path_folder = "images"
def rename_files(path, list_name):
    # Rename: "photo0.jpg", "photo1.jpg" Standard for examples...
    for position, name_files in enumerate(list_name):
        prefix = "photo"
        extension = name_files.split(".")[-1]
        new_name = f"{prefix}{position}.{extension}"
        path_origin = f"{path}/{name_files}"
        path_new = f"{path}/{new_name}"
        if new_name not in list_name:
            os.rename(path_origin, path_new)
    return os.listdir(path)


def show_images(folder):

    for image_name in folder:
        image = cv2.imread(f"{path_folder}/{image_name}")
        if image is None:
            print("Não foi possível abrir essa imagem")
            exit()
        cv2.namedWindow("Imagem", cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty("Imagem", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        cv2.imshow("Imagem", image)
        cv2.waitKey(1000)
        cv2.destroyAllWindows()


def main():
    list_name_files = os.listdir(path_folder)
    list_name_files = rename_files(path_folder, list_name_files)

    show_images(list_name_files)


main()
