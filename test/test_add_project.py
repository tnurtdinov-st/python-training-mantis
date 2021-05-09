from fixture.project import ProjectHelper
import random

def test_add_project(app):
    #Login
    app.session.login("administrator", "secret")
    #Переход в управление проектами
    app.project.configuration_tab()
    #Запрос списка проектов
    project = app.project.get_project_list()
    #Генерация рандомного имени проекта
    new_name="Test "+str(random.randint(0, 10000))
    #Создание проекта с возвратом id проекта
    id = app.project.create_new_rpoject(new_name, new_name)
    #Запрос нового списка проектов
    new_project = app.project.get_project_list()
    #Добавление новго проекта в старый список
    project.append([id,new_name])
    #Сверка результата
    assert sorted(project) == sorted(new_project)



