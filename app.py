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


@app.route("/") #Default route - home page.
def home():
    return render_template('home.html')

@app.route('/clubnews', methods=['GET']) #Member page
def getNews():
    cur = getCursor()
    cur.execute("select NewsHeader, NewsByline, NewsDate, News from ClubNews ORDER BY NewsDate LIMIT 3")
    select_News = cur.fetchall()
    ClubNews = [desc[0] for desc in cur.description]
    print(f"{ClubNews}")
    return render_template('members.html',ClubNews=select_News,News=ClubNews)

@app.route('/members', methods=['GET','POST']) #Member page
def getMembers():
    MemberID = request.args.get("MemberID")
    print(MemberID)
    if MemberID == '':
        return redirect("members.html")
    else:
        cur = getCursor()
        cur.execute("select * from Members where MemberID=%s",(MemberID,)) #not need code out the data from database. Use a for loop from Jinja template.
        member = cur.fetchall() # in the GET video Stu said it is okay to use fetchone to get a list with parameter??
        Members = [desc[0] for desc in cur.description]
        print(f"{Members}")
        return render_template('members.html',Members=member,clubmember=Members)

@app.route('/admin', methods=['GET','POST']) #Admin page
def getAdmin():
    MemberID = request.args.get("MemberID")
    print(MemberID)
    if MemberID == '':
        return redirect("admin.html")
    else:
        cur = getCursor()
        cur.execute("select * from Members where MemberID=%s",(MemberID,))
        select_admin = cur.fetchall()
        admin = [desc[0] for desc in cur.description]
        print(f"{admin}")
        return render_template('admin.html',Members=select_admin)

@app.route('/fixtures', methods=['GET','POST'])
def getFixtures():
    cur = getCursor()
    cur.execute("select HomeTeam from Fixtures join Members on Fixtures.HomeTeam = Members.TeamID where FixturesID=[1] and [3]")
    cur.execute("select HomeTeam from Fixtures join Teams on Fixtures.HomeTeam = Teams.TeamID where TeamID=[1] and [3]")
    cur.execute("select TeamID from Teams join Fixtures on Teams.TeamID = Fixtures.AwayTeam")
    select_Fixture = cur.fetchall()
    Fixtures = [desc[0] for desc in cur.description]
    print(f"{Fixtures}")
    return render_template('members.html',Fixtures=select_Fixture,dbfixtures=Fixtures)

@app.route('/members/update', methods=['GET','POST']) #Member page
def MembersUpdate():
    if request.method == 'POST':
            Email  = request.form.get('Email')
            Phone = request.form.get('Phone')
            Address1 = request.form.get('Address1')
            Address2 = request.form.get('Address2')
            cur = getCursor()
            cur.execute("UPDATE Members SET Email=%s, Address1=%s, Address2=%s, Phone=%s, where id=%s",(Email,Address1,Address2,str(Phone)))
            return redirect("/")
    else:
        MemberID = request.args.get('MemberID')
        if MemberID == '':
            return redirect("/")
        else:
            cur = getCursor()
            cur.execute("SELECT * FROM Members where MemberID=%s",(str(MemberID),))
            select_MemberID = cur.fetchone()
            print(select_MemberID)
            return render_template('members.html',Members = select_MemberID)

#@app.route('/customer', methods=['GET','POST'])
#def customer():
    #if request.method == 'POST':
        #print(request.form)
        #id = genID()
        #print(id)
        #company = request.form.get('companyname')
        #contact = request.form.get('contactname')
        #cur = getCursor()
        #cur.execute("INSERT INTO customers(customer_id, company_name, contact_name) VALUES (%s,%s,%s);",(str(id),company,contact,))
        #cur.execute("SELECT * FROM customers where customer_id=%s",(str(id),))
        #select_result = cur.fetchall()
        #column_names = [desc[0] for desc in cur.description]
        #return render_template('dbresult.html',dbresult=select_result,dbcols=column_names)
    #else:
        #return render_template('customerform.html')



