import os, sys; sys.path.insert(0, os.path.dirname(__file__))
print(sys.path)
from NewScreen import welcome
from NewButton import click

welcome()
click()