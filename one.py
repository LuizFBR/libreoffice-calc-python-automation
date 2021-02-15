import socket  # only needed on win32-OOo3.0.0
import uno

# get the uno component context from the PyUNO runtime
localContext = uno.getComponentContext()
# create the UnoUrlResolver
resolver = localContext.ServiceManager.createInstanceWithContext(
                "com.sun.star.bridge.UnoUrlResolver", localContext )
# connect to the running office
ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
smgr = ctx.ServiceManager
# get the central desktop object
desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",ctx)
# access the current writer document
document = desktop.getCurrentComponent()

# access the active sheet
active_sheet = document.CurrentController.ActiveSheet

# access cell C4
cell1 = active_sheet.getCellRangeByName("C4")

# set text inside
cell1.String = "Hello world"