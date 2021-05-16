from fixture.session import SessionHelper
import re

class ProjectHelper():
    def __init__(self, app):
        self.app = app

    def configuration_tab(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()

    def get_project_list(self):
        wd = self.app.wd
        self.configuration_tab()
        project = []
        j = 0
        links = [elem.get_attribute("href") for elem in wd.find_elements_by_tag_name('a')]
        text = [elem.get_attribute("text") for elem in wd.find_elements_by_tag_name('a')]
        for i in links:
            if "?project_id=" in i:
                project.append([i.split("id=")[1],text[j]])
            j+=1
        return project

    def get_project_id(self, name):
        wd = self.app.wd
        self.configuration_tab()
        id = 0
        j = 0
        links = [elem.get_attribute("href") for elem in wd.find_elements_by_tag_name('a')]
        text = [elem.get_attribute("text") for elem in wd.find_elements_by_tag_name('a')]
        for i in text:
            if name in i:
               id = links[j].split("id=")[1]
            j += 1
        return id

    def create_new_rpoject(self, name, description):
        wd = self.app.wd
        wd.find_element_by_xpath(u"//input[@value='Create New Project']").click()
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(name)
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(description)
        wd.find_element_by_xpath(u"//input[@value='Add Project']").click()
        return self.get_project_id(name)


    def projet_page(self, id):
        wd = self.app.wd
        wd.get("http://localhost/mantisbt-1.3.20/manage_proj_edit_page.php?project_id="+id)
        input = wd.find_element_by_id("project-name")
        return input.get_attribute('value')

    def delete_project(self):
        wd = self.app.wd
        wd.find_element_by_xpath(u"//input[@value='Delete Project']").click()
        wd.find_element_by_xpath(u"//input[@value='Delete Project']").click()


