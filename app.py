from flask import Flask, render_template ,request, redirect
import sqlite3 as db
# DataBase Connection
conn = db.connect('database.db')
# print ("Opened database successfully")

# conn.execute('CREATE TABLE todo (Title TEXT, Task TEXT, Date date)')
# print ("Table created successfully")

# conn.close()



# Server
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('file1.html')

@app.route('/home')
def home():
    return redirect('/')

@app.route('/about')
def about():
    return 'This Page Under Processig...'

@app.route('/contact')
def contact():
    return 'This Page Under Prosession...'

@app.route('/form_submit', methods=['POST'])
def form_submit():
    if request.method == 'POST':
        given_title = request.form['inp_title']
        given_task = request.form['inp_task']
        given_date = request.form['inp_date']
        print(f"Title is {given_title}, task is {given_task}, and date is {given_date}")
        conn.execute("INSERT INTO todo (Title,Task,Date) VALUES (?,?,?)",(given_title,given_task,given_date) )
        conn.commit()
        # thread = threading.Thread(target=database_operation, args=(given_title, given_task, given_date))
        # thread.start()
        # thread.join()
        return redirect('/') 

    else:
        return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)