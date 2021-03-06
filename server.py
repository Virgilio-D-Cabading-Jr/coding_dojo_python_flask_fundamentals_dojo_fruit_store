import datetime
from flask import Flask, render_template, request, redirect, session
from werkzeug.datastructures import RequestCacheControl

app = Flask(__name__)
app.secret_key = "TiYSKDNRitA!"                                                     # This is Your Secret Key Do Not Reveal it to Anyone!

@app.route('/')                                                                     # Main Page
def index():
    return render_template("index.html")

@app.route('/post_checkout', methods=['POST'])                                      # Page to handle data from submitting the checkout form
def post_checkout():
    print(request.form)
    # session['strawberry_num'] = request.form['strawberry']                          # Retrieve variables from the form
    # session['raspberry_num'] = request.form['raspberry']                            #     and store the vars as in a session
    # session['apple_num'] = request.form['apple']
    # session['first_name'] = request.form['first_name']
    # session['last_name'] = request.form['last_name']
    # session['student_id'] = request.form['student_id']
    session['fruit_store'] = {
        **request.form
    }
    return redirect ("/checkout")
    

@app.route('/checkout')                                                             # Page for showing the checkout info
def checkout():
    current_date_time = datetime.datetime.now()
    total_num_ordered = int(session['fruit_store']['strawberry']) + int(session['fruit_store']['raspberry']) + int(session['fruit_store']['apple'])

    return render_template("checkout.html", total_num_ordered= total_num_ordered, current_date_time= current_date_time)

@app.route('/fruits')                                                               # display the fruit pictures
def fruits():
    return render_template("fruits.html")

if __name__=="__main__":   
    app.run(debug=True)    