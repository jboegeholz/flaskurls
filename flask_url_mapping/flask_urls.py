import importlib.util  # needs backport to Python 2.7
# https://stackoverflow.com/questions/45350363/backport-of-importlib-for-python-2-7-from-3-6
import os

ERROR_MSG = """
Wrong mapping format!
The syntax is either (<route>, <function>, <http_method>) or (<prefix>, <module>)
"""

_permissions = {}


def register_urls(app, urls, prefix=""):
    app.logger.info("Registering Urls")
    _register_urls(app, urls, prefix)
    app.logger.info(app.url_map)


def _register_urls(app, urls, prefix):
    """Main entry point of the module. Takes an array of url mappings and registers them as url_rule at the Flask app
    :param app: a Flask app object
    :param urls: an array of tuples of (<route>, <function>, <http_method>) or (<prefix>, <module>)
    :param prefix: a prefix to the route
    :return:
    """
    app.logger.info("_register_urls")
    for url in urls:
        number_of_args = len(url)

        if number_of_args == 2 and isinstance(url[0], str) and hasattr(url[1], '__call__'):
            _register_endpoint(app, prefix, url[0], url[1], ["GET"])
        elif number_of_args == 2 and isinstance(url[0], str) and isinstance(url[1], str):
            _register_component(app, url)
        elif number_of_args == 3 and isinstance(url[0], str) and hasattr(url[1], '__call__') and isinstance(url[2], list):
            _register_endpoint(app, prefix, url[0], url[1], url[2])
        elif number_of_args == 4 and isinstance(url[0], str) and hasattr(url[1], '__call__') \
                and isinstance(url[2], list) and isinstance(url[3], str):
            _register_endpoint(app, prefix, url[0], url[1], url[2])
            _permissions[os.path.join(prefix, url[0])] = url[3]
            print(_permissions)
        else:
            raise Exception(ERROR_MSG)


def _register_component(app, url):
    app.logger.info("Registering component: " + str(url))
    prefix = url[0]
    urls_file = url[1]
    app.logger.info("Importing: " + urls_file)
    urls_file = urls_file.split(".")
    package = urls_file[0]
    module_name = urls_file[1]
    module_path = os.path.join(app.root_path, package)
    urls_path = os.path.join(module_path, module_name + ".py")
    loaded_module = _load_module(urls_path)
    _register_urls(app, loaded_module.urls, prefix)
    _append_template_path(app, module_path)


def _append_template_path(app, module_path):
    template_path = os.path.join(module_path, "templates")
    if os.path.isdir(template_path):
        app.jinja_loader.searchpath.append(template_path)


def _load_module(module_path):
    spec = importlib.util.spec_from_file_location("urls", module_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo


def _register_endpoint(app, prefix, route, view_func, methods):
    app.logger.info("Registering endpoint: " + str(route))
    if prefix:
        route = prefix + route
    app.add_url_rule(route, methods=methods, view_func=view_func)
