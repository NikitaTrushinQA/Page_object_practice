from .pages.product_page import ProductPage
import time
import pytest



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
def test_guest_can_add_product_to_cart(browser,link):
    '''Проверки: добавление товара в корзину,
                 наличие сообщения о добавлении товара в корзину,
                 имя добавленного товара соответствует имени в корзине,
                 наличие сообщения со стоимостью корзины,
                 cтоимость корзины совпадает с ценой товара'''
    #link = ' http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding_product()
    page.check_name_of_added_product_to_cart()
    page.should_be_message_with_total_cart_price()
    page.check_total_price_of_cart()


