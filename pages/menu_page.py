from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.element_utils import ElementUtils


class MenuPage:
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_menu(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.MENU_BUTTON)
        )

        ElementUtils.highlight(self.driver, element)
        element.click()

    def logout(self):
        element = self.wait.until(
            EC.element_to_be_clickable(self.LOGOUT_BUTTON)
        )

        ElementUtils.highlight(self.driver, element)
        element.click()

    def validate_logout(self):
        self.wait.until(
            EC.visibility_of_element_located(
                self.LOGIN_BUTTON
            )
        )

        return True
