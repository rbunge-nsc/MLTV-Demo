from flask import Flask, request, render_template
import  mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="test",
  passwd="test",
  database="MLTV" )

mycursor = mydb.cursor()

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

#the query returns a tuple. It must be converted to a list of strings. Then you can append to the list.
for x in mycursor:
   x=convertTuple(x)
   output.append(x)

outputStr =  convertTuple(listToString(output))

def get_db_info(query):
   mycursor.execute(query)
   for x in mycursor:
      x=convertTuple(x)
      output.append(x)
   outputStr = convertTuple(listToString(output))
  # return outputStr
   return output

#output section - using Flask
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('MLTVForm.html')

@app.route('/', methods=['POST'])
def my_form_post():
#    text = request.form['text']
    text = request.form['courses']
    query = "SELECT coursenum, coursename, courseurl FROM ITCourses WHERE coursenum = '"
    query = query + text + "';"
    mycursor.execute(query)
    records = mycursor.fetchall()
    return "More information about </br></br> " +  text + "  " + records[0][1] + "</br></br>can be found at: <a href=\"https://mltv.s3.amazonaws.com/" + text + "/" + records[0][2] +"\">" + records[0][2]+"</a>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')
