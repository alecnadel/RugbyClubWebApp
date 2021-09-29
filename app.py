from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
import mysql.connector
import connect
import uuid
connection = None
dbconn = None

app = Flask(__name__)

def getCursor():
    global dbconn
    global connection
    if dbconn == None:
        connection = mysql.connector.connect(user=connect.dbuser, \
        password=connect.dbpass, host=connect.dbhost, \
        database=connect.dbname, autocommit=True)
        dbconn = connection.cursor()
        return dbconn
    else:
        return dbconn

def genID():
    return uuid.uuid4().fields[1]


@app.route("/")
def home():
    cur = getCursor()
    cur.execute("select id, company, last_name from customers;")
    select_result = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    print(f"{column_names}")
    return render_template('customerresult.html',dbresult=select_result,dbcols=column_names)

@app.route('/order', methods=['GET'])
def getOrder():
    print(request.args)
    orderid = request.args.get("orderid")
    print(orderid)
    cur = getCursor()
    cur.execute("select * from orders where customer_id=%s",(orderid,))
    select_result = cur.fetchall()
    column_names = [desc[0] for desc in cur.description]
    print(f"{column_names}")
    return render_template('dbresult.html',dbresult=select_result,dbcols=column_names)


@app.route('/customer', methods=['GET','POST'])
def customer():
    if request.method == 'POST':
        print(request.form)
        id = genID()
        print(id)
        company = request.form.get('companyname')
        contact = request.form.get('contactname')
        cur = getCursor()
        cur.execute("INSERT INTO customers(customer_id, company_name, contact_name) VALUES (%s,%s,%s);",(str(id),company,contact,))
        cur.execute("SELECT * FROM customers where customer_id=%s",(str(id),))
        select_result = cur.fetchall()
        column_names = [desc[0] for desc in cur.description]
        return render_template('dbresult.html',dbresult=select_result,dbcols=column_names)
    else:
        return render_template('customerform.html')

@app.route('/customer/update', methods=['GET','POST'])
def customerUpdate():
    if request.method == 'POST':
            companyid = request.form.get('companyid')
            companyname = request.form.get('companyname')
            contactname = request.form.get('contactname')
            cur = getCursor()
            cur.execute("UPDATE customers SET company=%s, last_name=%s where id=%s",(companyname,contactname,str(companyid),))
            return redirect("/")
    else:
        id = request.args.get('customerid')
        if id == '':
            return redirect("/")
        else:
            cur = getCursor()
            cur.execute("SELECT * FROM customers where id=%s",(str(id),))
            select_result = cur.fetchone()
            print(select_result)
            return render_template('customerform.html',customerdetails = select_result)






