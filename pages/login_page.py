from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.element_utils import ElementUtils


class LoginPage:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    PRODUCTS_TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def login(self, username, password):
        username_field = self.wait.until(
            EC.visibility_of_element_located(self.USERNAME)
        )
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )

        self.type_text(username_field, username)
        self.type_text(password_field, password)

        element = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )

        ElementUtils.highlight(self.driver, element)
        element.click()

        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    self.PRODUCTS_TITLE
                )
            )
        except TimeoutException:
            raise Exception("Falha no login")

    @staticmethod
    def type_text(element, text):
        element.clear()
        element.send_keys(text)
