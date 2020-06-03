import requests
import pyautogui
import re
import time
#离线下载 650 95
#输入框 839 482
#开始下载 1164 641
#后台下载 1185 690
#取样点 1127 637
cookie={
        "password":"4ed0f94daf0571f89baf9d2ed5e6a37c"
}
    
def click_down():
    pyautogui.moveTo(1164,641,duration=1,tween=pyautogui.linear)
    pyautogui.click(x=1164,y=641,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
    im=pyautogui.screenshot()
    pixel=im.getpixel((1127,637))
    print(pixel)
    time.sleep(10)
    if pixel==(4,126,192):
        click_down() 
    else:
        return
def get_txt():
    url="https://sj-ghs.club/0511/booth/"
    main_page=requests.get(url,cookies=cookie)
    rc=re.compile(r'/\d+/[a-z]+/.*?\.[7ztx]+\.?\d*')
    items=rc.findall(main_page.text)
    main_page.close()
    down_urls=[]
    for item in items:
        if not item in down_urls:
            down_urls.append(item)
    f=open("./1.txt","a")
    for down_url in down_urls:
        f.write(down_url+"\n")
    f.close()



#get_txt()
down_urls=[]
f=open("./1.txt","r")
for line in f.readlines():
    down_urls.append(line.strip("\n"))
for down_url in down_urls:
    down_url=down_url.strip("\n")
    page=requests.get("https://sj-ghs.club"+down_url,cookies=cookie,allow_redirects=False)
    t_down_url=page.next.url
    page.close()
    pyautogui.moveTo(650,95,duration=1,tween=pyautogui.linear)
    pyautogui.click(x=650, y=95, clicks=1, interval=0.0, button='left', duration=0.1, tween=pyautogui.linear) 
    pyautogui.moveTo(839,482,duration=1,tween=pyautogui.linear)
    pyautogui.click(x=839,y=482,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
    pyautogui.moveTo(800,400,duration=1,tween=pyautogui.linear)
    pyautogui.typewrite(message=t_down_url,interval=0.05)

    click_down()
    time.sleep(5)

    pyautogui.moveTo(1185,690,duration=1,tween=pyautogui.linear)
    pyautogui.click(x=1185,y=690,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
