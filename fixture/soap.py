from suds.client import Client
from suds import WebFault

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.config['web']['baseUrl'] +"api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_project_list(self, username, password):
        client = Client(self.app.config['web']['baseUrl']+"api/soap/mantisconnect.php?wsdl")
        project = []
        try:
            tmp = client.service.mc_projects_get_user_accessible(username, password)
            for i in tmp:
                project.append([str(i['id']), str(i['name'])])
            return project
        except WebFault:
            return False