# coding=utf-8

# Last login: Mon Jun  3 00:28:40 on ttys000
# FOXdeMacBook-Air:~ FOX$ adb shell
# shell@pisces:/ $ su
# root@pisces:/ #
#
# #查看手机应用程序安装的第三方包
# adb shell pm list package -3
# #使用logcat获取应用程序活动（https://blog.csdn.net/jlminghui/article/details/40622103）
# adb logcat ActivityManager:I *:s
#
# #操作智联
# adb shell am start -n com.zhaopin.social/.SplashActivity
# #点击简历,点击刷新
# adb shell  input tap 724 1860
# adb shell  input tap 360 210
# #关闭程序
# adb shell am force-stop com.zhaopin.social
#
# #操作猎聘
# adb shell am start -n com.lietou.mishu/.activity.LPSplashActivity
# #点击简历,点击刷新
# adb shell  input tap 930 1848
# adb shell  input tap 919 1623
# #关闭程序
# adb shell am force-stop com.lietou.mishu
#
# #使用os.system()遥控
#
# 以上实现时实现思路


import os,time

def zhilian():
    """
    zhilian
    :return:
    """
    os.system("adb shell am start -n com.zhaopin.social/.SplashActivity")
    time.sleep(10)
    os.system("adb shell  input tap 724 1860")
    time.sleep(10)
    os.system("adb shell  input tap 360 210")
    time.sleep(10)
    os.system("adb shell am force-stop com.zhaopin.social")
    time.sleep(10)

def liepin():
    """
    liepin
    :return:
    """
    os.system("adb shell am start -n com.lietou.mishu/.activity.LPSplashActivity")
    time.sleep(10)
    os.system("adb shell  input tap 930 1848")
    time.sleep(10)
    os.system("adb shell  input tap 919 1623")
    time.sleep(10)
    os.system("adb shell am force-stop com.lietou.mishu")
    time.sleep(10)

for n in range(24):
    zhilian()
    liepin()
    time.sleep(5)