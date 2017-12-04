#!/usr/local/bin/python3
import requests
from bs4 import BeautifulSoup
import xlwt

thestep = 1
pagenum = 1
xlnum = 1
maxpage = 37934
divpage = 1000
data = [['姓名','身份证','手机','卡号']]
while thestep==1:
    if pagenum == maxpage:
        thestep = 2
        print("全部进程结束")
        break
    print("正在获取第"+str(pagenum)+"页数据...")
    response = requests.get('http://x.com/e/vip/user_vip.php?PageNum='+str(pagenum))
    soup = BeautifulSoup(response.text,"html.parser")
    trtext = soup.find_all('tr', align='center')

    for x in range(len(trtext)):
        trsoup = BeautifulSoup(str(trtext[x]),"html.parser")
        tdtext = trsoup.find_all('td')
        rowtext = [tdtext[1].text, tdtext[2].text, tdtext[3].text, tdtext[0].text]
        print(rowtext)
        data.append(rowtext)


    if (pagenum // divpage) == xlnum:

        xlnum += 1
        print("over,开始保存数据")
        workbook = xlwt.Workbook(encoding='utf-8')
        booksheet = workbook.add_sheet('Sheet 1', cell_overwrite_ok=True)

        for i, row in enumerate(data):
            for j, col in enumerate(row):
                booksheet.write(i, j, col)
        workbook.save('data'+str(xlnum)+'.xls')
        print(str(xlnum)+"号数据保存成功...")
        data = [['姓名', '身份证', '手机', '卡号']]
    pagenum += 1



