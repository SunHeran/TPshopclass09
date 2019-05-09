import allure
from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class HomePage(BaseAction):
    # 首页 - 我的
    mine_button = By.XPATH, "//*[@text='我的' and @resource-id='com.tpshop.malls:id/tab_txtv']"

    # 点击 我的
    @allure.step(title='主页 - 点击 我的')
    def click_mine(self):
        self.click(self.mine_button)