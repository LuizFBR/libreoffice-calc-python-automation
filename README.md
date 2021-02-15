# libreoffice-calc-python-automation
A repo containing a folder structure, automation scripts and a game of life script for libreoffice calc.

# How to use it

Run init.sh to enable python macros in your calc process. Then, you may run your python programs as normal. Python3 is recommended. If you run into errors, try giving it a bit of time. If erros persist, run clean.sh.

#  Template structure

The recommended practice is to run your scripts in functions. You must always call init() from init.py so you can link your open instance of calc with your scripts.
init() returns the reference to the document which you must pass to your script functions in order to get access to methods for altering your calc spreadsheets.

#Tutorials

Setting your environment https://medium.com/analytics-vidhya/macro-programming-in-openoffice-libreoffice-with-using-python-en-a37465e9bfa5

A few tutorials:
  https://wiki.openoffice.org/wiki/Python/Transfer_from_Basic_to_Python
  https://wiki.openoffice.org/wiki/Python
  https://wiki.openoffice.org/wiki/SQLAlquemyPyUNO - for SQL
