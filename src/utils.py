import json
from zipfile import ZipFile
import os


def extract_file(zip_file_name, filename):
    with ZipFile(zip_file_name, "r") as zip_obj:
        zip_obj.extract(filename)


def download_kaggle_dataset(dataset):
    os.system(f"kaggle datasets download -d {dataset}")
    file_name = dataset.split("/")[1]
    return f"{file_name}.zip"


def load_json_file(json_filename):
    with open(json_filename) as json_file:
        return json.load(json_file)


def fix_json_file(kv, filename):
    with open(filename, "r") as file:
        filedata = file.read()
    for k, v in kv.items():
        filedata = filedata.replace(k, v)
    with open(filename, "w") as file:
        file.write(filedata)
        
def parse_percent(str_percent):
    try:
        return int(str_percent.strip("%"))
    except ValueError:
        pass


def parse_ratio(str_ratio):
    try:
        male, female = [int(number) for number in str_ratio.split(":")]
        return male / female if female != 0 else 1
    except ValueError:
        pass