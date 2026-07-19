import logging

DEBUG = True

logging.basicConfig(
    filename="logs/automacao.log",
    level=logging.DEBUG if DEBUG else logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
