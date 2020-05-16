import urllib.request as request
import bs4
import time

pet_list = [] # 將爬到的資料存進這
i = 1 # 設定頁面變數
while i <= 9:  # 爬到第9頁 停止
    # 放網頁 後面"+str(i)+" 為頁面變數
    url = "https://www.chanchao.com.tw/petsshow/taipei/visitorProduct.asp?page="+str(i)+"&cat=&view=list"
    # 使用request Mod 加入使用者信息
    req = request.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        })
    # 使用request Mod 網路連線
    with request.urlopen(req) as response: 
        # 使用response讀取, 並解碼, 存進data
        data = response.read().decode("utf-8")
        # 使用BeautifulSoup解析html格式
    root = bs4.BeautifulSoup(data, "html.parser")
        # 用BeautifulSoup Mod的find功能, 篩選div標籤及屬性名稱
    titles = root.find_all("div", class_="right")
        # 使用for loop將篩選的資料一條一條讀取
    for line in titles:
        if line.h4 != None: # 要是資料有h4
            time.sleep(3) # time Mod的sleep功能
            # 將h4標籤裡的字串, 加進pet_list
            pet_list.append(line.h4.string)
    i += 1  # 換頁
    time.sleep(5) # 停滯5秒

    # 寫入pet.txt
with open("pet.txt", "w", encoding="utf-8") as f:
    for line in pet_list:
        f.write(line + "\n")
        print(line)
