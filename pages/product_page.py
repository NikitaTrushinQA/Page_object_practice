from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart(self):
        """Добавление товара в корзину"""
        add_to_card_button = self.browser.find_element(*ProductPageLocators.PRODUCT_PAGE_ADD_TO_CART_BUTTON)
        add_to_card_button.click()

    def check_name_of_added_product_to_cart(self):
        """Проверка, соответствия названия добавленного товара с  названим товара в сообщении"""
        NAME = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        NAME_IN_MESSAGE = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_MESSAGE).text
        assert NAME == NAME_IN_MESSAGE, f'"{NAME}" not equal to"{NAME_IN_MESSAGE}"'

    def should_be_message_about_adding_product(self):
        """Проверка наличия сообщения о добавлении товара в корзину"""
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING_PRODUCT), "MESSAGE ABOUT ADDING PRODUCT is not presented"

    def should_be_message_with_total_cart_price(self):
        """Проверка наличия сообщения с суммой корзины"""
        assert self.is_element_present(*ProductPageLocators.MESSAGE_ABOUT_CART_PRICE), "MESSAGE ABOUT CART PRICE is not presented"

    def check_total_price_of_cart(self):
        """Проверка что стоимость корзины совпадает с ценой товара"""
        basket_total = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_price == basket_total, f'"{product_price} == {basket_total}" не верно'

    def get_item_name_in_cart(self):
        """Возвращает имя товара в корзине"""
        item_in_cart = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT_IN_MESSAGE).text
        return item_in_cart

    def get_name_of_product(self):
        """Возвращает имя товара"""
        name_of_product = self.browser.find_element(*ProductPageLocators.NAME_OF_PRODUCT).text
        return name_of_product

    def get_item_price(self):
        """Возвращает цену товара"""
        item_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        return item_price

    def get_item_price_in_cart(self):
        """Возвращает цену товара в корзине"""
        item_price_in_cart = self.browser.find_element(*ProductPageLocators.CART_PRICE).text
        return item_price_in_cart

    def should_not_be_success_message(self):
        '''Проверяем, что нет сообщения об успехе'''
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ABOUT_ADDING_PRODUCT), "Success message is presented, but should not be"

    def success_message_disappeared(self):
        """Проверяем,что сообщение об успешном добавлении товара в корзину исчезло"""
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ABOUT_ADDING_PRODUCT), "Success message is presented, but should not be"
