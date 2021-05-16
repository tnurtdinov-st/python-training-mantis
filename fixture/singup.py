import re

class SingupHelper:
    def __init__(self, app):
        self.app = app

    def new_user(self, username, email,  password):
        wd = self.app.wd
        wd.get(self.app.base_url + "/signup_page.php")
        wd.find_element_by_name("username").send_keys(username)
        wd.find_element_by_name("email").send_keys(email)
        wd.find_element_by_css_selector('input[type="submit"]').click()

        mail = self.app.mail.get_mail(username, password, "[MantisBT] Account registration")
        url = self.extract_confirmail_url(mail)
        wd.get(url)
        wd.find_element_by_name("password").send_keys(password)
        wd.find_element_by_name("password_confirm").send_keys(password)
        wd.find_element_by_css_selector('input[value="Update User"]').click()

    def extract_confirmail_url(self, text):
        return re.search("http://.*$", str(text), re.MULTILINE).group(0).split("\\n\\nIf you")[0]

   #ALT BACKUP
    # def extract_confirmail_url_alt(self, text):
    #     text = "http://" + text.split("http://")[1].split("If you")[0]
    #     return text.replace("=\n", "").replace("=3D", "=")



