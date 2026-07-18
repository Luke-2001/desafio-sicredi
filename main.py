import logging

from config import settings
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.login_page import LoginPage
from pages.menu_page import MenuPage
from pages.products_page import ProductsPage
from services.csv_reader import CsvReader
from services.report_service import ReportService
from utils.driver_factory import create_driver


def main():
    successful_products = []
    failed_products = []
    driver = None

    try:
        driver = create_driver()

        if settings.DEBUG:
            logging.info(
                "Iniciando automação do desafio-sicredi..."
            )

        driver.get(
            "https://www.saucedemo.com"
        )

        # Login
        login_page = LoginPage(driver)

        login_page.login(
            "standard_user",
            "secret_sauce"
        )

        logging.info(
            "Login realizado com sucesso."
        )

        # Produtos
        products = CsvReader.read_products(
            "data/produtos_compra.csv"
        )

        products_page = ProductsPage(driver)

        for product in products:

            try:

                products_page.click_add_to_cart(
                    product
                )

                successful_products.append(
                    product["produto"]
                )

                logging.info(
                    f"Produto adicionado: {product['produto']}"
                )


            except Exception as e:

                logging.error(
                    f"Erro ao adicionar produto "
                    f"{product['produto']}: {str(e)}"
                )

                failed_products.append(
                    {
                        "produto": product["produto"],
                        "erro": str(e)
                    }
                )

        # Não continuar sem produtos
        if not successful_products:
            logging.error(
                "Nenhum produto foi adicionado ao carrinho."
            )

            ReportService.generate_report(
                successful_products,
                failed_products,
                "Compra não realizada"
            )

            return

        # Carrinho
        cart_page = CartPage(driver)

        cart_page.click_cart()

        cart_page.take_cart_screenshot()

        # Única validação do carrinho
        missing_products = (
            cart_page.get_missing_products(
                successful_products
            )
        )

        for product in missing_products:
            logging.warning(
                f"Produto ausente no carrinho: {product}"
            )

            failed_products.append(
                {
                    "produto": product,
                    "erro": "Produto ausente no carrinho"
                }
            )

        # Checkout
        checkout = CheckoutPage(driver)

        try:

            checkout.click_checkout()

            checkout.fill_information(
                "Lucas",
                "Bassanesi",
                "87000-000"
            )

            checkout.click_continue()

            checkout.click_finish()


        except Exception as e:

            logging.error(
                f"Erro no checkout: {str(e)}"
            )

            ReportService.generate_report(
                successful_products,
                failed_products,
                f"Falha no checkout: {str(e)}"
            )

            return

        checkout.take_confirmation_screenshot()

        confirmation_message = (
            checkout.get_confirmation_message()
        )

        logging.info(
            f"Compra finalizada: {confirmation_message}"
        )

        checkout.click_generate_pdf()

        checkout.click_back_to_products()

        # Relatório antes do logout
        ReportService.generate_report(
            successful_products,
            failed_products,
            confirmation_message
        )

        # Logout
        menu = MenuPage(driver)

        menu.open_menu()

        menu.logout()

        menu.validate_logout()

        logging.info(
            "Automação finalizada com sucesso."
        )

        if settings.DEBUG:
            input(
                "Pressione ENTER para fechar..."
            )



    except Exception as e:

        logging.exception(
            f"Erro inesperado: {str(e)}"
        )

        ReportService.generate_report(
            successful_products,
            failed_products,
            f"Falha inesperada: {str(e)}"
        )


    finally:

        if driver:
            driver.quit()


if __name__ == "__main__":
    main()
