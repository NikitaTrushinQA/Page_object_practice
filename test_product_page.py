from .pages.product_page import ProductPage
import time
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.solve_quiz_and_get_code()
    #time.sleep(300)
    page.should_be_message_about_adding_product()
    page.check_name_of_added_product_to_cart()


