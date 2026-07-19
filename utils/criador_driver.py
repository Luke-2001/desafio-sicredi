import os

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

modo_headless = os.getenv("HEADLESS", "false").lower() == "true"


def criar_driver():
    modo_headless = os.getenv("HEADLESS", "false").lower() == "true"

    opcoes = webdriver.EdgeOptions()
    opcoes.add_argument("--start-maximized")

    if modo_headless:
        opcoes.add_argument("--headless=new")

    return webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=opcoes
    )
