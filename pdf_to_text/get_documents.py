import os


def get_documents(dir_path):
# list to store files
    docs = []

# Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            docs.append(path)
    return docs
