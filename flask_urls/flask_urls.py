import importlib.util

import os


def register_urls(app, urls, prefix=None):
    for url in urls:
        number_of_args = len(url)
        if number_of_args == 3: # we register a single endpoint
            print("Registering endpoint: " + str(url))
            app.add_url_rule(url[0], methods=url[2], view_func=url[1])
        elif number_of_args == 2: # we register a component
            print("Registering component: " + str(url))
            urls_file = url[1]
            if isinstance(urls_file, str):
                print("Importing: " + urls_file)
                urls_file = urls_file.split(".")
                package = urls_file[0]
                module_name = urls_file[1]
                print(app.root_path)
                module_path = os.path.join(app.root_path, package, module_name + ".py")
                spec = importlib.util.spec_from_file_location("urls", module_path)
                foo = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(foo)
                print(foo.urls)
                register_urls(app, foo.urls)
