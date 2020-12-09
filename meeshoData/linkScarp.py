from bs4 import BeautifulSoup as bs
from selenium import webdriver as wd
import json

url = "https://meesho.com"
driver = wd.Chrome()
driver.get(url)
Data_F = {}
def link_extract():
    data = bs(driver.page_source, "html.parser")

    span_d = data.find_all("span", attrs={'class': 'nav-head-item pointer nonHover'})

    nav_data = []
    for i in span_d:
        nav_data.append(i.text)
    for i in range(1, 10):
        span = "//body/div[@id='root']/div[1]/div[1]/div[2]/span[" + str(i) + "]"
        driver.find_element_by_xpath(span).click()
        data = bs(driver.page_source, "html.parser")
        sub = data.find_all("div", attrs={'class': 'nav-sub-list'})
        if i == 1:
            sub = sub[1:]
        Cat = {}

        for j in sub:
            sub_cat = {}
            a = j.find_all('a')
            for k in a:
                sc = k.text.replace(" ","_")
                sc = sc.replace("&","and")
                sub_cat[sc] = url + k.attrs['href']

            cat = j.find("div").text
            Cat[cat] = sub_cat
        Data_F[nav_data[i - 1]] = Cat

    with open("links.json", "w+") as f:
        json.dump(Data_F, f)

    f.close()

    driver.close()

#
# def data_extract():
#     for i in Data_F:
#         cat = {}
#         for j in Data_F[i]:
#             sub_cat = {}
#             for k in Data_F[i][j]:
#                 print(Data_F[i][j][k])
#                 link1 = Data_F[i][j][k]
#
#                 driver.get(link1)
#
#                 extract = []
#
#
#                 for l in range(1):
#                     time.sleep(1.5)
#                     soup = bs(driver.page_source, "html.parser")
#                     data = soup.find_all('a', attrs={'class': 'plp-card-desktop'})
#                     for m in data:
#                         img = m.find('img').attrs['src']
#                         name = m.find("h4").text
#                         price = m.find('div', attrs={'class': "actual-cost"}).text
#                         link = url + m.attrs["href"]
#                         extract.append([name, price, link, img])
#
#                     driver.find_element_by_xpath("//a[contains(text(),'Next')]").click()
#
#                 sub_cat[k] = extract
#             cat[j] = sub_cat
#         Data_F2[i] = cat
#
#         with open("products.txt", "w+") as f:
#             f.write(str(Data_F))
#
#         f.close()
#     return Data_F2
#

if __name__ == '__main__':
    link_extract()
    # DataF = data_extract()
    # with open("products.txt", "w+") as f:
    #     f.write(str(DataF))
    #
    # f.close()

