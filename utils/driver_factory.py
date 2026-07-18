import os

from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager

headless = os.getenv("HEADLESS", "false").lower() == "true"


def create_driver():
    options = webdriver.EdgeOptions()
    options.add_argument("--start-maximized")

    if headless:
        options.add_argument("--headless=new")

    driver = webdriver.Edge(
        service=Service(EdgeChromiumDriverManager().install()),
        options=options
    )

    return driver
