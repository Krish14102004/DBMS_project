from flask import Flask, render_template, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'universitymanagementsystem'

mysql = MySQL(app)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/students')
def get_students():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM studentinfo")  # use your view
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]
    data = [dict(zip(columns, row)) for row in rows]
    return jsonify(data)

@app.route('/api/faculty')
def get_faculty():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM facultyinfo")
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]
    data = [dict(zip(columns, row)) for row in rows]
    return jsonify(data)

@app.route('/api/hostels')
def get_hostels():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM hosteloccupancy")
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]
    data = [dict(zip(columns, row)) for row in rows]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
