from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID,'login_form')
    LOGIN_RESTRATION_FORM = (By.ID,'register_form')

class ProductPageLocators():
    PRODUCT_PAGE_ADD_TO_CART_BUTTON=(By.CLASS_NAME,'btn.btn-lg.btn-primary.btn-add-to-basket')
    NAME_OF_PRODUCT = (By.CSS_SELECTOR,'.col-sm-6.product_main h1')
    NAME_OF_PRODUCT_IN_MESSAGE=(By.CSS_SELECTOR,'#messages .alert-success .alertinner strong')
    MESSAGE_ABOUT_ADDING_PRODUCT =(By.CSS_SELECTOR,'#messages .alert-success .alertinner ')
    PRODUCT_PRICE =(By.CSS_SELECTOR,'.col-sm-6.product_main .price_color')
    CART_PRICE = (By.CSS_SELECTOR,'.alertinner p strong')
    MESSAGE_ABOUT_CART_PRICE =(By.CSS_SELECTOR,'.alertinner p:first-child')
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR,'.btn-group' )

class BasketPageLocators():
    BASKET_ITEMS = (By.CSS_SELECTOR,'.basket_summary ')

