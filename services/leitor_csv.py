import csv


class LeitorCsv:

    @staticmethod
    def ler_produtos(caminho_arquivo):
        produtos = []

        with open(caminho_arquivo, newline="", encoding="utf-8") as arquivo_csv:
            leitor = csv.DictReader(arquivo_csv)

            for linha in leitor:

                try:

                    produtos.append({
                        "produto": linha["Produto"].strip(),
                        "quantidade": int(linha["Quantidade"])
                    })

                except (KeyError, ValueError) as erro:
                    raise Exception(
                        f"Erro ao ler CSV: {erro}"
                    )

        return produtos
