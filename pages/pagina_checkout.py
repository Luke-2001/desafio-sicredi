from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.util_elementos import UtilElementos


class PaginaCheckout:
    BOTAO_CHECKOUT = (By.ID, "checkout")
    CAMPO_NOME = (By.ID, "first-name")
    CAMPO_SOBRENOME = (By.ID, "last-name")
    CAMPO_CEP = (By.ID, "postal-code")
    BOTAO_CONTINUAR = (By.ID, "continue")
    BOTAO_FINALIZAR = (By.ID, "finish")
    BOTAO_GERAR_PDF_PEDIDO = (By.ID, "generate-pdf-order")
    BOTAO_VOLTAR_PRODUTOS = (By.ID, "back-to-products")
    MENSAGEM_CONFIRMACAO = (By.CLASS_NAME, "complete-header")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def clicar_checkout(self):
        elemento = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_CHECKOUT)
        )

        UtilElementos.destacar(self.driver, elemento)
        elemento.click()

    def preencher_informacoes(self, nome, sobrenome, cep):
        campo_nome = self.wait.until(
            EC.visibility_of_element_located(self.CAMPO_NOME)
        )
        campo_sobrenome = self.driver.find_element(*self.CAMPO_SOBRENOME)
        campo_cep = self.driver.find_element(*self.CAMPO_CEP)

        self.digitar_texto(campo_nome, nome)
        self.digitar_texto(campo_sobrenome, sobrenome)
        self.digitar_texto(campo_cep, cep)

    def clicar_continuar(self):
        elemento = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_CONTINUAR)
        )

        UtilElementos.destacar(self.driver, elemento)
        elemento.click()

    def clicar_finalizar(self):
        elemento = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_FINALIZAR)
        )

        UtilElementos.destacar(self.driver, elemento)
        elemento.click()

    def clicar_gerar_pdf(self):
        elemento = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_GERAR_PDF_PEDIDO)
        )

        UtilElementos.destacar(self.driver, elemento)
        elemento.click()

    def clicar_voltar_produtos(self):
        elemento = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_VOLTAR_PRODUTOS)
        )

        UtilElementos.destacar(self.driver, elemento)
        elemento.click()

    @staticmethod
    def digitar_texto(elemento, texto):
        elemento.clear()
        elemento.send_keys(texto)

    def obter_mensagem_confirmacao(self):
        return self.wait.until(
            EC.visibility_of_element_located(
                self.MENSAGEM_CONFIRMACAO
            )
        ).text

    def capturar_tela_confirmacao(self):
        self.driver.save_screenshot(
            "screenshots/confirmation.png"
        )
