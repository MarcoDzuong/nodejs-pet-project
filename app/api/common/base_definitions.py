from flask import Flask

class BaseFlask(Flask):
    def __init__(self,import_name):Flask.__init__(self,import_name)