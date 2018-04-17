import views

urls = [
  ('/', ['GET'], views.index),
  ('/users', ['GET'], views.get_users)
]