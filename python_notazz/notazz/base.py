import requests


class NotazzException(Exception):
    pass


class NotazzBase(object):

    api_key = None

    PRD_URI = 'https://app.notazz.com/api/{0}'

    @property
    def base_uri(self):
        return NotazzBase.PRD_URI

    def __init__(self, api_key):
        self.api_key = api_key

    @staticmethod
    def load_testing_env_variables():
        import os
        from notazz.environment import environment
        for key, value in environment:
            try:
                os.environ.setdefault(key, value)
            except:
                print('Error on key', key)

    def process_errors(self, response):
        """
        :param response:
        :return:
        """
        if response.status_code == 400:
            r = response.json()
            if 'errors' in r:
                for e in r['errors']:
                    raise NotazzException('{code} - {desc}'.format(
                        code=e['code'],
                        desc=e['description'],
                    ))
        elif response.status_code == 401:
            raise NotazzException('Auth Error: 401 - API key missing')
        elif response.status_code == 404:
            raise NotazzException('Programming error: 404 - URI not found')
        elif response.status_code == 500:
            raise NotazzException('500 -Something wrong with ASAAS Server')

    def do_get_request(self, url, params=None):
        headers = {
            'content-type': 'application/json',
            'access_token': self.api_key,
        }
        params = params if params else {}
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            self.process_errors(response)
        else:
            return response

    def do_post_request(self, url, params=None):
        headers = {
            'content-type': 'application/json',
            'access_token': self.api_key,
        }
        params = params if params else {}
        response = requests.post(url, json=params, headers=headers)
        if response.status_code != 200:
            self.process_errors(response)
            return response
        else:
            return response

    def do_put_request(self, url, params=None):
        headers = {
            'content-type': 'application/json',
            'access_token': self.api_key,
        }
        params = params if params else {}
        response = requests.put(url, json=params, headers=headers)
        if response.status_code != 200:
            self.process_errors(response)
        else:
            return response

    def do_delete_request(self, url, params=None):
        headers = {
            'content-type': 'application/json',
            'access_token': self.api_key,
        }
        params = params if params else {}
        response = requests.delete(url, data=params, headers=headers)
        if response.status_code != 200:
            self.process_errors(response)
        else:
            return response
