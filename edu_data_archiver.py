
import os
import requests
from bs4 import BeautifulSoup

# 请求网页内容
url = 'https://www.get-information-schools.service.gov.uk/Groups/Group/Details/3320#list'
response = requests.get(url)
html = response.text

# 解析HTML
soup = BeautifulSoup(html, 'html.parser')

# 提取<h2>标签内容
h2_tags = soup.find_all('h2', class_='govuk-heading-s')

# 指定D盘桌面路径
desktop_path = r'D:\Desktop\Website\Academics from web'

# 打开一个文件以保存提取的数据
with open(os.path.join(desktop_path, 'extracted_data.txt'), 'w', encoding='utf-8') as file:
    count = 1
    # 遍历所有<h2>标签
    for h2 in h2_tags:
        # 提取<a>标签内容
        a_tags = h2.find_all('a')
        for a in a_tags:
            # 获取a标签的href属性和文本内容
            href = a.get('href')
            code = href.split('/')[-1] #分割字符串并取最后一部分
            text = a.text
            # 在控制台打印提取的数据
            print(f'{count}: {text}, Code: {code}')
            # 将提取的内容写入文件
            file.write(f'{count}: {text}, {code}\n')
            count += 1

# 提示：文件已保存
print(f'save success')
