from datetime import datetime


class ServicoRelatorio:

    @staticmethod
    def gerar_relatorio(
            produtos_sucesso,
            produtos_falha,
            mensagem_confirmacao
    ):

        with open(
                "relatorio_compras.txt",
                "w",
                encoding="utf-8"
        ) as arquivo:

            arquivo.write(
                f"Data execução: "
                f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
            )

            arquivo.write(
                f"Sucessos: {len(produtos_sucesso)}\n"
            )

            arquivo.write(
                f"Falhas: {len(produtos_falha)}\n\n"
            )

            arquivo.write(
                "=== PRODUTOS COM SUCESSO ===\n"
            )

            for produto in produtos_sucesso:
                arquivo.write(f"{produto}\n")

            arquivo.write(
                "\n=== PRODUTOS COM ERRO ===\n"
            )

            for produto in produtos_falha:
                arquivo.write(
                    f"{produto['produto']} - "
                    f"{produto['erro']}\n"
                )

            arquivo.write(
                f"\nConfirmação: "
                f"{mensagem_confirmacao or 'Não disponível'}\n"
            )
