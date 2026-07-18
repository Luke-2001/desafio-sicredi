import csv


class CsvReader:

    @staticmethod
    def read_products(file_path):
        products = []

        with open(file_path, newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:

                try:

                    products.append({
                        "produto": row["Produto"].strip(),
                        "quantidade": int(row["Quantidade"])
                    })

                except (KeyError, ValueError) as e:
                    raise Exception(
                        f"Erro ao ler CSV: {str(e)}"
                    )

        return products
