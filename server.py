from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)

#@app.route("/<username>/<int:post_id>")
#def hello_world(username=None, post_id=None):
 #   #print(url_for('static', filename='ad.ico'))  
  #  return render_template('index.html', name=username, post_id=post_id)

@app.route("/index.html")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>') #with this syntax it can dynamically accept different url parameters
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'\n{email},{subject},{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writter = csv.writer(database2, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writter.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    #error = None
    if request.method == 'POST':
        try:
          data = request.form.to_dict()
          write_to_csv(data)
          return redirect('/thankyou.html')
        except:
          return 'did not save to database'
    else:
        return 'Something went wrong. Try again.'
    #    if valid_login(request.form['username'],
    #                  request.form['password']):
    #        return log_the_user_in(request.form['username'])
    #    else:
    #        error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    #return render_template('login.html', error=error)    
        

#@app.route("/about.html")
#def about():
#    return render_template('about.html')

#@app.route("/contact.html")
#def contact():
#    return render_template('contact.html')    

#@app.route("/favicon.ico")
#def blog():
#    return "Blogs suck"    

