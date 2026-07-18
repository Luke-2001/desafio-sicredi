from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.element_utils import ElementUtils


class CartPage:
    CART_BUTTON = (By.CLASS_NAME, "shopping_cart_link")
    CART_ITEMS = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_cart(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.CART_BUTTON)
        )
        ElementUtils.highlight(self.driver, element)
        element.click()

    def get_cart_products(self):
        elements = self.wait.until(
            EC.visibility_of_all_elements_located(self.CART_ITEMS)
        )

        return [element.text for element in elements]

    def get_missing_products(self, expected_products):
        cart_products = self.get_cart_products()

        missing_products = [
            product
            for product in expected_products
            if product not in cart_products
        ]

        return missing_products

    def validate_products(self, expected_products):
        missing_products = self.get_missing_products(expected_products)
        if missing_products:
            raise AssertionError(
                "Validação do carrinho falhou. "
                f"Produtos ausentes: {missing_products}"
            )

    def take_cart_screenshot(self):
        self.driver.save_screenshot(
            "screenshots/cart.png"
        )
