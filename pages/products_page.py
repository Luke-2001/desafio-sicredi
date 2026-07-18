import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.element_utils import ElementUtils


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_add_to_cart(self, product):

        product_name = product["produto"]
        product_id_name = product_name.lower().replace(" ", "-")
        product_id = f"add-to-cart-{product_id_name}"

        try:
            element = self.wait.until(
                EC.element_to_be_clickable(
                    (By.ID, product_id)
                )
            )
        except TimeoutException:
            raise Exception(
                f"Produto não encontrado: {product_name}"
            )

        ElementUtils.highlight(
            self.driver,
            element
        )

        element.click()

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, f"remove-{product_id_name}")
                )
            )
        except TimeoutException:
            raise Exception(
                f"Falha ao adicionar produto: {product_name}"
            )

        logging.info(
            f"Produto adicionado com sucesso: {product_name}"
        )

        return True
