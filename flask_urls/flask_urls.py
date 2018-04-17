from __future__ import print_function
import importlib.util
import os


def register_urls(app, urls, prefix=None):
    for url in urls:
        number_of_args = len(url)
        if number_of_args == 3:
            register_endpoint(app, prefix, url)
        elif number_of_args == 2:
            register_component(app, url)


def register_component(app, url):
    print("Registering component: " + str(url))
    urls_file = url[1]
    prefix = url[0]
    if isinstance(urls_file, str):
        print("Importing: " + urls_file)
        urls_file = urls_file.split(".")
        package = urls_file[0]
        module_name = urls_file[1]
        module_path = os.path.join(app.root_path, package, module_name + ".py")
        spec = importlib.util.spec_from_file_location("urls", module_path)
        foo = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(foo)
        register_urls(app, foo.urls, prefix)


def register_endpoint(app, prefix, url):
    print("Registering endpoint: " + str(url))
    if prefix:
        endpoint = prefix + url[0]
    else:
        endpoint = url[0]
    app.add_url_rule(endpoint, methods=url[2], view_func=url[1])
