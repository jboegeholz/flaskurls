import importlib.util  # needs backport to Python 2.7
# https://stackoverflow.com/questions/45350363/backport-of-importlib-for-python-2-7-from-3-6
import os
from flask import current_app
from flask_login import current_user
ERROR_MSG = """
Wrong mapping format!
The syntax is either (<route>, <function>, <http_method>) or (<prefix>, <module>)
"""


class FlaskUrls(object):

    def __init__(self, app=None):
        self._permissions = {}
        if app is not None:
            self.app = app
            self.init_app(app)

    def init_app(self, app):
        app.url_value_preprocessors.setdefault(None, []).append(self._check_permissions)

    def _check_permissions(self, endpoint, values):
        """
        this function checks if a current user has the permission to 'use' the endpoint
        :param endpoint:
        :param values: not used but part of the signature
        :return:
        """
        with self.app.app_context():
            print(current_app.name)
            print("_check_permissions for: " + endpoint)
            print(current_user)


    def register_urls(self, urls, prefix=""):

        self.app.logger.info("Registering Urls")
        self._register_urls(urls, prefix)
        self.app.logger.info(self.app.url_map)

    def _register_urls(self, urls, prefix):
        """Main entry point of the module. Takes an array of url mappings and registers them as url_rule at the Flask app
        :param app: a Flask app object
        :param urls: an array of tuples of (<route>, <function>, <http_method>) or (<prefix>, <module>)
        :param prefix: a prefix to the route
        :return:
        """
        self.app.logger.info("_register_urls")
        for url in urls:
            number_of_args = len(url)

            if number_of_args == 2 and isinstance(url[0], str) and hasattr(url[1], '__call__'):
                self._register_endpoint(prefix, url[0], url[1], ["GET"])
            elif number_of_args == 2 and isinstance(url[0], str) and isinstance(url[1], str):
                self._register_component(url)
            elif number_of_args == 3 and isinstance(url[0], str) and hasattr(url[1], '__call__') and isinstance(url[2], list):
                self._register_endpoint(prefix, url[0], url[1], url[2])
            elif number_of_args == 4 and isinstance(url[0], str) and hasattr(url[1], '__call__') \
                    and isinstance(url[2], list) and isinstance(url[3], str):
                self._register_endpoint(prefix, url[0], url[1], url[2])
                self._permissions[os.path.join(prefix, url[0])] = url[3]
                print(self._permissions)
            else:
                raise Exception(ERROR_MSG)

    def _register_component(self, url):
        self.app.logger.info("Registering component: " + str(url))
        prefix = url[0]
        urls_file = url[1]
        self.app.logger.info("Importing: " + urls_file)
        urls_file = urls_file.split(".")
        package = urls_file[0]
        module_name = urls_file[1]
        module_path = os.path.join(self.app.root_path, package)
        urls_path = os.path.join(module_path, module_name + ".py")
        loaded_module = self._load_module(urls_path)
        self._register_urls(loaded_module.urls, prefix)
        self._append_template_path(module_path)

    def _append_template_path(self, module_path):
        template_path = os.path.join(module_path, "templates")
        if os.path.isdir(template_path):
            self.app.jinja_loader.searchpath.append(template_path)

    def _load_module(self, module_path):
        spec = importlib.util.spec_from_file_location("urls", module_path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        return foo

    def _register_endpoint(self, prefix, route, view_func, methods):
        self.app.logger.info("Registering endpoint: " + str(route))
        if prefix:
            route = prefix + route
        self.app.add_url_rule(route, methods=methods, view_func=view_func)
