import os
import shutil
from time import sleep

temp = "C:/Users/Sahaj/AppData/Local/Temp"
opera = "C:/Users/Sahaj/AppData/Local/Opera Software/Opera GX Stable"
disc = "C:/Users/Sahaj/AppData/Roaming/discord"
his1 = "C:/Users/Sahaj/AppData/Roaming/Opera Software/Opera GX Stable/History"
his2 = "C:/Users/Sahaj/AppData/Roaming/Opera Software/Opera GX Stable/History-journal"
cook1 = "C:/Users/Sahaj/AppData/Roaming/Opera Software/Opera GX Stable/Cookies"
cook2 = "C:/Users/Sahaj/AppData/Roaming/Opera Software/Opera GX Stable/Cookies-journal"


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
