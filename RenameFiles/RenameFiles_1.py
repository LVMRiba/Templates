import pathlib

##### METHOD 1
def rename_photos_1():
    path = pathlib.Path('.') / "photos"
    for folder in path.iterdir():
        print(folder)
        if folder.is_dir():
            counter = 1
            for file in folder.iterdir():
                if file.is_file():
                    new_file = folder.name + str(counter) + file.suffix
                    file.rename(path/folder.name/new_file)
                    counter += 1
            print(counter)

if __name__ == "__main__":
    rename_photos_1()