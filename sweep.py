import list_dir
import hashlib
import os

def sweep(dir):
    if dir:
        if isinstance(dir, list) and dir:
            dir = ''.join(dir)
        source_path = dir
        source_dir = list_dir.list_dirs(source_path)
        new_dir_list = []
        # print("Directory: " + dir)
        yield "Directory: ", dir

        for path in source_dir:
            if not os.path.isdir(path):
                with open(path, 'rb') as file:
                    bytes = file.read()
                    hashedFile = hashlib.sha256(bytes).hexdigest()
                    # print(path + "\t\t\t\t" + hashedFile)
                    yield hashedFile, path
            else:
                new_dir_list.append(path)
                # sweep(new_dir_list)

        for path in sweep(new_dir_list):
            yield path
