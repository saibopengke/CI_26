import os
import time
import unittest
import configparser

import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@allure.feature("UI自动化测试")
class Selenium(unittest.TestCase):

    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))
        return config

    def setUp(self) -> None:
        config = self.get_config()
        try:
            using_headless = os.environ['using_headless']
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')
        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")
            # 读取配置文件
        self.driver = webdriver.Chrome(executable_path=config.get('driver', "chrome_driver"),
                                       options=chrome_options)

    def tearDown(self) -> None:
        self.driver.quit()

    @allure.story('-------测试今日头条-------')
    def test_webui_1(self):
        self._test_baidu("今日头条", 'test_webui_1')

    @allure.story('-------王者荣耀-------')
    def test_webui_2(self):
        self._test_baidu("王者荣耀", 'test_webui_2')

    def _test_baidu(self, search_keyword, testcase_name):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element(By.ID, "kw").send_keys(f'{search_keyword}{Keys.RETURN}')
        time.sleep(5)
        self.assertTrue(f'{search_keyword}' in self.driver.title,
                        msg=f'{testcase_name} pass')
