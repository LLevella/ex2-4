import os
import sys

def get_params():
    migrations = 'Migrations'
    file_extension = "sql"
    ps = []
    lcs = len(sys.argv)
    if lcs > 1:
        for i in range(1,lcs):
            ps.append(sys.argv[i])
        if lcs < 3:
             ps.append(file_extension)
    else:
        ps.append(migrations)
        ps.append(file_extension)
    return ps



def create_abs_dir_name(dir_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    migr_dir = os.path.join(current_dir,dir_name)
    if not os.path.lexists(migr_dir):
        return None
    return migr_dir

def search_files_in_directory(dir_name):
    files_names = []
    migr_dir = create_abs_dir_name(dir_name)
    if migr_dir is not None:
        files_names = os.listdir(migr_dir)
    return files_names


def get_files_by_extensions(dir_name, files_names, file_extension):
    f_by_ext = []
    migr_dir = create_abs_dir_name(dir_name)
    if migr_dir is not None:
        for fn in files_names:
            s_ext = fn.split(".")[-1]
            if file_extension.count(s_ext.lower())>0:
                f_by_ext.append(os.path.join(migr_dir, fn))
    return f_by_ext

def get_files_by_words(sparam, l_files):
    new_l_files=[]
    for l_file in l_files:
        with open(l_file, 'r') as fin:
            text = fin.read()
            n = text.find(sparam)
            if n!=-1:
                new_l_files.append(l_file)

    return new_l_files
