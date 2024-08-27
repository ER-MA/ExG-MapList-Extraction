import os
import re
import csv
from datetime import datetime

import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def get_map_list_from_exg_map_ordering():
    # 读取: ./maps_html_from_exg_menu.txt
    # 写入: ./ExG_ZE_MapList_{timestamp}.csv

    # 读取项目根目录下的TXT文件
    txt_file_path = "input/maps_html_from_exg_menu.txt"
    with open(txt_file_path, "r", encoding="utf-8") as file:
        data = file.read()

    # 使用正则表达式提取option中的value值，并替换英文名和中文别名之间的空格
    matches = re.findall(r'value="([^"]+)"', data)
    processed_data = [re.sub(r'([^ ]+) ([^"]+)', r'\1,\2', match) for match in matches]

    # 准备写入CSV文件的数据
    csv_data = "\n".join(processed_data)

    # 确保output目录存在，如果不存在则创建它
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 将数据写入CSV文件，文件名加上时间戳，并确保输出到output目录
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    csv_file_path = os.path.join(output_dir, f"ExG_ZE_MapList_{timestamp}.csv")
    with open(csv_file_path, "w", encoding="utf-8-sig") as file:
        file.write(csv_data)


def get_map_list_from_exg_map_list():
    # 读取: https://list.darkrp.cn:9000/ServerList/Cs2MapList
    # 写入: ./ExG_MapList_{timestamp}.csv

    # 设置Selenium选项
    options = Options()
    options.headless = True  # 无头模式
    options.add_argument("--window-size=1920,1080")

    # 初始化webdriver
    service = Service('./chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=options)

    # 打开网页
    url = 'https://list.darkrp.cn:9000/ServerList/Cs2MapList'
    driver.get(url)

    # 等待JavaScript加载完毕
    driver.implicitly_wait(10)

    # 获取表格数据
    table = driver.find_element(By.ID, 'data-tablebody')
    rows = table.find_elements(By.TAG_NAME, 'tr')

    data = []
    for row in rows:
        cols = row.find_elements(By.TAG_NAME, 'td')
        cols = [col.text.strip() for col in cols]
        workshop_link = cols[-1]
        workshop_id = workshop_link.split('=')[-1] if '=' in workshop_link else workshop_link
        cols[-1] = workshop_id
        data.append(cols)

    # 关闭浏览器
    driver.quit()

    if not data:
        print("没有找到任何数据")
        return

    # 确保output目录存在，如果不存在则创建它
    output_dir = 'output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 写入CSV文件
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    filename = f'ExG_MapList_{timestamp}.csv'
    csv_file_path = os.path.join(output_dir, filename)
    with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['地图名', '中文名', '难度', '冷却时长', '冷却截止', 'Workshop'])
        writer.writerows(data)

