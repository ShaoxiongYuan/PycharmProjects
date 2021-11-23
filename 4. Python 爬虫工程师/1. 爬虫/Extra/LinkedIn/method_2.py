import requests

PROXYCURL_API_KEY = '8dea9ba4-0b73-423e-940f-cdf14a06900d'


def get_profile(profile_id):
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
    header_dic = {'Authorization': 'Bearer ' + PROXYCURL_API_KEY}
    params = {
        'url': f'https://www.linkedin.com/in/{profile_id}',
    }
    response = requests.get(api_endpoint,
                            params=params,
                            headers=header_dic)
    return response.json()


profile = get_profile('steven-goh-6738131b')
print(profile['full_name'])
print(profile['country_full_name'])
