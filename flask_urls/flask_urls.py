def register_urls(app, urls):
    for url in urls:
        app.add_url_rule(url[0], methods=url[1], view_func=url[2])
