import os
import time
import unittest

from appium import webdriver
from pytest_testconfig import config
from selenium.webdriver.common.by import By


class IAppium(unittest.TestCase):
    def setUp(self) -> None:
        desired_caps = {}
        # appium_server_url = config['appium_server_url']
        appium_server_url = config['appium_server_url']
        desired_caps['platformName'] = config['desired_caps']['platformName']
        desired_caps['udid'] = config['desired_caps']['udid']
        desired_caps['deviceName'] = config['desired_caps']['deviceName']
        desired_caps['appPackage'] = config['desired_caps']['appPackage']
        desired_caps['appActivity'] = config['desired_caps']['appActivity']
        desired_caps['automationName'] = config['desired_caps']['automationName']
        desired_caps['noReset'] = config['desired_caps']['noReset']
        desired_caps['app'] = f'{os.path.dirname(os.path.dirname(__file__))}/app/ContactManager.apk'
        self.driver = webdriver.Remote(appium_server_url, desired_caps)

    def tearDown(self) -> None:
        self.driver.quit()

    def test_contact(self):
        self._click_addContact_btn()
        time.sleep(2)
        self._add_Contact_Name("heihei")
        self._add_Contact_Phone("13800000000")
        self._add_Contact_Email("titanmax@163.com")
        self._save_button()
        time.sleep(3)

    def _click_addContact_btn(self):
        ele = self.driver.find_element(By.ID, "com.example.android.contactmanager:id/addContactButton")
        print("-------- 点击 Add Contact ----------")
        ele.click()

    def _add_Contact_Name(self,txt_name):
        ele = self.driver.find_element(By.ID, "com.example.android.contactmanager:id/contactNameEditText")
        print("-------- 输入 Contact Name ----------")
        ele.send_keys(txt_name)

    def _add_Contact_Phone(self,txt_phone):
        ele = self.driver.find_element(By.ID, "com.example.android.contactmanager:id/contactPhoneEditText")
        print("-------- 输入 Contact Phone ----------")
        ele.send_keys(txt_phone)

    def _add_Contact_Email(self, txt_email):
        ele = self.driver.find_element(By.ID, "com.example.android.contactmanager:id/contactEmailEditText")
        print("-------- 输入 Contact Email ----------")
        ele.send_keys(txt_email)

    def _save_button(self):
        ele = self.driver.find_element(By.ID, "com.example.android.contactmanager:id/contactSaveButton")
        print("---- 保存 ------")
        ele.click()

