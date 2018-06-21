import requests

HOST = 'api.bitfinex.com/v1'
ENDPOINT_SYMBOL = '/symbols'
ENDPOINT_TICKER = '/pubticker/{}'


class ApiClient:
    def __init__(self):
        self.host = HOST

    def _request(self, method, endpoint, params=None, json=None):
        url = 'https://{}/{}'.format(self.host, endpoint)
        response = requests.request(method, url, params=params, json=json)
        return response

    def get(self, endpoint):
        return self._request('get', endpoint)

    def get_symbols(self):
        return self.get(ENDPOINT_SYMBOL)

    def get_ticker(self, symbol_name):
        return self.get(ENDPOINT_TICKER.format(symbol_name)).json()

    def get_last_price(self, symbol_name):
        return self.get_ticker(symbol_name).get('last_price')

    def get_low(self, symbol_name):
        return self.get_ticker(symbol_name).get('low')

    def get_high(self, symbol_name):
        return self.get_ticker(symbol_name).get('high')

    def get_volume(self, symbol_name):
        return self.get_ticker(symbol_name).get('volume')
