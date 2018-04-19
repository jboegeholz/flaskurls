import importlib.util
import os

ERROR_MSG = """
Wrong mapping format!
The syntax is either (<route>, <function>, <http_method>) or (<prefix>, <module>)
"""


def register_urls(app, urls, prefix=None):
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
        if number_of_args not in (2, 3):
            raise Exception(ERROR_MSG)

        if isinstance(url[0], str):
            if hasattr(url[1], '__call__'):
                if number_of_args == 3 and isinstance(url[2], list):
                    _register_endpoint(app, prefix, url[0], url[1], url[2])
                elif number_of_args == 2:
                    _register_endpoint(app, prefix, url[0], url[1], ["GET"])
                else:
                    raise Exception(ERROR_MSG)
            elif isinstance(url[1], str):
                _register_component(app, url)
            else:
                raise Exception(ERROR_MSG)


def _register_component(app, url):
    app.logger.info("Registering component: " + str(url))
    urls_file = url[1]
    prefix = url[0]
    if isinstance(urls_file, str):
        app.logger.info("Importing: " + urls_file)
        urls_file = urls_file.split(".")
        package = urls_file[0]
        module_name = urls_file[1]
        module_path = os.path.join(app.root_path, package)
        urls_path = os.path.join(module_path, module_name + ".py")
        foo = _load_module(urls_path)
        _register_urls(app, foo.urls, prefix)
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
