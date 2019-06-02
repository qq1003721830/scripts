# coding=utf-8
# 智联
import adb,os,time



def zhilian():
    """
    zhilian
    :return:
    """
    os.system("adb shell am start -n com.zhaopin.social/.SplashActivity")
    time.sleep(15)
    os.system("adb shell  input tap 724 1860")
    time.sleep(15)
    os.system("adb shell  input tap 360 210")
    time.sleep(15)
    os.system("adb shell am force-stop com.zhaopin.social")
    time.sleep(15)



def liepin():e
    """
    liepin
    :return:
    """
    os.system("adb shell am start -n com.lietou.mishu/.activity.LPSplashActivity")
    time.sleep(15)
    os.system("adb shell  input tap 930 1848")
    time.sleep(15)
    os.system("adb shell  input tap 919 1623")
    time.sleep(15)
    os.system("adeb shell am force-stop com.lietou.mishu")
    time.sleep(15)



for n in range(24):
    zhilian()
    liepin()
    time.sleep(1200)