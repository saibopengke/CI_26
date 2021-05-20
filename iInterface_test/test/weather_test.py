import unittest

import allure

from iInterface_test.library.httpclient import HttpClient


@allure.feature("测试 Weather APi")
class Weather(unittest.TestCase):
    def setUp(self) -> None:
        self.host = "http://www.weather.com.cn"
        self.path = "/data/cityinfo"
        self.client = HttpClient()

    @allure.story("测试深圳")
    def test_1(self):
        city_code = "101280601"
        exp_city = "深圳"
        self._test(city_code, exp_city)

    @allure.story("测试北京")
    def test_2(self):
        city_code = '101010100'
        exp_city = '北京'
        self._test(city_code, exp_city)

    def _test(self, city_code, exp_city):
        url = f"{self.host}{self.path}/{city_code}.html"
        response = self.client.Get(url=url)
        act_city = response.json()["weatherinfo"]["city"]
        self.assertEqual(exp_city, act_city, f"Expect city={exp_city}, Actual city={act_city}")
