import requests
import bs4
import pandas as pd

list_project = []
list_address = []
list_area = []
list_price = []
list_investor = []
list_progress = []
crawled_price = []
crawled_address = []
crawled_area = []
crawled_projects = []
crawled_investor = []
crawled_progress = []
url_list = []

base_url = 'https://batdongsan.com.vn/can-ho-chung-cu-ha-noi/p'
for i in range (1,50):
    url = base_url + str(i)
    url_list.append(url)


for i in url_list:
    page = requests.get(i)
    soup = bs4.BeautifulSoup(page.text, "html.parser")



    area = soup.find_all('div', class_='area')
    for i in area:
        crawled_area.append(i)
    for i in crawled_area:
        i = str(i).replace('<div class="area">', '').replace('<span class="left">Diện tích: </span>', 'Diện tích: ').replace('</div>','').replace('\r', '').replace('\n', '')
        list_area.append(i)
    crawled_area.clear()



    add = soup.find_all('div', class_='add')
    for i in add:
        crawled_address.append(i)
    for i in crawled_address:
        i = str(i).replace('<div', '').replace(' class="add">', '').replace('</div>', '')
        list_address.append(i)
    crawled_address.clear()



    price = soup.find_all('div', class_='price')
    for i in price:
        crawled_price.append(i)
    for i in crawled_price:
        i = str(i).replace('<div class="price">\n<span class="left">','').replace('</span>\n<strong class="price">','').replace('</strong>\n</div>','').replace('</span>\n<span class="price">','').replace('</span>\n</div>','')
        list_price.append(i)
    crawled_price.clear()

    invest = soup.find_all('div',class_='investor')
    for i in invest:
        crawled_investor.append(i)
    for i in crawled_investor:
        i = str(i).replace('<div class="investor">\n<span class="left">','').replace('</span>\r\n','').replace('\r\n</div>','')
        list_investor.append(i)
    crawled_investor.clear()
    progress = soup.find_all('div',class_='prgrs')
    for i in progress:
        crawled_progress.append(i)
    for i in crawled_progress:
        i = str(i).replace('<div class="prgrs">\n<span class="left">','').replace('</span>\r\n','').replace('\r\n</div>','')
        list_progress.append(i)
    crawled_progress.clear()


    projects = soup.find_all('div', class_='thumb')
    for i in projects:
        title = i.find('a')
        for j in title:
            j.find('title')
            crawled_projects.append(j)
    for i in crawled_projects:
        i = str(i).replace('<img alt=','Tên dự án:').replace('src=',', Ảnh:').replace('/>','')
        list_project.append(i)
    list_project = list(dict.fromkeys(list_project))
    list_project.remove('\n')


bds = pd.DataFrame({'Tên dự án': list_project,
                    'Địa chỉ' : list_address,
                    'Diện tích': list_area,
                    'Giá bán': list_price,
                    'Chủ đầu tư' : list_investor,
                    'Tiến độ': list_progress})
df = pd.DataFrame(bds, columns=['Tên dự án','Địa chỉ','Diện tích','Giá bán','Chủ đầu tư','Tiến độ'])

df.to_csv(r'C:\Users\ngoma\Downloads\NhadatHaNoi.csv', index = False, header=True)








