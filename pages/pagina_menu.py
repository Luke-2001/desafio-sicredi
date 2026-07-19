from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.util_elementos import UtilElementos


class PaginaMenu:
    BOTAO_MENU = (By.ID, "react-burger-menu-btn")
    BOTAO_LOGOUT = (By.ID, "logout_sidebar_link")
    BOTAO_LOGIN = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def abrir_menu(self):
        elemento = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_MENU)
        )

        UtilElementos.destacar(self.driver, elemento)
        elemento.click()

    def realizar_logout(self):
        elemento = self.wait.until(
            EC.element_to_be_clickable(self.BOTAO_LOGOUT)
        )

        UtilElementos.destacar(self.driver, elemento)
        elemento.click()

    def validar_logout(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self.BOTAO_LOGIN
            )
        )

        return True
