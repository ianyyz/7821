# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import subprocess
import os

def Execute_file(folder_path):
    print("job start")
    # give permission to text2wfreq.unix
    subprocess.check_call(["chmod", "u+x", "text2wfreq.unix"])

    files = os.listdir(folder_path)
    print(files)
    for file_name in files:
        print(file_name)
        new_file_name = file_name[:-3] + "wfreq"
        #subprocess.check_call(["sh","-c", "./text2wfreq.unix", "<", file_name, ">", new_file_name])
        subprocess.check_call("./text2wfreq.unix" + " < " + os.path.join(folder_path,file_name) + " > " + new_file_name, shell=True)

    print("job done")

    return 1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    folder_path = "/home/yuanzhe/Desktop/nyu_material/7871/HW1/code/asia"
    Execute_file(folder_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
