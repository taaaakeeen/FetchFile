import os
import sys
import shutil
import csv
from pathlib import Path
from datetime import datetime
import logging

logger = logging.getLogger(__name__)
FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(filename='FetchFile.log', level=logging.DEBUG, format=FORMAT, datefmt='%Y-%m-%d %H:%M:%S', encoding='utf-8')

def make_dir():
    try:
        dt_now = datetime.now()
        dir_path = dt_now.strftime('%Y_%m_%d_%H_%M_%S')
        os.makedirs(dir_path, exist_ok=True)
        message = f'success make dir -> {dir_path}'
        logging.info(message)
        return dir_path
    except Exception as e:
        message = str(e)
        logging.info(message)
        sys.exit()

def save_file(file_path, save_dir_path):
    try:
        shutil.copy2(file_path, save_dir_path)
        message = f'success fetch file -> {file_path}'
        logging.info(message)
    except Exception as e:
        message = str(e)
        logging.info(message)

def save_dir(dir_path, save_dir_path):
    try:
        shutil.copytree(dir_path, save_dir_path, dirs_exist_ok=True)
        message = f'success fetch dir -> {dir_path}'
        logging.info(message)
    except Exception as e:
        message = str(e)
        logging.info(message)

def get_fetch_csv():
    try:
        file_path = 'FetchFile.csv'
        with open(file_path, encoding='utf-8') as f:
            reader = csv.reader(f)
            next(reader) # skip header
            l = [row for row in reader]
        return l
    except Exception as e:
        message = str(e)
        logging.info(message)
        sys.exit()

def main():

    # get save target
    l = get_fetch_csv()

    # make save dir
    save_dir_path = make_dir()

    for item in l:

        # obj_name = item[0]
        obj_path = item[1]
        print(obj_path)

        # is exist?
        if os.path.exists(obj_path):

            # is file?
            if os.path.isfile(obj_path):
                save_file(obj_path, save_dir_path)

            # is dir?
            else:
                dir_name = Path(obj_path).name
                save_dir(obj_path, os.path.join(save_dir_path, dir_name))

if __name__ == '__main__':
    main()