import requests
import pyautogui
import re
import time
#离线下载 650 95
#输入框 839 482
#开始下载 1164 641
#后台下载 1185 690
#url="https://sj-ghs.club/0330/fanita/"
#main_page=requests.get(url)
#rc=re.compile(r'/\d+/[a-z]+/.*?\.[7ztx]+\.?\d*')
#
#items=rc.findall(main_page.text)
#main_page.close()
#down_urls=[]
#for item in items:
#    if not item in down_urls:
#        down_urls.append(item)
#f=open("./1.txt","a")
#for down_url in down_urls:
#    f.write(down_url+"\n")
#f.close()


down_urls=[]
f=open("./1.txt","r")
for line in f.readlines():
    down_urls.append(line.strip("\n"))
for down_url in down_urls:
    down_url=down_url.strip("\n")
    page=requests.get("https://sj-ghs.club"+down_url,allow_redirects=False)
    t_down_url=page.next.url
    page.close()
    #print(t_down_url)
    pyautogui.moveTo(650,95,duration=1,tween=pyautogui.linear)
    pyautogui.click(x=650, y=95, clicks=1, interval=0.0, button='left', duration=0.1, tween=pyautogui.linear)
    time.sleep(2)
    
    pyautogui.moveTo(839,482,duration=1,tween=pyautogui.linear)
    pyautogui.click(x=839,y=482,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
    pyautogui.moveTo(800,400,duration=1,tween=pyautogui.linear)
    time.sleep(2)
    pyautogui.typewrite(message=t_down_url,interval=0.005)
    time.sleep(2)
    pyautogui.moveTo(1164,641,duration=1,tween=pyautogui.linear)
    pyautogui.click(x=1164,y=641,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
    time.sleep(10)
    pyautogui.moveTo(1185,690,duration=1,tween=pyautogui.linear)
    pyautogui.click(x=1185,y=690,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
    time.sleep(1)
