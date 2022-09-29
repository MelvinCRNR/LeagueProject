from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = "flash message"

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Mysql2022'
app.config['MYSQL_DB'] = 'LolBase'

mysql = MySQL(app)


@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM champions_stats")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html', champions_stats=data)


@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        flash("Data Inserted Succesfully")

        Champions = request.form['Champions']
        EB_price = request.form['EB_price']
        RP_price = request.form['RP_price']
        Release_date = request.form['Release_date']
        Attributes = request.form['Attributes']

        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO champions_stats(Champions, EB_price, RP_price, Release_date, Attributes) VALUES (%s, %s, %s, "
            "%s, %s)",
            (Champions, EB_price, RP_price, Release_date, Attributes))
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/delete/<string:id_data>', methods=['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM champions_stats WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))


@app.route('/update', methods=['POST', 'GET'])
def update():
    if request.method == 'POST':
        Champions = request.form['Champions']
        EB_price = request.form['EB_price']
        RP_price = request.form['RP_price']
        Release_date = request.form['Release_date']
        Attributes = request.form['Attributes']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE champions_stats
               SET EB_price=%s, RP_price=%s, Release_date=%s, Attributes=%s
               WHERE Champions=%s 
            """, (Champions, EB_price, RP_price, Release_date, Attributes))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))


if __name__ == "__main__":
    app.run(debug=True)
