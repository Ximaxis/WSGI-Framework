"""
Using the template engine jinja2
"""
import os
from jinja2 import Template, Environment, FileSystemLoader


def render(template_name, folder='templates', **kwargs):
    """
    A minimal example of working with the template engine
    :param template_name: template name
    :param kwargs: parameters to pass to the template
    :return:
    
    file_path = os.path.join(folder, template_name)
    with open(file_path, encoding='utf-8') as f:
        template = Template(f.read())
    return template.render(**kwargs)
    """
    env = Environment()
    env.loader = FileSystemLoader(folder)
    tmpl = env.get_template(template_name)
    return tmpl.render(**kwargs)


if __name__ == '__main__':
    output_test = render('authors.html', object_list=[{'name': 'Maxim'}, {'name': 'Baranov'}])
    print(output_test)
