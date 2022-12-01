from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        login_url = self.should_be_login_url()
        login_form = self.should_be_login_form()
        registe_form = self.should_be_register_form()

    def should_be_login_url(self):
        """проверка на корректный url адрес"""
        assert 'login' in self.url, "'login' is not in current_url"

    def should_be_login_form(self):
        """ проверка, что есть форма логина"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login_form is not presented"

    def should_be_register_form(self):
        """ проверка, что есть форма регистрации на странице"""
        assert self.is_element_present(*LoginPageLocators.LOGIN_RESTRATION_FORM), "register_form is not presented"

    def register_new_user(self, email, password):
        """Регистрируем нового пользователя"""
        email_field = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_FORM_EMAIL)
        email_field.send_keys(email)
        password_field = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_FORM_PASSWORD)
        password_field.send_keys(password)
        password_field_repeat = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_FORM_REPEAT_PASSWORD)
        password_field_repeat.send_keys(password)
        registration_button = self.browser.find_element(*LoginPageLocators.LOGIN_REGISTRATION_BUTTON)
        registration_button.click()
