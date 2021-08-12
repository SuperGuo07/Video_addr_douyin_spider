from appium import webdriver

cap={
  "platformName": "Android",
  "platformVersion": "5.1.1",
  "deviceName": "127.0.0.1:62025",
  "appPackage": "com.ss.android.ugc.aweme",
  "appActivity": "com.ss.android.ugc.aweme.main.MainActivity",
  "noReset": True,
  "unicodekeyboard": True,
  "resetkeyboard": True
}

server='http://localhost:4723/wd/hub'
print("*"*50,"正在打开抖音","*"*50)
driver = webdriver.Remote(server,cap)
def get_size():
    x=driver.get_window_size()["width"]
    y=driver.get_window_size()["height"]
    return(x,y)

l=get_size()

home_huadong=input("是否进行滑动：")

while home_huadong == "1":
    if "没有更多了" in driver.page_source:
            break
    else:
        driver.swipe(int(l[0]*0.5),int(l[1]*0.9),int(l[0]*0.5),int(l[1]*0.25))