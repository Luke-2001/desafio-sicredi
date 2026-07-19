from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.util_elementos import UtilElementos


class PaginaLogin:
    CAMPO_USUARIO = (By.ID, "user-name")
    CAMPO_SENHA = (By.ID, "password")
    BOTAO_LOGIN = (By.ID, "login-button")
    TITULO_PRODUTOS = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def realizar_login(self, usuario, senha):
        campo_usuario = self.wait.until(
            EC.visibility_of_element_located(self.CAMPO_USUARIO)
        )
        campo_senha = self.wait.until(
            EC.visibility_of_element_located(self.CAMPO_SENHA)
        )

        self.digitar_texto(campo_usuario, usuario)
        self.digitar_texto(campo_senha, senha)

        elemento = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_LOGIN)
        )

        UtilElementos.destacar(self.driver, elemento)
        elemento.click()

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.TITULO_PRODUTOS
                )
            )
        except TimeoutException as erro:
            raise Exception("Falha no login") from erro

    @staticmethod
    def digitar_texto(elemento, texto):
        elemento.clear()
        elemento.send_keys(texto)
