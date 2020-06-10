import pprint 
import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)


with app.test_request_context('/hello', method='POST'):
    # now you can do something with the request until the
    # end of the with block, such as basic assertions:
    assert request.path == '/hello'
    assert request.method == 'POST'

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
 #   processed_text = text.upper()
  #  return processed_text 
    return text

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  passwd="test",
  database="mydatabase" ) 

mycursor = mydb.cursor() 
sql = "SHOW DATABASES LIKE "
userinput = my_form_post()
#userinput = "'m%'"
sql = sql + userinput

mycursor.execute(sql)

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
