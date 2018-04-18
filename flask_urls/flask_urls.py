import importlib.util
import os


def register_urls(app, urls, prefix=None):
    app.logger.info("register_urls")
    for url in urls:
        number_of_args = len(url)
        if number_of_args == 3:
            register_endpoint(app, prefix, url)
        elif number_of_args == 2:
            register_component(app, url)


def register_component(app, url):
    app.logger.info("Registering component: " + str(url))
    urls_file = url[1]
    prefix = url[0]
    if isinstance(urls_file, str):
        app.logger.info("Importing: " + urls_file)
        urls_file = urls_file.split(".")
        package = urls_file[0]
        module_name = urls_file[1]
        module_path = os.path.join(app.root_path, package, module_name + ".py")
        foo = load_module(module_path)
        register_urls(app, foo.urls, prefix)


def load_module(module_path):
    spec = importlib.util.spec_from_file_location("urls", module_path)
    foo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(foo)
    return foo


def register_endpoint(app, prefix, url):
    app.logger.info("Registering endpoint: " + str(url))
    if prefix:
        endpoint = prefix + url[0]
    else:
        endpoint = url[0]
    app.add_url_rule(endpoint, methods=url[2], view_func=url[1])
