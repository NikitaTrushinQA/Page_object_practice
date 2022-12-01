from .pages.product_page import ProductPage
import time
import pytest
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
from .pages.base_page import BasePage


@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser, link):
    """Проверки: добавление товара в корзину,
                 наличие сообщения о добавлении товара в корзину,
                 имя добавленного товара соответствует имени в корзине,
                 наличие сообщения со стоимостью корзины,
                 cтоимость корзины совпадает с ценой товара"""
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding_product()
    page.check_name_of_added_product_to_cart()
    page.should_be_message_with_total_cart_price()
    page.check_total_price_of_cart()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    """Проверка,отсутствия сообщения об успешном добавлении товара в корзину,после добавления товара в корзину
    """
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    time.sleep(1)
    page.success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_items_in_basket()
    basket_page.should_be_text_that_basket_is_empty()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email=email, password=password)
        page = BasePage(browser, link)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        """Проверки: добавление товара в корзину,
                     наличие сообщения о добавлении товара в корзину,
                     имя добавленного товара соответствует имени в корзине,
                     наличие сообщения со стоимостью корзины,
                     cтоимость корзины совпадает с ценой товара"""
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0'
        page = ProductPage(browser, link)
        page.open()
        page.add_to_cart()
        page.solve_quiz_and_get_code()
        page.should_be_message_about_adding_product()
        page.check_name_of_added_product_to_cart()
        page.should_be_message_with_total_cart_price()
        page.check_total_price_of_cart()
