from bs4 import BeautifulSoup
import requests
import re
import sys


def catchurl(url_input):
    dept_list = []
    req = requests.get(url=url_input)
    html = req.text
    bf = BeautifulSoup(html, features='lxml')
    courses = bf.find_all('a', href=True)
    for course in courses:
        id_pattern = re.compile(r'<a href="https://classes.usc.edu/term-20213/classes/(.*?)/">', re.S)
        class_id = id_pattern.findall(str(course))
        if len(class_id) != 0:
            dept_list.append(class_id)
    dept_list = [str(x) for x in dept_list]
    return dept_list


if __name__ == "__main__":
    # target = input("input URL: ")
    i = 0
    dept_list = catchurl('https://classes.usc.edu/term-20213/')
    while (i < len(dept_list)):
        target = 'https://classes.usc.edu/term-20213/classes/' + str(dept_list[i])[2:-2] + '/'
        print(target)
        req = requests.get(url=target)
        html = req.text
        bf = BeautifulSoup(html, features='lxml')
        courses = bf.find_all('div', class_='course-info')
        for course in courses:
            id_pattern = re.compile(r'<div class="course-info.*?id="(.*?)"><', re.S)
            class_id = id_pattern.findall(str(course))[0]
            sys.stdout.write(class_id)
            name_pattern = re.compile(r'</strong>(.*?)<span class="units">', re.S)
            name = name_pattern.findall(str(course))[0]
            print(name)
            section_pattern = re.compile(r'<td class="section">(.*?)</td>', re.S)
            sections = section_pattern.findall(str(course))
            # print(sections)
            for section in sections:
                print(section)
        i += 1
