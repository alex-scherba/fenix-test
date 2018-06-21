import unittest
from hamcrest import *
from utils.api_client import ApiClient

SYMBOLS_LIST = ["btcusd", "ltcusd", "ltcbtc", "ethusd", "ethbtc", "etcbtc", "etcusd", "rrtusd",
                "rrtbtc", "zecusd", "zecbtc", "xmrusd", "xmrbtc", "dshusd", "dshbtc", "btceur",
                "btcjpy", "xrpusd", "xrpbtc", "iotusd", "iotbtc", "ioteth", "eosusd", "eosbtc",
                "eoseth", "sanusd", "sanbtc", "saneth", "omgusd", "omgbtc", "omgeth", "bchusd",
                "bchbtc", "bcheth", "neousd", "neobtc", "neoeth", "etpusd", "etpbtc", "etpeth",
                "qtmusd", "qtmbtc", "qtmeth", "avtusd", "avtbtc", "avteth", "edousd", "edobtc",
                "edoeth", "btgusd", "btgbtc", "datusd", "datbtc", "dateth", "qshusd", "qshbtc",
                "qsheth", "yywusd", "yywbtc", "yyweth", "gntusd", "gntbtc", "gnteth", "sntusd",
                "sntbtc", "snteth", "ioteur", "batusd", "batbtc", "bateth", "mnausd", "mnabtc",
                "mnaeth", "funusd", "funbtc", "funeth", "zrxusd", "zrxbtc", "zrxeth", "tnbusd",
                "tnbbtc", "tnbeth", "spkusd", "spkbtc", "spketh", "trxusd", "trxbtc", "trxeth",
                "rcnusd", "rcnbtc", "rcneth", "rlcusd", "rlcbtc", "rlceth", "aidusd", "aidbtc",
                "aideth", "sngusd", "sngbtc", "sngeth", "repusd", "repbtc", "repeth", "elfusd",
                "elfbtc", "elfeth", "btcgbp", "etheur", "ethjpy", "ethgbp", "neoeur", "neojpy",
                "neogbp", "eoseur", "eosjpy", "eosgbp", "iotjpy", "iotgbp", "iosusd", "iosbtc",
                "ioseth", "aiousd", "aiobtc", "aioeth", "requsd", "reqbtc", "reqeth", "rdnusd",
                "rdnbtc", "rdneth", "lrcusd", "lrcbtc", "lrceth", "waxusd", "waxbtc", "waxeth",
                "daiusd", "daibtc", "daieth", "cfiusd", "cfibtc", "cfieth", "agiusd", "agibtc",
                "agieth", "bftusd", "bftbtc", "bfteth", "mtnusd", "mtnbtc", "mtneth", "odeusd",
                "odebtc", "odeeth", "antusd", "antbtc", "anteth", "dthusd", "dthbtc", "dtheth",
                "mitusd", "mitbtc", "miteth", "stjusd", "stjbtc", "stjeth", "xlmusd", "xlmeur",
                "xlmjpy", "xlmgbp", "xlmbtc", "xlmeth", "xvgusd", "xvgeur", "xvgjpy", "xvggbp",
                "xvgbtc", "xvgeth", "bciusd", "bcibtc", "mkrusd", "mkrbtc", "mkreth", "venusd",
                "venbtc", "veneth", "kncusd", "kncbtc", "knceth", "poausd", "poabtc", "poaeth",
                "lymusd", "lymbtc", "lymeth", "utkusd", "utkbtc", "utketh", "veeusd", "veebtc",
                "veeeth", "dadusd", "dadbtc", "dadeth", "orsusd", "orsbtc", "orseth", "aucusd",
                "aucbtc", "auceth", "poyusd", "poybtc", "poyeth", "fsnusd", "fsnbtc", "fsneth",
                "cbtusd", "cbtbtc", "cbteth"]
HEADERS_LIST = ['Date', 'Content-Type', 'Transfer-Encoding', 'Connection', 'Set-Cookie', 'Vary', 'X-Frame-Options',
                'X-XSS-Protection', 'X-Content-Type-Options', 'ETag', 'Cache-Control', 'X-Request-Id', 'X-Runtime',
                'Strict-Transport-Security', 'Content-Encoding', 'Expect-CT', 'Server', 'CF-RAY']
RATE_LIMIT_MESSAGE = 'ERR_RATE_LIMIT'


class TestSymbols(unittest.TestCase):

    def setUp(self):
        self.api_client = ApiClient()

    def test_list_symbols_status_code(self):
        assert_that(self.api_client.get_symbols().status_code, equal_to(200))

    def test_list_symbols_content(self):
        assert_that(self.api_client.get_symbols().json(), equal_to(SYMBOLS_LIST))

    def test_list_symbols_headers(self):
        headers = [key for key in self.api_client.get_symbols().headers]
        assert_that(headers, equal_to(HEADERS_LIST))

    def test_rate_limit_status_code(self):
        [self.api_client.get_symbols() for _ in range(5)]
        assert_that(self.api_client.get_symbols().status_code, equal_to(429))

    def test_rate_limit_message_body(self):
        [self.api_client.get_symbols() for _ in range(5)]
        assert_that(self.api_client.get_symbols().json().get('error'), equal_to(RATE_LIMIT_MESSAGE))


if __name__ == '__main__':
    unittest.main()
