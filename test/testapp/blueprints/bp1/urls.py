from test.testapp.blueprints.bp1 import views

urls = [
  ('/bp1_index', views.index(), ['GET'])
]