import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
cookies = {
    'bcookie': "v=2&3ee66614-8fc6-4c37-86cf-a607c45c8824",
    'scookie': "v=1&20210813140039f7de7e54-7f64-4dd6-8cce-8bdd7cd60348AQFRwXR9vBfXOe23s5s90v0_NhXXXx3s",
    'fid': 'AQFU0si7k4iEEgAAAXs_0JeIC_olw23Hmv5nEYEmMR8OLEdXzbjviK4AIOr6t44j62fzL5rgMEZ7tw',
    '_ga': 'GA1.2.447553955.1628863243', '_gid': 'GA1.2.1083926558.1628863243',
    'fcookie': 'AQHlVcXCBOPGxwAAAXs_0Mu1EwiE6fpCSWXdNo8ARW7dPaY0zFc8M41M31kfJSq1_ccrgw2HROQyU8nPHKNM9ejmvzReuf-kgZ59HPr8VUgJrjJUV6qWTa-ABTm6EYseH0-kjq3JKpCKnutQEVBRZIZU7l3w-JxmifhjGRiWqPZsVs0pYrZIgy1ingS0gA0QXPBSf1WZiK8Y_vYHTm-rOUMuKChvvhbAOw-xOdoHeuFnv8q0Gu-D6ZTNkYM97iLQgjGoHptsSX1dm9iYIESuGWp2KC2QzYf1RB9wDwAUEbhPFKTeiwfbk+rIsGBqwqOyX1iUqMabFf7JBna2uyT5eHrfgMsv1gSbo72x3zl7mwzT6Xdhz3aHmg==',
    'li_at': 'AQEDASgqyXEBrmMCAAABez_QzFwAAAF7Y91QXFYAUj_fpmnrKg_3jStuRYT-0rrZqPbda9uMIH_kmYFv7awra3_LVu3vp9UvIR5_rg7dKD3Uab0jA0OnIEv09al7dHKHcdEbMyOAT9wQ0Kcsym9MK24c',
    'liap': 'true',
    'JSESSIONID': "ajax:1164707066053231545",
    'lidc': "b=OB21:s=O:r=O:a=O:p=O:g=3510:u=332:x=1:i=1628863254:t=1628872368:v=2:sig=AQHGsIeUuWvTzXAawD2Kh8rmrtdROiAZ",
    'timezone': 'Etc/GMT-8',
    'lang': 'v=2&lang=en-us',
    'spectroscopyId': '29e99ede-d1a6-467d-b04a-9e9412aef7e9'
}
url = 'https://www.linkedin.com/in/shaoxiong-steven-y-269828169/'
response = requests.get(url=url, headers=headers, cookies=cookies)
print(response.text)
