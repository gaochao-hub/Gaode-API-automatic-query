import time
from selenium import webdriver
import csv
from selenium.webdriver.common.keys import Keys
text = []
filename = "C:/Users/PC/Desktop/data.csv"
with open(filename) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    for row in reader:
        text.append(row[1])
    f.close()
print(time.ctime())
driver1 = webdriver.Edge()
driver2 = webdriver.Edge()
driver1.get("https://developer.amap.com/tools/picker")
for i in range(100):
    search_text = "兰州市" + text[i]
    driver1.find_element_by_id("txtSearch").clear()
    driver1.find_element_by_id("txtSearch").send_keys(search_text)
    driver1.find_element_by_link_text("搜索").click()
    if driver1.find_element_by_class_name('message').text == '':
        driver1.find_element_by_link_text("复制").click()
        driver2.get("http://127.0.0.1:8000/")
        copy1 = driver2.find_element_by_name("name")
        copy2 = driver2.find_element_by_name("coordinate")
        copy3 = driver2.find_element_by_name('number')
        copy1.send_keys(text[i])
        copy2.send_keys(Keys.CONTROL, 'v')
        copy3.send_keys(i + 2)
        driver2.find_element_by_name("submit").click()
print(time.ctime())
