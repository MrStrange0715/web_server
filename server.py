from flask import Flask, render_template, url_for, request, redirect
import csv

#render_template module helps us send our html file to the server

'''
app = Flask(__name__)
print(__name__) #prints out main as this is the main file that we are running


#@app.route() decorator runs the function if the parameter within the decorator is present in the url
#@app.route("/")
#def hello_world():
#    return "<p>HELLO???</p>"

@app.route('/')
def hello_world():
    return render_template('./index.html') #./ indicates current directory
#here, when render_template function is called, flask searches folder named templates and returns an error if theres no folder named templates. so we crate a folder templates and move the html file into it


@app.route('/about.html')
def about():
    return render_template('./about.html')

@app.route("/blog")
def blog():
    return "<p>These are my thots on blogs</p>"

@app.route("/blog/2020/dogs")
def blog2():
    return "<p>You are a dog!! lel!!</p>"

#css and javascript files are called static files as they never change
#so we create a static folder so that flask searches tht folder for css and js
'''

'''
app = Flask(__name__)


#using this func we can read the url and pass the data
@app.route('/<username>')
def hello_world2(username=None):
    #print(url_for('static', filename='bolt.ico')) #prints the actual url of bolt.ico file
    return render_template('./index.html', name=username)


@app.route('/<username>/<int:post_id>') #<int:post_id> means post_id should only be int
def hello_world(username=None, post_id=None):
    #print(url_for('static', filename='bolt.ico')) #prints the actual url of bolt.ico file
    return render_template('./index2.html', name=username, post_id=post_id)

@app.route('/about.html')
def about():
    return render_template('./about.html')


#favicon.ico refers to the image of website in the tab buttons
#A “favicon” is an icon used by browsers for tabs and bookmarks
'''

'''app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/works.html')
def work():
    return render_template('./works.html')

@app.route('/about.html')
def about():
    return render_template('./about.html')

@app.route('/contact.html')
def contact():
    return render_template('./contact.html')'''

#we should type ./static bfre assests, main(i.e css & js files) as we moved them to static folder

'''
app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET']) #this endpont will be able to accept methods post & get
def submit_form():
    return 'Form Submitted yay!'
#to calll this func on the front end of the browser, we make small changes in the contact.html
#i.e,<form action="submit_form" method="post" class="reveal-content">, we type submit_form in the action and post in method 

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict() #turning form data into dictionary
        print(data)
        #return'Form submitted'
        return redirect('/thankyou.html')
    else:
        return 'Oops...Something went wrong...Try again!'
'''

app = Flask(__name__)
print(__name__)

@app.route('/')
def home():
    return render_template('./index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

#CSV - comma separated values.. comma indicates new column
#def write_to_csv(data):
  #with open('database.csv', mode='a') as database2:
    #email = data["email"]
    #subject = data["subject"]
    #message = data["message"]
    #csv_writer = csv.writer(database2, delimiter=',', quotechar='"', newline='', quoting=csv.QUOTE_MINIMAL) #delimiter indicates by which value the columns are separated
    #csv_writer.writerow([email,subject,message])
    

def write_to_csv(data):
  with open('database.csv', newline='', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict() #turning form data into dictionary
            #print(data)
            #write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Oops...Did not save to database...Try again!'
    else:
        return 'Oops...Something went wrong...Try again!'




'''app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
  with open('database.txt', mode='a') as database:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
  with open('database.csv', newline='', mode='a') as database2:
    email = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
      try:
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankyou.html')
      except:
        return 'did not save to database'
    else:
      return 'something went wrong. Try again!'''