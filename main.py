import os
import time
import pynput
from pynput.keyboard import Key, Controller


def run_main(runtime):
    ONE_DAY = 60 * 60 * 24
    ONE_HOUR = 60 * 60
    # keyboard = Controller()
    while (1):
        nowtime = time.localtime()
        if nowtime[3] == runtime:
            os.popen("weixin.exe")
            print("execute at" + time.ctime())
            time.sleep(ONE_DAY)
        else:
            time.sleep(ONE_HOUR)
        # print(os.getcwd(), time.ctime())
        # os.popen("weixin.exe")
        # # os.system("weixin.exe")
        # print("push finish")
        # # keyboard.press(Key.space)
        # # keyboard.release(Key.space)
        # time.sleep(ONE_DAY)


if __name__ == "__main__":
    run_main(7)
    # keyboard = Controller()
    # keyboard.type("中文123asv")

