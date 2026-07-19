import logging

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.util_elementos import UtilElementos


class PaginaProdutos:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def adicionar_produto_carrinho(self, produto):

        nome_produto = produto["produto"]
        id_nome_produto = nome_produto.lower().replace(" ", "-")
        id_produto = f"add-to-cart-{id_nome_produto}"

        try:
            elemento = self.wait.until(
                EC.element_to_be_clickable(
                    (By.ID, id_produto)
                )
            )
        except TimeoutException as erro:
            raise Exception(
                f"Produto não encontrado: {nome_produto}"
            ) from erro

        UtilElementos.destacar(
            self.driver,
            elemento
        )

        elemento.click()

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.ID, f"remove-{id_nome_produto}")
                )
            )
        except TimeoutException as erro:
            raise Exception(
                f"Falha ao adicionar produto: {nome_produto}"
            ) from erro

        logging.info(
            "Produto adicionado com sucesso: %s",
            nome_produto
        )

        return True
