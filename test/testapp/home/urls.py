from test.testapp.home import views

urls = [
  ('/home_index', views.home_index, ['GET']),
  ('/home_users', views.home_users, ['GET'])
]