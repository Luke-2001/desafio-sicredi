class ElementUtils:

    @staticmethod
    def highlight(driver, element):
        try:
            driver.execute_script("""
                arguments[0].scrollIntoView({
                    block: 'center'
                });
            """, element)

            driver.execute_script("""
                arguments[0].style.transition = '0.2s';
                arguments[0].style.boxShadow = '0 0 20px red';
            """, element)

            driver.execute_script("""
                arguments[0].style.boxShadow = '';
            """, element)

        except Exception:
            pass
