from utils.get_by_local import GetByLocal


class LoginPage(object):

    file_path = "/Users/lvjing/PycharmProjects/AppiumForPython/config/local_element.ini"

    def __init__(self, driver):
        self.get_by_local = GetByLocal(driver)

    # 获取登录页面所有的页面元素信息
    def get_username_element(self):
        """
            获取登录用户名元素
        :return:
        """
        username = self.get_by_local.get_element(self.file_path, "login_element", "username")
        return username

    def get_password_element(self):
        """
            获取登录密码元素
        :return:
        """
        password = self.get_by_local.get_element(self.file_path, "login_element", "password")
        return password

    def get_login_button_element(self):
        """
            获取[登录]按钮元素
        :return:
        """
        login_button = self.get_by_local.get_element(self.file_path, "login_element", "login_button")
        return login_button