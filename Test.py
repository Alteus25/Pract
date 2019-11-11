import requests
from bs4 import BeautifulSoup as bs
import csv

def get_html(url):
    r = requests.get(url)
    return r.text

def get_total_pages(html):
    soup = bs(html, 'html.parser')
    pages = soup.find('ul', class_='pager').find_all('a')[-1].get('href')
    total_pages = pages.split('=')[1]

    return int(total_pages)

def get_page_data(html):
    soup = bs(html, 'html.parser')
    divs = soup.find_all('h3')
    for div in divs:
        company_name = div.find('a').text
        company_prelink = div.find('a').get('href')

        company_link = 'https://connect.supplysideshow.com' + company_prelink
        print(company_name)
        print(company_link)


def write_csv(data):
    with open('D:\workspace\practise\Education\fhparser.csv'):

def main():
    url = 'https://connect.supplysideshow.com/search/exhibitors?page=0'
    base_url = 'https://connect.supplysideshow.com/search/exhibitors?page='
    total_pages = get_total_pages(get_html(url))

    for i in range(0, total_pages):
        url_gen = base_url + str(i)
        html = get_html(url_gen)
        get_page_data(html)



if __name__ == '__main__':
    main()





#count = 0
#
# while True:
#     base_url = 'https://connect.supplysideshow.com/search/exhibitors?page=' + str(count)
#     r = requests.get(base_url).text
#
#     soup = bs(r, "html.parser")
#     divs = soup.find_all('h3')
#
#     for div in divs:
#         company_name = div.find('a').text
#         company_link = div.find('a').get('href')
#         global_company_link = 'https://connect.supplysideshow.com' + company_link
#
#     print("Page number" + str(count))
#     count += 1
#     print(company_name)
#     print(global_company_link)