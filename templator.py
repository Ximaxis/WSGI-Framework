"""
Using the template engine jinja2
"""
from jinja2 import Template


def render(template_name, **kwargs):
    """
    A minimal example of working with the template engine
    :param template_name: template name
    :param kwargs: parameters to pass to the template
    :return:
    """
    with open(template_name) as f:
        template = Template(f.read())
    return template.render(**kwargs)


if __name__ == '__main__':
    output_test = render('authors.html', object_list=[{'name': 'Maxim'}, {'name': 'Baranov'}])
    print(output_test)
