import csv
import os
from PIL import Image


TENSORFLOW_LOCATION = "tensorflow-for-poets-2\\"
DATA_LOCATION = "traditional-decor-patterns\\"
CATEGORY_NAME = "decor"


def read_csv():
    csv_data = []
    with open(DATA_LOCATION + "decor.csv") as file:
        reader = csv.DictReader(file)
        for line in reader:
            csv_data.append(line)
    return csv_data


def create_folder(folder_name):
    if os.path.exists(TENSORFLOW_LOCATION + "tf_files\images\\" + folder_name):
        if os.path.isdir(TENSORFLOW_LOCATION + "tf_files\images\\" + folder_name):
            pass
    else:
        os.makedirs(TENSORFLOW_LOCATION + "tf_files\images\\" + folder_name)


def convert_png_to_jpeg(image_name, folder_name):
    split = image_name.split(".")
    if split[1] == "png":
        im = Image.open(DATA_LOCATION + "decor\\" + image_name)
        rgb_im = im.convert("RGB")
        rgb_im.save(TENSORFLOW_LOCATION + "tf_files\images\\" + folder_name + "\\" + split[0] + ".jpg")


def copy_image(csv_data, column):
    for row in csv_data:
        if row["type"] == "product":
            folder_name = row[column].lower()
            if 'ĺ‚' in folder_name:
                folder_name = folder_name.replace('ĺ‚','l')
            create_folder(folder_name)
            convert_png_to_jpeg(row["file"],folder_name)


if __name__ == "__main__":
    csv_data = read_csv()
    copy_image(csv_data,CATEGORY_NAME)