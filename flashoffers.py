# -- coding: utf-8 --
import os,time


"""
思路
Last login: Mon Jun  3 00:28:40 on ttys000
FOXdeMacBook-Air:~ FOX$ adb shell
shell@pisces:/ $ su
root@pisces:/ #

#查看手机应用程序安装的第三方包
adb shell pm list package -3
#使用logcat获取应用程序活动（https://blog.csdn.net/jlminghui/article/details/40622103）
adb logcat ActivityManager:I *:s

#操作智联
adb shell am start -n com.zhaopin.social/.SplashActivity
#点击简历,点击刷新
adb shell  input tap 724 1860
adb shell  input tap 360 210
#关闭程序
adb shell am force-stop com.zhaopin.social

#操作猎聘
adb shell am start -n com.lietou.mishu/.activity.LPSplashActivity
#点击简历,点击刷新
adb shell  input tap 930 1848
adb shell  input tap 919 1623
#关闭程序
adb shell am force-stop com.lietou.mishu

#使用os.system()遥控

以上实现时实现思路
push-->手机端端qpython3
adb push flashoffers.py /storage/emulated/0/qpython
"""




def zhilian():
    """
    zhilian
    :return:
    """

    os.system("adb shell am start -n com.zhaopin.social/.SplashActivity")
    time.sleep(10)

    # 刷新简历状态
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


def qiancheng():
    """
    liepin
    :return:
    """
    os.system("adb shell am start -n com.job.android/.pages.common.home.AppHomeActivity")
    time.sleep(10)
    os.system("adb shell  input tap 658 1840")
    time.sleep(10)
    os.system("adb shell  input tap 528 550")
    time.sleep(10)
    os.system("adb shell am force-stop com.job.android")
    time.sleep(10)


def zhuoping():
    """
    liepin
    :return:
    """
    os.system("adb shell am start -n com.zhaopin.highpin/.page.resume.ResumeTabActivity")
    time.sleep(10)
    os.system("adb shell  input tap 658 1840")
    time.sleep(10)
    os.system("adb shell  input tap 528 550")
    time.sleep(10)
    os.system("adb shell am force-stop com.job.android")
    time.sleep(10)



# for n in range(24):
#     print(n)
#     zhilian()
#     liepin()
#     qiancheng()
#     time.sleep(600)


#################################################################################################


site = "adb shell am start -n com.zhaopin.social/.SplashActivity"
position = ["运营总监", "产品总监", "客服"]
region_key = ["xiamen", "shanghai", "guangzhou", "shenzheng",
              "hangzhou"]  # "xiamen"+2,"shanghai"+0,"guangzhou"+0,"shenzheng"+0,"hangzhou"+1



def delivery(site, position, n):
    region_value = ["516 1616", "528 731", "510 908", "523 1104", "534 1696"]
    os.system(site)
    time.sleep(5)

    os.system("adb shell  input tap 430 160")  # 选择地区
    time.sleep(3)

    os.system("adb shell  input tap 99 130")  # 点击选择
    time.sleep(3)



    if region_key[n] == "shanghai" or region_key[n] == "guangzhou" or region_key[n] == "shenzheng":
        print("this is :" + region_key[n])
        os.system("adb shell  input tap " + region_value[n])
        time.sleep(3)




    elif region_key[n] == "hangzhou":
        print("this is :" + region_key[n])
        for a in range(1):
            os.system("adb shell input swipe 550 1740 550 750")  # 翻1页
            time.sleep(1)
        os.system("adb shell  input tap " + region_value[n])
        time.sleep(1)




    elif region_key[n] == "xiamen":
        print("this is: " + region_key[n])
        for a in range(2):
            os.system("adb shell input swipe 550 1740 550 750")  # 翻2页
            time.sleep(1)
        os.system("adb shell  input tap " + region_value[n])
        time.sleep(1)




    text = position  # 搜索
    os.system("adb shell am broadcast -a ADB_INPUT_TEXT --es msg '" + text + "'")
    os.system("adb shell input keyevent 66")



    os.system("adb shell  input tap 380 300")  # 筛选
    time.sleep(1)
    os.system("adb shell input swipe 105 735 675 695")
    time.sleep(1)
    os.system("adb shell  input tap 545 1536")




    os.system("adb shell  input tap 970 150")  # 批量投递
    x = 3
    for n in range(x):
        os.system("adb shell  input tap 90 1861")
        time.sleep(1)
        os.system("adb shell  input tap 860 1848")
        time.sleep(1)
        os.system("adb shell  input tap 90 1861")
        time.sleep(1)
        for n in range(12):
            os.system("adb shell input swipe 550 1740 550 290")
            time.sleep(1)
        time.sleep(2)

    os.system("adb shell am force-stop com.zhaopin.social")  # 关闭程序
    print("exe delivery Success:", position,region_key[n-1], site)




if __name__ == '__main__':
    delivery(site, position[0], 3)


