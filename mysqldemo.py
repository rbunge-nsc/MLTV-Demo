import pprint 
import mysql.connector 

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  passwd="test",
  database="mydatabase" ) 

mycursor = mydb.cursor() 

mycursor.execute("SHOW DATABASES")

#initialize a list for the output
output = []

# converts tuple to string
def convertTuple(tup):
    str = ''.join(tup)
    return str

# converts a list to a string
def listToString(s):
    # initialize an empty string
    str1 = " "
    # return string
    return (str1.join(s))

#the query returns a tuple. It must be converted to a list of strings. Then you can append to the 
#list.
for x in mycursor:
   x=convertTuple(x)
   output.append(x) 

outputStr = convertTuple(listToString(output))

def handler(environ, start_fn):
    start_fn('200 OK', [('Content-Type', 'text/plain')])
    return[outputStr.encode('utf-8')] 

def log_environ(handler):
    def _inner(environ, start_fn):
        pprint.pprint(environ)
        return handler(environ, start_fn)
    return _inner 

app = log_environ(handler)
