from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)

# @app.route('/')
@app.route('/hello')
def hello_world():
    # return 'Hello, Rohit!'
    # print(url_for('static', filename='icon.png')) # /static/icon.png
    return render_template('indexold.html')

# @app.route('/<username>')
# def hello_1(username = None):
#     return render_template('indexold.html', name = username) # to run use {{name}} in html body

@app.route('/blog')
def blog():
    return 'Hello, It\'s an app'




# for website

@app.route('/')
def my_home():
    return render_template('index.html')

# @app.route('/about.html')
# def about():
#     return render_template('about.html')

# @app.route('/works.html')
# def work():
#     return render_template('works.html')

# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html') # Instead of above 3 to avoid DRY. use this below variable rules method


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
    with open('database.csv', mode='a',newline='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar = '"',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])

@app.route('/submit_form', methods=['POST', 'GET']) # for Contacts Page
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            # print(data)
            # write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to Database'
    else:
        return 'Something Went Wrong. Try Again!!'

