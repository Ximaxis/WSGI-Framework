"""
Работа с шаблонами, паттерн INTERFACE
Используем шаблонизатор jinja2
"""
from jinja2 import Template, FileSystemLoader
from jinja2.environment import Environment
import os


def render(template_name, folder='templates', **kwargs):
    # рассказать про простую загрузку и про указание путей
    # file_path = os.path.join(folder, template_name)
    # # Открываем шаблон по имени
    # with open(file_path, encoding='utf-8') as f:
    #     # Читаем
    #     template = Template(f.read())
    # # рендерим шаблон с параметрами
    # return template.render(**kwargs)
    env = Environment()
    env.loader = FileSystemLoader(folder)
    #file_path = os.path.join(folder, template_name)
    tmpl = env.get_template(template_name)
    return tmpl.render(**kwargs)

# from jinja import FileSystemLoader
# from jinja.environment import Environment
#
# env = Environment()
# env.loader = FileSystemLoader('.')
# tmpl = env.get_template('page.html')
# print tmpl.render(parser.vars)
