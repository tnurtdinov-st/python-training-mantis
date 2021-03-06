from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.singup import SingupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, config):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            self.wd = webdriver.Chrome()
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        #self.wd.implicitly_wait(10)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.base_url=config['web']['baseUrl']
        self.config = config
        self.james = JamesHelper(self)
        self.mail = MailHelper(self)
        self.signup = SingupHelper(self)
        self.soap = SoapHelper(self)

    def is_vaild(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def destroy(self):
        self.wd.quit()

    def open_home_page(self):
        wd = self.wd
        # Open homepage
        if not (wd.current_url.endswith("/mantisbt-1.3.20/")):
            wd.get("http://localhost/mantisbt-1.3.20/")
        wd.get("http://localhost/mantisbt-1.3.20/")
