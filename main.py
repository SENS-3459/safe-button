import os
import shutil
from time import sleep
temp = os.path.expanduser("~/AppData/Local/Temp") # temp files folder
browser = os.path.expanduser("~/AppData/Local/Google/Chrome/ser Data/Default") # browser cache, history and cookies
disc = os.path.expanduser("~/AppData/Roaming/discord") # discord cache folder


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
    if sure == "y" or "yes":
        if remove(browser):
            print("Browser- Done")
        else:
            print("Browser- Error Occured")

        if remove(disc):
            print("Disc- Done")
        else:
            print("Disc- Error Occured")
            
        if tempRem():
            print("TempFiles- Done")
        else:
            print("TempFiles- Error Occured")
        sleep(1.5)
    else:
        quit()
