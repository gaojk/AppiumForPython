from page_object.page_ui.login_page import LoginPage


class LoginHandle(LoginPage):

    def input_username(self, value):
        """
            输入用户名
        :param value:
        :return:
        """
        self.get_username_element().send_keys(value)

    def input_password(self, value):
        """
            输入密码
        :param value:
        :return:
        """
        self.get_password_element().send_keys(value)

    def click_login_button(self):
        """
            点击[登录]按钮
        :return:
        """
        self.get_login_button_element().click()