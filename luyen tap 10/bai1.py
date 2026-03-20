def get_file_name(path):
    return path.replace("\\", "/").split("/")[-1]
