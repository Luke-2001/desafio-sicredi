from datetime import datetime


class ReportService:

    @staticmethod
    def generate_report(
            success_products,
            failed_products,
            confirmation_message
    ):

        with open(
                "relatorio_compras.txt",
                "w",
                encoding="utf-8"
        ) as file:

            file.write(
                f"Data execução: "
                f"{datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n\n"
            )

            file.write(
                f"Sucessos: {len(success_products)}\n"
            )

            file.write(
                f"Falhas: {len(failed_products)}\n\n"
            )

            file.write(
                "=== PRODUTOS COM SUCESSO ===\n"
            )

            for product in success_products:
                file.write(f"{product}\n")

            file.write(
                "\n=== PRODUTOS COM ERRO ===\n"
            )

            for product in failed_products:
                file.write(
                    f"{product['produto']} - "
                    f"{product['erro']}\n"
                )

            file.write(
                f"\nConfirmação: "
                f"{confirmation_message or 'Não disponível'}\n"
            )
