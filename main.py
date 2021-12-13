import os
import shutil
from time import sleep
temp = os.path.expanduser("~/AppData/Local/Temp") # temp files folder
opera = os.path.expanduser("~/AppData/Local/Opera Software/Opera GX Stable") # browser cache folder
disc = os.path.expanduser("~/AppData/Roaming/discord") # disc cache folder
his1 = os.path.expanduser("~/AppData/Roaming/Opera Software/Opera GX Stable/History") # history file
his2 = os.path.expanduser("~/AppData/Roaming/Opera Software/Opera GX Stable/History-journal") # history-journal file
cook1 = os.path.expanduser("~/AppData/Roaming/Opera Software/Opera GX Stable/Cookies") # cookies file
cook2 = os.path.expanduser("~/AppData/Roaming/Opera Software/Opera GX Stable/Cookies-journal") # cookies-journal file


def remove(loc):
    if os.path.isdir(loc):
        try:
            shutil.rmtree(loc)
            return True
        except:
            return False
    else:
        try:
            os.remove(loc)
            return True
        except:
            return False


def tempRem():
    try:
        for root, dirs, files in os.walk(temp, topdown=True):
            if len(files) != 0:
                for f in files:
                    try:
                        os.remove(os.path.join(root, f))
                    except:
                        pass
        return True
    except:
        return False


if __name__ == "__main__":
    sure = input("Sure?")
    if sure == "f":
        if remove(opera):
            print("OperCache- Done")
        else:
            print("OperCache- Error Occured")

        if remove(disc):
            print("DiscCache- Done")
        else:
            print("DiscCache- Error Occured")

        if remove(his1) and remove(his2):
            print("His- Done")
        else:
            print("His- Error Occured")

        if remove(cook1) and remove(cook2):
            print("Cook- Done")
        else:
            print("Cook- Error Occured")
        if tempRem():
            print("Temp- Done")
        else:
            print("Temp- Error Occured")
        sleep(1.5)
    else:
        quit()
