import os
import collections
from pprint import pprint

EXT_AUDIO = ['mp3', 'wav', 'raw', 'wma', 'mid', 'midi']
EXT_VIDEO = ['mp4', 'mpg', 'mpeg', 'avi', 'mov', 'flv', 'mkv', 'mwv', 'm4v', 'h264', 'hevc']
EXT_IMGS  = ['png', 'jpg', 'jpeg', 'gif', 'svg', 'bmp', 'psd', 'tiff', 'tif']
EXT_DOCS  = ['txt', 'pdf', 'csv', 'xls', 'xlsx', 'ods', 'doc', 'docx', 'html', 'odt', 'tex', 'ppt', 'pptx', 'log']
EXT_COMPR = ['zip', 'z', '7z', 'rar', 'tar', 'gz', 'rpm', 'pkg', 'deb']
EXT_INSTL = ['dmg', 'exe', 'iso']

# Step 1 - Crete directories where we want to store the files
BASE_PATH = os.path.expanduser('~')
DEST_DIR = ['Audio', 'Video', 'Pictures', 'Documents', 'Application', 'Other', 'Compressed']
for d in DEST_DIR:
    dir_path = os.path.join(BASE_PATH, d)
    if not os.path.isdir(dir_path):
        os.mkdir(dir_path)

#Step 2 - Map files from downloads folder based on their file extension

DOWNLOADS_PATH = os.path.join(BASE_PATH, 'Downloads')
files_mapping = collections.defaultdict(list)
files_list = os.listdir(DOWNLOADS_PATH)

for file_name in files_list:
    file_ext = file_name.split('.')[-1]
    files_mapping[file_ext].append(file_name)

pprint(files_mapping)

#Step 3 - Move All files given a file extension to a target directory
for f_ext, f_list in files_mapping.items():
    if f_ext in EXT_INSTL:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH, 'Applications', file))

    elif f_ext in EXT_AUDIO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH,'Audio', file)) 
    
    elif f_ext in EXT_VIDEO:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH,'Video', file)) 

    elif f_ext in EXT_IMGS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH,'Pictures', file)) 
    
    elif f_ext in EXT_DOCS:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH,'Documents', file)) 

    elif f_ext in EXT_COMPR:
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH,'Compressed', file)) 

    else :
        for file in f_list:
            os.rename(os.path.join(DOWNLOADS_PATH, file), os.path.join(BASE_PATH,'Other', file)) 

    