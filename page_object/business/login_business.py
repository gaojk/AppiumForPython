from page_object.handle.login_handle import LoginHandle


class LoginBusiness(LoginHandle):

    def login(self):
        username = "3123123"
        password = "234234"
        self.input_username(username)
        self.input_password(password)
        self.click_login_button()