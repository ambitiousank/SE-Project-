import time
import os
import sys
import fileinput
from subprocess import call

## yyyy-mm-dd format
created_on= time.strftime("%Y-%m-%d")
BASE_DIR=os.path.dirname(os.path.abspath(__file__))
textToSearch =  "date_now"

print ("Text to replace it with:")
textToReplace = "\""+created_on+"\""

print ("File to perform Search-Replace on:")
fileToSearch  = BASE_DIR+"/db_template"
fileToSave    = BASE_DIR+"/initial_db.json"
#fileToSearch = 'D:\dummy1.txt'

tempFile = open( fileToSave, 'w+' )

for line in fileinput.input( fileToSearch ):
    tempFile.write( line.replace( textToSearch, textToReplace ) )
tempFile.close()
call(["python", "manage.py", "loaddata", fileToSave])