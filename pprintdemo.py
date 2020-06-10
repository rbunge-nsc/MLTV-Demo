import pprint
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  passwd="test",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

# output = "test"
output = []

# for x in mycursor:
#    output.append(x)

def convertTuple(tup): 
    str =  ''.join(tup) 
    return str

def listToString(s):  
    
    # initialize an empty string 
    str1 = " " 
    
    # return string   
    return (str1.join(s)) 

for x in mycursor:
   x=convertTuple(x) 
   output.append(x)


# outputStr = convertTuple(output)
outputStr =  convertTuple(listToString(output))

def handler(environ, start_fn):
    start_fn('200 OK', [('Content-Type', 'text/plain')])
#    return ["Hello World!\n" + outputStr]
#    return [outputStr]
    return[outputStr.encode('utf-8')]

def log_environ(handler):
    def _inner(environ, start_fn):
        pprint.pprint(environ)
        return handler(environ, start_fn)
    return _inner


app = log_environ(handler)
