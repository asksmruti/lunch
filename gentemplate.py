import os
from jinja2 import Environment, FileSystemLoader


def html(getlist):
    getlist = [getlist]
    jdict = {
        'allLists': getlist,
    }
    root = os.path.dirname(os.path.abspath(__file__))
    templates_dir = os.path.join(root, 'templates')
    env = Environment(loader=FileSystemLoader(templates_dir))
    template = env.get_template('template.html')
    output = template.render(jdict)
    return output
