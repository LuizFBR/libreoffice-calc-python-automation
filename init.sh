#!/bin/bash
# Source: https://medium.com/analytics-vidhya/macro-programming-in-openoffice-libreoffice-with-using-python-en-a37465e9bfa5
soffice --calc --accept="socket,host=localhost,port=2002;urp;StarOffice.ServiceManager" & # & leaves the process running in the background