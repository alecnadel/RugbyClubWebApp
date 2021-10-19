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
#define the cursor action to get the data by connecting to database and enable the connection.
def genID():
    return uuid.uuid4().fields[1] #Take out the second number of the six numbers make up of uuid.


@app.route("/", methods=['GET','POST']) #Default route - home page.
def home():
    if request.method=='POST':
        root=request.form.get('members')
        return redirect(root) #root here is the variable call to get the data from the Members table and redirect to the route.
    else:
        cur = getCursor()
        cur.execute("select MemberFirstName, MemberLastName, MemberID, AdminAccess from Members")
        member = cur.fetchall()
        return render_template('home.html', Members=member)
#this function is return the data from Members table, execute the query through python from MySQL. Then get the data to display on Homepage.

@app.route('/member', methods=['GET','POST']) #Member page/member is a name given as variable for the route on the link.
def getMembers():
    MemberID = request.args.get("MemberID")
    print(MemberID)
    cur = getCursor()
    cur.execute("select NewsHeader, NewsByline, NewsDate, News from ClubNews ORDER BY NewsDate LIMIT 3") #get data from ClubNews table, display the latest three news item.
    select_News = cur.fetchall()
    print(select_News)
    ClubNews = [desc[0] for desc in cur.description]
    cur.execute("select MemberID, MemberFirstName, MemberLastName, Address1, Address2, City, Email, Phone from Members where MemberID=%s",(MemberID,))
    #get data from Members table and identify the member by their unique MemberID.
    member = cur.fetchall()
    Members = [desc[0] for desc in cur.description]
    print(f"{Members}")
    #display list of upcoming fixtures. Use join table method to display the game information join in either hometeam or awayteam.
    cur.execute("select FixtureID, FixtureDate, HomeTeam, AwayTeam from Fixtures join Members on Fixtures.HomeTeam = Members.TeamID where FixtureDate > '2021-10-22 19:30:00'")
    select_Fixture = cur.fetchall()
    Fixtures = [desc[0] for desc in cur.description]
    print(f"{Fixtures}")
    return render_template('members.html',Members=member,clubmember=Members,ClubNews=select_News,News=ClubNews,Fixtureresult=select_Fixture,fixturecolumn=Fixtures)

@app.route('/member/update', methods=['GET','POST']) #Member page
def Updatemembercontacts():
    if request.method == 'POST':
            MemberFirstName = request.form.get('MemberFirstName')
            MemberLastName = request.form.get('MemberLastName')
            Address1 = request.form.get('Address1')
            Address2 = request.form.get('Address2')
            City = request.form.get('City')
            Email  = request.form.get('Email')
            Phone = request.form.get('Phone')
            cur = getCursor()
            cur.execute("UPDATE Members SET MemberFirstName=%s, MemberLastName=%s, Address1=%s, Address2=%s, City=%s, Email=%s, Phone=%s where MemberID=%s",(MemberFirstName,MemberLastName,Address1,Address2,City,Email,str(Phone),))
            return redirect("/")
    else:
        MemberID = request.args.get('MemberID')
        if MemberID == '':
            return redirect("/") #check whether they have a memberID.
        else:
            cur = getCursor()
            cur.execute("SELECT * FROM Members where MemberID=%s",(str(MemberID),))
            select_MemberID = cur.fetchone()
            print(select_MemberID)
            return render_template('updatecontacts.html',Memberdetails = select_MemberID)

@app.route('/admin', methods=['GET','POST']) #Admin page
def getAdmin():
    MemberID = request.args.get("MemberID")
    print(MemberID)
    cur = getCursor()
    cur.execute("select MemberID, MemberFirstName, MemberLastName, Address1, Address2, City, Email, Phone from Members where MemberID=%s",(MemberID,))
    select_admin = cur.fetchall()
    admin = [desc[0] for desc in cur.description]
    print(f"{admin}")
    return render_template('admin.html',admin=select_admin)


