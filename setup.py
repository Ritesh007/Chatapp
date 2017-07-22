"""
writes setup.py in distutils to create a zip file
command to run this python setup.py sdist --format zip
"""
from distutils.core import setup

setup(
    name="Console Chat app",
    version='1.0',
    packages = ['Chatapp','Chatapp.Test','Chatapp.utilities','Chatapp.files'],
    data_files = ['Chatapp/files/chat.txt','Chatapp/files/users.txt','__main__.py'],
    #metadata
    author='Ritesh',
    author_email='rithu.ritesh@gmail.com',
    description='A simple chat app that can be used on linux or windows console if python is installed on it',
)
