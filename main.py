import logging

from config import settings
from pages.pagina_carrinho import PaginaCarrinho
from pages.pagina_checkout import PaginaCheckout
from pages.pagina_login import PaginaLogin
from pages.pagina_menu import PaginaMenu
from pages.pagina_produtos import PaginaProdutos
from services.leitor_csv import LeitorCsv
from services.servico_relatorio import ServicoRelatorio
from utils.criador_driver import criar_driver


def main():
    produtos_sucesso = []
    produtos_falha = []
    driver = None

    try:
        driver = criar_driver()

        if settings.DEBUG:
            logging.info(
                "Iniciando automação do desafio-sicredi..."
            )

        driver.get("https://www.saucedemo.com")

        # Login
        pagina_login = PaginaLogin(driver)

        pagina_login.realizar_login(
            "standard_user",
            "secret_sauce"
        )

        logging.info(
            "Login realizado com sucesso."
        )

        # Produtos
        produtos = LeitorCsv.ler_produtos(
            "data/produtos_compra.csv"
        )

        pagina_produtos = PaginaProdutos(driver)

        for produto in produtos:
            try:
                pagina_produtos.adicionar_produto_carrinho(
                    produto
                )

                produtos_sucesso.append(
                    produto["produto"]
                )

                logging.info(
                    "Produto adicionado: %s",
                    produto["produto"]
                )

            except Exception as erro:
                logging.error(
                    "Erro ao adicionar produto %s: %s",
                    produto["produto"],
                    erro
                )

                produtos_falha.append(
                    {
                        "produto": produto["produto"],
                        "erro": str(erro)
                    }
                )

        # Não continuar sem produtos
        if not produtos_sucesso:
            logging.error(
                "Nenhum produto foi adicionado ao carrinho."
            )

            ServicoRelatorio.gerar_relatorio(
                produtos_sucesso,
                produtos_falha,
                "Compra não realizada"
            )
            return

        # Carrinho
        pagina_carrinho = PaginaCarrinho(driver)

        pagina_carrinho.clicar_carrinho()
        pagina_carrinho.capturar_tela_carrinho()

        produtos_ausentes = (
            pagina_carrinho.obter_produtos_ausentes(
                produtos_sucesso
            )
        )

        for produto in produtos_ausentes:
            logging.warning(
                "Produto ausente no carrinho: %s",
                produto
            )

            produtos_falha.append(
                {
                    "produto": produto,
                    "erro": "Produto ausente no carrinho"
                }
            )

        # Checkout
        pagina_checkout = PaginaCheckout(driver)

        try:
            pagina_checkout.clicar_checkout()

            pagina_checkout.preencher_informacoes(
                "Lucas",
                "Bassanesi",
                "87000-000"
            )

            pagina_checkout.clicar_continuar()
            pagina_checkout.clicar_finalizar()

        except Exception as erro:
            logging.error(
                "Erro no checkout: %s",
                erro
            )

            ServicoRelatorio.gerar_relatorio(
                produtos_sucesso,
                produtos_falha,
                f"Falha no checkout: {erro}"
            )
            return

        pagina_checkout.capturar_tela_confirmacao()

        mensagem_confirmacao = (
            pagina_checkout.obter_mensagem_confirmacao()
        )

        logging.info(
            "Compra finalizada: %s",
            mensagem_confirmacao
        )

        pagina_checkout.clicar_gerar_pdf()
        pagina_checkout.clicar_voltar_produtos()

        # Relatório antes do logout
        ServicoRelatorio.gerar_relatorio(
            produtos_sucesso,
            produtos_falha,
            mensagem_confirmacao
        )

        # Logout
        pagina_menu = PaginaMenu(driver)

        pagina_menu.abrir_menu()
        pagina_menu.realizar_logout()
        pagina_menu.validar_logout()

        logging.info(
            "Automação finalizada com sucesso."
        )

        if settings.DEBUG:
            input(
                "Pressione ENTER para fechar..."
            )

    except Exception as erro:
        logging.exception(
            "Erro inesperado: %s",
            erro
        )

        ServicoRelatorio.gerar_relatorio(
            produtos_sucesso,
            produtos_falha,
            f"Falha inesperada: {erro}"
        )

    finally:
        if driver:
            driver.quit()


if __name__ == "__main__":
    main()
