"""
This is used to build a exe file for this Application
To run this file ---->python C:\Users\Kuchukulla\PycharmProjects\Python\Chatapp\Chat_consoleapp\setup.py build
"""

import sys
from cx_Freeze import setup, Executable


exe = Executable(
      script="C:\\Users\\Kuchukulla\\PycharmProjects\\Python\\Chatapp\\Chat_consoleapp\\main.py",
      base="console",
      targetName="C:\\Users\\Kuchukulla\\PycharmProjects\\Python\\Chatapp\\Chat_consoleapp\\executable\\ConsoleChatApp.exe"
     )
setup(
      name="ConsoleChatApp.exe",
      version="1.0",
      author="Ritesh",
      description="Console Chat Application",
      executables=[exe]
      )