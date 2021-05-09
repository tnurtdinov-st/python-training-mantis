from fixture.project import ProjectHelper
import random

def test_del_project(app):
    #Авторизация
    app.session.login("administrator", "secret")
    #Переход в управление проектами
    app.project.configuration_tab()
    #Запрос списка проектов
    project = app.project.get_project_list()
    #Выбор рандомного проекта на удаление
    del_pro = random.choice(project)
    #Проверка корректностип перехода в профиль нужного проекта
    assert del_pro[1] == app.project.projet_page(del_pro[0])
    #Удаление проекта
    app.project.delete_project()
    #Запрос нового списка проектов
    new_project = app.project.get_project_list()
    #Удаление удаленного проекта из первого списка
    project.remove(del_pro)
    #Сверка результата
    assert sorted(project) == sorted(new_project)

