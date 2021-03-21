import requests
import pyautogui
import re
import time
import pyperclip
import json
#离线下载 650 95
#输入框 839 482
#开始下载 1164 641
#后台下载 1185 690
#取样点 1127 637
proxy={
'http':'127.0.0.1:10809',
'https':'127.0.0.1:10809'
}
cookie_str="__cfduid=dc8cef069fd08bc183e2917ed9b54646f1616307611; darkmode=false; __cf_bm=81ca7052dd2d98beb16909dfa7ab52c5eed5f8f7-1616343185-1800-AT6UJ7nk0bXmnRz61aekvdVNrc74xuLsPgX8QCui9+gp7SXWoTIBDgsGCXLE+K+PxRZ1gFn7HJl8a6O/b2HaIBS1XcPOECKW7i6r8Sq6lIt0YguL/uHrpEP+TTrSFJeRyw=="
def make_cookie(cookie_str):
    cookie_json={}
    cookies=cookie_str.split(";")
    for cookie in cookies:
        c=cookie.split("=")
        cookie_json[c[0]]=c[1]
    return cookie_json
cookie=make_cookie(cookie_str)
json_data={
    "pagenum":1
}
page_header={
    "authority": "sj-ghs.club",
    "method": "GET",
    "path": "/2020/1106/getchu/",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://sj-ghs.club/2020/1106/",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36"
}
down_header={
    "authority": "sj-ghs.club",
    "method": "GET",
    "path": "/2020/1000/booth/booth/(SWDPN0005)%201148959.7z",
    "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer":"https://sj-ghs.club/2020/1000/booth/booth/",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "same-origin",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}   
def click_down():
    pyautogui.moveTo(1164,641,duration=1,tween=pyautogui.linear)
    pyautogui.click(x=1164,y=641,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
    time.sleep(10)
    im=pyautogui.screenshot()
    pixel=im.getpixel((1127,637))
    if pixel==(4,126,192) or pixel==(6,168,255):
        click_down() 
    else:
        return
def get_txt():
    url="https://sj-ghs.club/2021/0120/getchu/"
    #url="https://dl.smileacg.com/CN3/sf19/"
    #main_page=requests.get(url,cookies=cookie)
    main_page=requests.get(url,cookies=cookie,headers=page_header,proxies=proxy)
    rc=re.compile(r'/\d+/[a-z\;\&]+/.*?\.[7ztx]+\.?\d*')
    #rc=re.compile(r'[^<>"]+?.7z')
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
def get_link():
    f=open("./1.txt")
    for line in f.readlines():
        down_url=line.strip("\n")
        page=requests.get("https://sj-ghs.club/2021"+down_url,cookies=cookie,allow_redirects=False,proxies=proxy)
        t_down_url=page.next.url
        f=open("./2.txt","a")
        f.write(t_down_url+"\n")
        print(line)
def downfromtxt():
    i=0
    f=open("./1.txt","r")
    down_urls=[]
    for line in f.readlines():
        down_urls.append(line.strip("\n"))
    while(True):
        try:
            if(i>=len(down_urls)):
                break
            down_url=down_urls[i]
            down_url=down_url.strip("\n")
            page=requests.get("https://sj-ghs.club/2021"+down_url,cookies=cookie,headers=down_header,allow_redirects=False)
            #page=requests.get("https://dl.smileacg.com/"+down_url,cookies=cookie,allow_redirects=False)
            t_down_url=page.next.url
            pyperclip.copy(t_down_url)
            page.close()
            pyautogui.moveTo(625,70,duration=1,tween=pyautogui.linear)
            pyautogui.click(x=625, y=70, clicks=1, interval=0.01, button='left', duration=0.1, tween=pyautogui.linear) 
            pyautogui.moveTo(839,482,duration=1,tween=pyautogui.linear)
            pyautogui.click(x=839,y=482,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
            #pyautogui.moveTo(800,400,duration=1,tween=pyautogui.linear)
            #pyautogui.typewrite(message=t_down_url,interval=0.001)
            pyautogui.hotkey('ctrl', 'v')

            click_down()
            time.sleep(5)

            pyautogui.moveTo(1185,690,duration=1,tween=pyautogui.linear)
            pyautogui.click(x=1185,y=690,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
            i=i+1
        except:
            continue
"""
    for down_url in down_urls:
        down_url=down_url.strip("\n")
        page=requests.get("https://sj-ghs.club/2021"+down_url,cookies=cookie,headers=down_header,allow_redirects=False)
        #page=requests.get("https://dl.smileacg.com/"+down_url,cookies=cookie,allow_redirects=False)
        t_down_url=page.next.url
        pyperclip.copy(t_down_url)
        page.close()
        pyautogui.moveTo(625,70,duration=1,tween=pyautogui.linear)
        pyautogui.click(x=625, y=70, clicks=1, interval=0.01, button='left', duration=0.1, tween=pyautogui.linear) 
        pyautogui.moveTo(839,482,duration=1,tween=pyautogui.linear)
        pyautogui.click(x=839,y=482,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
        #pyautogui.moveTo(800,400,duration=1,tween=pyautogui.linear)
        #pyautogui.typewrite(message=t_down_url,interval=0.001)
        pyautogui.hotkey('ctrl', 'v')

        click_down()
        time.sleep(5)

        pyautogui.moveTo(1185,690,duration=1,tween=pyautogui.linear)
        pyautogui.click(x=1185,y=690,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
"""
def downfromlink():
    f=open("./2.txt")
    for line in f.readlines():
        down_url=line.strip("\n")
        pyperclip.copy(down_url)
        pyautogui.moveTo(650,95,duration=1,tween=pyautogui.linear)
        pyautogui.click(x=650, y=95, clicks=1, interval=0.01, button='left', duration=0.1, tween=pyautogui.linear) 
        pyautogui.moveTo(839,482,duration=1,tween=pyautogui.linear)
        pyautogui.click(x=839,y=482,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
        pyautogui.hotkey('ctrl', 'v')

        click_down()
        time.sleep(5)

        pyautogui.moveTo(1185,690,duration=1,tween=pyautogui.linear)
        pyautogui.click(x=1185,y=690,clicks=1,interval=0,button='left',duration=0.1,tween=pyautogui.linear)
downfromtxt()