from selenium.webdriver.common.by import By

from base.base_action import BaseAction

import allure


class LoginPage(BaseAction):

    phone_edit_text = By.ID, "com.tpshop.malls:id/edit_phone_num"

    password_edit_text = By.ID, "com.tpshop.malls:id/edit_password"

    login_button = By.ID, "com.tpshop.malls:id/btn_login"

    # 输入 用户名
    @allure.step(title='登录 - 输入 用户名')
    def input_phone(self, content):
        allure.attach("输入用户名", content)
        self.input(self.phone_edit_text, content)

    # 输入 密码
    @allure.step(title='登录 - 输入 密码')
    def input_password(self, content):
        allure.attach("输入密码", content)
        self.input(self.password_edit_text, content)

    # 点击登录
    @allure.step(title='登录 - 点击 登录')
    def click_login(self):
        self.click(self.login_button)

    def is_login_button_enabled(self):
        return not self.find_element(self.login_button).get_attribute("enabled") == "false"