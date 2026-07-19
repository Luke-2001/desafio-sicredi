import logging

from selenium.common.exceptions import JavascriptException, WebDriverException

logger = logging.getLogger(__name__)


class UtilElementos:

    @staticmethod
    def destacar(driver, elemento):
        try:
            driver.execute_script("""
                arguments[0].scrollIntoView({
                    block: 'center'
                });
            """, elemento)

            driver.execute_script("""
                arguments[0].style.transition = '0.2s';
                arguments[0].style.boxShadow = '0 0 20px red';
            """, elemento)

            driver.execute_script("""
                arguments[0].style.boxShadow = '';
            """, elemento)

        except (JavascriptException, WebDriverException) as erro:
            logger.debug("Não foi possível destacar o elemento: %s", erro)
