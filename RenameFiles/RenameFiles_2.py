import os

##### METHOD 2
def rename_photos_2():
    file_path = "photos"
    for file in os.listdir(file_path):
        print(file, end='\t\t\t')
        f_name, f_ext = os.path.splitext(file)

        f_title, f_info, f_num = f_name.split('-')

        f_title = f_title.strip()
        f_info = f_info.strip()
        f_num = f_num.strip()[1:].zfill(2)

        new_name = "{}-{}-{}{}".format(f_num, f_info, f_title, f_ext)
        print(new_name)

        file_path_old = f'{file_path}/{file}'
        file_path_new = f'{file_path}/{new_name}'

        os.rename(file_path_old, file_path_new)

if __name__ == "__main__":
    rename_photos_2()