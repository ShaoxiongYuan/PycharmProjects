import requests
import base64

AK = 'T9jGu6eahnAawqPRSDz1Eg5A'
SK = 'cUBpSBVrrsl3hGX9DFYeaGBhaw8inolY'

host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + AK + '&client_secret=' + SK
df = requests.get(host).json()
token = df['access_token']


def get_pig(file_in, file_on):
    request_url = 'https://aip.baidubce.com/rest/2.0/image-process/v1/selfie_anime'
    with open(file_in, 'rb') as f:
        img = base64.b64encode(f.read())
    params = {'image': img}
    headers = {'User-Agent':'Mozilla/5.0'}
    response = requests.post(request_url + '?access_token=' + token, data=params, headers=headers).json()
    img = response['image']
    imgdata = base64.b64decode(img)
    with open(file_on, 'wb') as f:
        f.write(imgdata)


file_in = '2.jpg'
file_on = 'second.jpg'
get_pig(file_in, file_on)
