import uno  # libreoffice's API
import os,sys
sys.path.insert(1, os.path.join(sys.path[0], '..')) # gets parent folder reference to import init.py
from init import init


def template(document):
    # access the active sheet
    active_sheet = document.CurrentController.ActiveSheet

    # access cell C4
    cell1 = active_sheet.getCellRangeByName("C4")

    # set text inside
    cell1.String = "Hello world"

document = init()
template(init())