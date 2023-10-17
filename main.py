import csv
import requests
from bs4 import BeautifulSoup


class TianLang:
    def __init__(self):
        self.head = ['导演','主演','类型','语言','年份','更新状态','更新日期']
        self.file = open('data.csv',mode='a',encoding='utf-8',newline='')
        self.writer = csv.writer(self.file)
        self.writer.writerow(self.head)

    def one_page(self,url):
        html = requests.get(url).text
        bf = BeautifulSoup(html)
        lis = bf.find_all('li', class_='li_r')
        sum0 = []
        for li in lis:
            li = li.text.strip('\xa0')
            sum0.append(li.replace('\xa0', ' '))
        self.writer.writerow(sum0)

    def max_page(self,num):
        for i in range(1, num):
            print(f'正在获取列表:{i}')
            url0 = f'http://tlyy.pw/list/1-{i}.html'
            html = requests.get(url0).text
            bf = BeautifulSoup(html)
            ids = bf.find_all('a', class_='item-link')
            for j in ids:
                id = j['href']
                url1 = f'http://tlyy.pw{id}'
                self.one_page(url1)
        else:
            self.file.close()

TianLang().max_page(1000)