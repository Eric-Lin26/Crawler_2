import urllib.request as request
import bs4
import time

pet_list = []
i = 1
while i <= 9:
    url = "https://www.chanchao.com.tw/petsshow/taipei/visitorProduct.asp?page="+str(i)+"&cat=&view=list"
    req = request.Request(url, headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
        })
    with request.urlopen(req) as response: 
        data = response.read().decode("utf-8")

    root = bs4.BeautifulSoup(data, "html.parser")
    titles = root.find_all("div", class_="right")

    for line in titles:
        if line.h4 != None:
            time.sleep(3)
            pet_list.append(line.h4.string)
    i += 1
    time.sleep(5)

with open("pet.txt", "w", encoding="utf-8") as f:
    for line in pet_list:
        f.write(line + "\n")
        print(line)
