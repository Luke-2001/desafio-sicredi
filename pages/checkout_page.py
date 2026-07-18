from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.element_utils import ElementUtils


class CheckoutPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    GENERATE_PDF_ORDER_BUTTON = (By.ID, "generate-pdf-order")
    BACK_TO_PRODUCTS_BUTTON = (By.ID, "back-to-products")
    CONFIRMATION_MESSAGE = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_checkout(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.CHECKOUT_BUTTON)
        )

        ElementUtils.highlight(self.driver, element)
        element.click()

    def fill_information(self, first_name, last_name, postal_code):
        first = self.wait.until(
            EC.visibility_of_element_located(self.FIRST_NAME)
        )
        last = self.driver.find_element(*self.LAST_NAME)
        postal = self.driver.find_element(*self.POSTAL_CODE)

        self.type_text(first, first_name)
        self.type_text(last, last_name)
        self.type_text(postal, postal_code)

    def click_continue(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.CONTINUE_BUTTON)
        )

        ElementUtils.highlight(self.driver, element)
        element.click()

    def click_finish(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.FINISH_BUTTON)
        )

        ElementUtils.highlight(self.driver, element)
        element.click()

    def click_generate_pdf(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.GENERATE_PDF_ORDER_BUTTON)
        )

        ElementUtils.highlight(self.driver, element)
        element.click()

    def click_back_to_products(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.BACK_TO_PRODUCTS_BUTTON)
        )

        ElementUtils.highlight(self.driver, element)
        element.click()

    @staticmethod
    def type_text(element, text):
        element.clear()
        element.send_keys(text)

    def get_confirmation_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.CONFIRMATION_MESSAGE
            )
        ).text

    def take_confirmation_screenshot(self):
        self.driver.save_screenshot(
            "screenshots/confirmation.png"
        )
