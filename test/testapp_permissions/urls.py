from test.testapp import views

urls = [
    ("/", views.index, ["GET"]),
    ("/users", views.get_users, ["GET"]),
    ("/home", "home.urls")
]
