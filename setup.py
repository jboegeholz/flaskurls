import setuptools

# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='flask_url_mapping',
    version='0.6',
    packages=['flask_url_mapping'],
    url='https://github.com/jboegeholz/flaskurls',
    download_url='https://github.com/jboegeholz/flaskurls/archive/0.2.tar.gz',
    license='MIT',
    author='Joern Boegeholz',
    author_email='boegeholz.joern@gmail.com',
    description='Django-style url handling for Flask',
    long_description=long_description,
    long_description_content_type='text/markdown',
    install_requires=["Flask", "Flask-Login"]
)
