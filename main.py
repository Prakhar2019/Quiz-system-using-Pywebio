from pywebio.input import *
from pywebio.output import *
from flask import Flask
from pywebio.platform.flask import webio_view
from pywebio import STATIC_PATH
from pywebio.session import *

app = Flask(__name__)


def exam():
        
    c = 0
  
    put_html("<h1>Quiz</h1>")

    name = input("Please enter your name to start the test", type ="text", validate = validate_name)


    q1 = radio("Q1. Why do we need biological neural networks?",['to solve tasks like machine vision & natural language processing','to apply heuristic search methods to find solutions of problem','to make smart human interactive & user friendly system','all of the mentioned'])
    if q1 =='all of the mentioned':
        c+=1

    q2 = radio("Q2. What is unsupervised learning?",['features of group explicitly stated','number of groups may be known','neither feature & nor number of groups is known','none of the mentioned'])
    if q2 =='neither feature & nor number of groups is known':
        c+=1

    q3 = radio("Q3.What is an operating system?",['interface between the hardware and application programs','collection of programs that manages hardware resources','system service provider to the application programs','all of the mentioned'])
    if q3 =='all of the mentioned':
        c+=1

    q4 = radio("Q4. functions that is used to get th length of string in Python",['count()','length()','dis()','len()'])
    if q4 == 'len()':
        c+=1
    q5 = radio("Q5. Which is not a web framework",['Django','React','Numpy','Angular'])
    if q5 == 'Numpy':
        c+=1
    q6 = radio("Q6. CPU scheduling is the basis of ___________",['multiprogramming operating systems','larger memory sized systems','multiprocessor systems','none of the mentioned'])
    if q6 == 'multiprogramming operating systems':
        c+=1
    q7 = radio("Q7. If a process fails, most operating system write the error information to a ______",['new file','another running process','log file','none of the mentioned'])
    if q7 == 'log file':
        c+=1
    q8 = radio("Q8. What is the full form of DBMS?",['Data of Binary Management System','Database Management System','Database Management Service','Data Backup Management System'])
    if q8 == 'Database Management System':
        c+=1
    q9 = radio("Q9. What is DBMS?",['DBMS is a collection of queries','DBMS is a high-level language','DBMS is a programming language','DBMS stores, modifies and retrieves data'])
    if q9 == 'DBMS stores, modifies and retrieves data':
        c+=1
    q10 = radio("Q10.  Which memory device is generally made of semiconductors?",['Hard-disk','Floppy disk','Cd disk','RAM'])
    if q10 == 'RAM':
        c+=1

    if c>6:
    	message = [style(put_html("<h1 style='display:inline;border-bottom:0px'>Congratulations !! </h1>"+ name + ", your score is <b>"+ str(c) + "</b><br><br>") ,'color:green;'),style(put_html("<p>Result : <b>PASSED</b></p>"),'color:green'), put_html("<b>Thank You for your participation.</b>")]
    	popup("Result", content=message, size='large', implicit_close=True, closable=True)
    else:
    	message = [style(put_html("<h1 style='display:inline;border-bottom:0px'>Oops! " + "</h1>" + name + ", your score is <b>"+ str(c) + "</b><br><br>"),'color:red'), style(put_html("<p>Result : <b>FAILED</b></p>"), 'color:red') , put_html("<b>Thank You for your participation.</b><br><br>"), style(put_link('Retry ↺',""), 'color:red;align-content: center;border-radius: 5px;color:#f9faf8;padding: 5px 100px;text-align:center;align-items : center;background-color: white;\
            background-image: linear-gradient(270deg, #8cf5f5 1%, #0a43f3 100%);')]
    	popup("Result", content=message, size='large', implicit_close=True, closable=True)
"""A method to validate the name entered by user"""
def validate_name(name):
	#removing all spaces from the input name
	name = name.replace(" ","")
	#performing validation checks
	#check 1 : Name must not be empty
	#check 2 : It should contain only alphabets [a-z] or [A-Z]
	if(name == "" or not(name.isalpha())):
		return("Please enter a non empty name consisting of alphabets only")



app.add_url_rule('/','webio_view',webio_view(exam),methods=['GET','POST','OPTIONS'])

if __name__ == '__main__':
    app.run(debug=True, port= 5000)
