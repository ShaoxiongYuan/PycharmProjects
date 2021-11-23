from bs4 import BeautifulSoup
import requests
import re

if __name__ == "__main__":
    # target = input("input URL: ")
    target = 'https://classes.usc.edu/term-20213/classes/ali/'
    req = requests.get(url=target)
    html = req.text
    bf = BeautifulSoup(html, features='lxml')
    courses = bf.find_all('div', class_='course-info')
    for course in courses:
        id_pattern = re.compile(r'<div class="course-info.*?id="(.*?)"><', re.S)
        class_id = id_pattern.findall(str(course))[0]
        print(class_id)
        section_pattern = re.compile(r'<td class="section">(.*?)</td>', re.S)
        sections = section_pattern.findall(str(course))
        print(sections)
        print('*' * 50)
