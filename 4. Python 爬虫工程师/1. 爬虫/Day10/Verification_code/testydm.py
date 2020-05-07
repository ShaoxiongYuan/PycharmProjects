from ydmapi import get_result
import os

for root, dirs, filenames in os.walk('./Captcha'):
    for filename in filenames:
        result = get_result('./Captcha/' + filename)
        print(result)
