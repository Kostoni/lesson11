from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.opera import OperaDriverManager


class WebDriverFactory:
    @classmethod
    def get(cls, browser: str) -> webdriver:
        if browser == "firefox":
            wd = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        elif browser == "opera":
            wd = webdriver.Opera(executable_path=OperaDriverManager().install())
        else:
            wd = webdriver.Chrome(ChromeDriverManager().install())

        wd.maximize_window()

        return wd
