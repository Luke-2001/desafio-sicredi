from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.util_elementos import UtilElementos


class PaginaCarrinho:
    BOTAO_CARRINHO = (By.CLASS_NAME, "shopping_cart_link")
    ITENS_CARRINHO = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def clicar_carrinho(self):
        elemento = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_CARRINHO)
        )
        UtilElementos.destacar(self.driver, elemento)
        elemento.click()

    def obter_produtos_do_carrinho(self):
        elementos = self.wait.until(
            EC.visibility_of_all_elements_located(self.ITENS_CARRINHO)
        )

        return [elemento.text for elemento in elementos]

    def obter_produtos_ausentes(self, produtos_esperados):
        produtos_carrinho = self.obter_produtos_do_carrinho()

        produtos_ausentes = [
            produto
            for produto in produtos_esperados
            if produto not in produtos_carrinho
        ]

        return produtos_ausentes

    def validar_produtos(self, produtos_esperados):
        produtos_ausentes = self.obter_produtos_ausentes(produtos_esperados)
        if produtos_ausentes:
            raise AssertionError(
                "Validação do carrinho falhou. "
                f"Produtos ausentes: {produtos_ausentes}"
            )

    def capturar_tela_carrinho(self):
        self.driver.save_screenshot(
            "screenshots/cart.png"
        )
