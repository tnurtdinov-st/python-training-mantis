from fixture.project import ProjectHelper
import random

def test_del_project(app):
    #Авторизация
    app.session.login("administrator", "secret")
    #Переход в управление проектами
    app.project.configuration_tab()
    #Запрос списка проектов SOAP
    project = app.soap.get_project_list("administrator", "secret")
    #Проверка на отсутствие проектов
    if len(project)==0:
        new_name = "Test " + str(random.randint(0, 10000))
        # Создание проекта с возвратом id проекта
        app.project.create_new_rpoject(new_name, new_name)
        project = app.soap.get_project_list("administrator", "secret")
    #Выбор рандомного проекта на удаление
    del_pro = random.choice(project)
    #Проверка корректностип перехода в профиль нужного проекта
    assert del_pro[1] == app.project.projet_page(del_pro[0])
    #Удаление проекта
    app.project.delete_project()
    #Запрос нового списка проектов SOAP
    new_project = app.soap.get_project_list("administrator", "secret")
    #Удаление удаленного проекта из первого списка
    project.remove(del_pro)
    #Сверка результата
    assert sorted(project) == sorted(new_project)

