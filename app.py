from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from datetime import datetime
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
        if connection.is_connected():
            return dbconn
        else:
            connection=None
            dbconn=None
            return getCursor()
#Define the cursor function to get the data by connecting to database and enable the connection.
def genID():
    return uuid.uuid4().fields[1] #Take out the second number of the six numbers make up of uuid.


@app.route("/", methods=['GET','POST']) #Default route - home page.
def home():
    if request.method=='POST':
        root=request.form.get('members')
        return redirect(root) 
#The root here is the variable call to get the data from the Members table and redirect to the route according to the member names.
    else:
        cur = getCursor()
        cur.execute("select MemberFirstName, MemberLastName, MemberID, AdminAccess from Members;")
        member = cur.fetchall()
        return render_template('home.html', Members=member)
#This function is return the data from Members table, execute the query through python from MySQL. Then get the data to display on Homepage.

@app.route('/member', methods=['GET','POST']) #Member page. Route/member is a name given as variable for the route on the link.
def getMembers():
    MemberID = request.args.get('MemberID')
    print(MemberID)
    cur = getCursor()
    cur.execute("select NewsHeader, NewsByline, NewsDate, News from ClubNews ORDER BY NewsDate LIMIT 3;") 
#Get data from ClubNews table, display the latest three news item by use limit.
    select_News = cur.fetchall()
    print(select_News)
    ClubNews = [desc[0] for desc in cur.description]
    cur.execute("select MemberID, MemberFirstName, MemberLastName, Address1, Address2, City, Email, Phone from Members where MemberID=%s;",(MemberID,))
#Get data from Members table and identify the member by their unique MemberID.
    member = cur.fetchall()
    Members = [desc[0] for desc in cur.description]
    print(f"{Members}")
#Display list of upcoming fixtures. Use join table method to display the game information and know whether the team from hometeam or awayteam.
    cur.execute("""select FixtureID, FixtureDate, HomeTeam, AwayTeam, HT.TeamName as HomeTeamName, AWT.TeamName as AwayTeamName from Fixtures 
                    join Teams as HT on Fixtures.HomeTeam = HT.TeamID
                    join Teams as AWT on Fixtures.AwayTeam = AWT.TeamID where FixtureDate>%s;""",(datetime.now(),))
    select_Fixture = cur.fetchall()
    Fixtures = [desc[0] for desc in cur.description]
    print(f"{Fixtures}")
    return render_template('members.html',Members=member,clubmember=Members,ClubNews=select_News,News=ClubNews,Fixtureresult=select_Fixture,fixturecolumn=Fixtures)

@app.route('/member/update', methods=['GET','POST']) #Member page
def Updatemembercontacts():
    MemberID = request.args.get('MemberID')
    if request.method == 'POST':
            MemberID = request.form.get('MemberID')
            MemberFirstName = request.form.get('MemberFirstName')
            MemberLastName = request.form.get('MemberLastName')
            Address1 = request.form.get('Address1')
            Address2 = request.form.get('Address2')
            City = request.form.get('City')
            Email  = request.form.get('Email')
            Phone = request.form.get('Phone')
            cur = getCursor()
            cur.execute("UPDATE Members SET MemberFirstName=%s, MemberLastName=%s, Address1=%s, Address2=%s, City=%s, Email=%s, Phone=%s where MemberID=%s;",
            (MemberFirstName,MemberLastName,Address1,Address2,City,Email,Phone,MemberID,))
            return redirect(url_for("getMembers", MemberID=MemberID))
#Above code allow members to update their contacts via a new page, redirect here reference to the members function.
#Update as a keyword in MySQL query to command the system update those details and Set is setting the variable name when retrieve the data from database.
    else:
        MemberID = request.args.get('MemberID')
        if MemberID == '':
            return redirect("/") #check whether they have a memberID, authenticate the member login.
        else:
            cur = getCursor()
            cur.execute("SELECT * FROM Members where MemberID=%s;",(str(MemberID),))
            select_MemberID = cur.fetchone()
            print(select_MemberID)
            return render_template('updatecontacts.html',Memberdetails=select_MemberID)
#Last bit of code getting information from the members table and get all the data from html page and set Jinja variable name when use for loop to loop over the data correctly.

@app.route('/admin', methods=['GET','POST']) #Admin page
def getAdmin():
    MemberID = request.args.get('MemberID')
    print(MemberID)
    cur = getCursor()
    cur.execute("select ClubID, NewsHeader, NewsByline, NewsDate, News from ClubNews ORDER BY NewsDate;")
    select_News = cur.fetchall()
    ClubNews = [desc[0] for desc in cur.description]
    cur.execute("select ClubID, TeamName, TeamGrade from Teams;")
    all_teams = cur.fetchall()
    tm = [desc[0] for desc in cur.description]
    return render_template('admin.html',team=all_teams,selectteam=tm,ClubNews=select_News,News=ClubNews)
#Use MemberID identify the admin access and display the News and Teams updates.
#Two MySQL queries here to select the data we want to see on the admin page.

@app.route('/admin/updatenews', methods=['GET', 'POST'])
def addnews():
    if request.method == 'POST':
        print(request.form)
        Header = request.form.get('NewsHeader')
        Author = request.form.get('NewsByline')
        Date = request.form.get('NewsDate')
        NewNews = request.form.get('News')
        cur = getCursor()
        cur.execute("insert into ClubNews(ClubID, NewsHeader, NewsByline, NewsDate, News) values (23,%s,%s,%s,%s);",(Header,Author,Date,NewNews,))
        cur.execute("select * from ClubNews;")
        MemberID = cur.fetchall()
        newscol = [desc[0] for desc in cur.description]
        return redirect(url_for('getAdmin',pickmember=MemberID,dbnew=newscol))
    else:
        return render_template('addnews.html')
#This route function allow admin to add new clubnews to the club, request is the word when upload the new data when user submit the form.
#Two MySQL queries here to get the right data and add it to the database with different set variable names at the end for calling.
#ClubID is default to 23 because that is only club admin belong to the club is able to add news to the club.
#In here use redirect to link the URL given to bring user to the right place they want to go on the page.

@app.route('/admin/clubmember', methods=['GET', 'POST'])
def viewmember():
    if request.method == 'GET':
        cur = getCursor()
        cur.execute("select * from Members;")
        memberresult = cur.fetchall()
        coldbresult = [desc[0] for desc in cur.description]
        print(f"{coldbresult}")
        return render_template('viewmember.html',dbmemberresult=memberresult,col=coldbresult)
#For admin to see all the members, whether they are active or not. GET here is to read the information, but not submitting or editing.
#Print a report of all active members can be done through the next function within the admin page.

@app.route('/admin/activemembers', methods=['GET', 'POST'])
def viewactivemember():
    if request.method == 'GET':
        cur = getCursor()
        cur.execute("select ClubID, TeamID, MemberFirstName, MemberLastName, City, Email, MembershipStatus, AdminAccess from Members where MembershipStatus=1;")
        activember = cur.fetchall()
        mber = [desc[0] for desc in cur.description]
        print(f"{mber}")
        return render_template('activemembers.html',dbactive=activember,colmber=mber)
#This page show all the active member where the previous function display all the club members whether they are active or inactive.
#This page also suitable for printing with less member details which the admin do not need to know. And the rest of the member details
#can be found in the previous function view club member page.

@app.route('/admin/clubmember/add', methods=['GET','POST'])
def addmember():
    if request.method == 'POST':
        print(request.form)
        id = genID()
        print(id)
        First_Name = request.form.get('MemberFirstName')
        Last_Name = request.form.get('MemberLastName')
        Address1 = request.form.get('Address1')
        Address2 = request.form.get('Address2')
        City = request.form.get('City')
        Email = request.form.get('Email')
        Phone = request.form.get('Phone')
        Birthdate = request.form.get('Birthdate')
        Memberstatus = request.form.get('MembershipStatus')
        Adminaccess = request.form.get('AdminAccess')
        cur = getCursor()
        cur.execute("""INSERT INTO Members(MemberID, MemberFirstName, MemberLastName, Address1, Address2, City, 
        Email, Phone, Birthdate, MembershipStatus, AdminAccess) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
        (str(id),First_Name,Last_Name,Address1,Address2,City,Email,Phone,Birthdate,Memberstatus,Adminaccess,))
        cur.execute("""SELECT MemberID, MemberFirstName, MemberLastName, Address1, Address2, City, Email, Phone, 
        Birthdate, MembershipStatus, AdminAccess FROM Members where MemberID=%s;""",(str(id),))
        select_member = cur.fetchall()
        membercol = [desc[0] for desc in cur.description]
        return render_template('viewmember.html',insertmember=select_member,mber=membercol)
    else:
        cur = getCursor()
        cur.execute("select TeamID, TeamName from Teams;")
        selectid = cur.fetchall()
        return render_template('addmember.html',team=selectid)
#Add member allow admin to add a new member with POST method when submit the form to let the system know to update the database.
#Insert and select queries here ensure all the variables are in orders for the display on the page correctly, %s is placeholder for new data insert to database.
#else condition is the GET request for a drop down menu show list of TeamID available for member to join a team.

@app.route('/admin/clubmember/update', methods=['GET', 'POST'])
def updatemember():
    if request.method == 'POST':
            memberid = request.form.get('MemberID')
            clubid = request.form.get('ClubID')
            teamid = request.form.get('TeamID')
            MemberFirstName = request.form.get('MemberFirstName')
            MemberLastName = request.form.get('MemberLastName')
            Address1 = request.form.get('Address1')
            Address2 = request.form.get('Address2')
            City = request.form.get('City')
            Email  = request.form.get('Email')
            Phone = request.form.get('Phone')
            BirthDate = request.form.get('Birthdate')
            MembershipStatus = request.form.get('MembershipStatus')
            AdminAccess = request.form.get('AdminAccess')
            cur = getCursor()
            cur.execute("""UPDATE Members SET ClubID=%s, TeamID=%s, MemberFirstName=%s, MemberLastName=%s, Address1=%s, Address2=%s, 
            City=%s, Email=%s, Phone=%s, Birthdate=%s, MembershipStatus=%s, AdminAccess=%s where MemberID=%s;""",
            (clubid,teamid,MemberFirstName,MemberLastName,Address1,Address2,City,Email,Phone,BirthDate,MembershipStatus,AdminAccess,memberid,))
            memberID = cur.fetchall()
            return redirect(url_for("viewmember",pickID=memberID))
    else:
        MemberID = request.args.get('MemberID')
        if MemberID == '':
            return redirect("/")        
        else:
            cur = getCursor()
            cur.execute("SELECT * FROM Members where MemberID=%s;",(str(MemberID),))
            memberresult = cur.fetchone()
            print(memberresult)
            return render_template('updatemember.html',memberdetails=memberresult)
#This function allow admin to update edit the existing member details use POST method allow submit the form to the system for changes made.
#Update is the keyword let the computer know update the row of data to the system and display them with the same order of the variable names after the query.
#Check the Member with valid ID, if not, bring you back to the home page.
#Get all the member details from Members table in order for admin to update the Members table data.

@app.route('/admin/newteam', methods=['GET', 'POST'])
def addnewteam():
    if request.method == 'POST':
        print(request.form)
        clubid = request.form.get('ClubID')
        teamname = request.form.get('TeamName')
        teamgrade = request.form.get('teamgrade')
        cur = getCursor()
        cur.execute("insert into Teams(ClubID, TeamName, TeamGrade) values (%s,%s,%s);",(str(clubid),teamname,str(teamgrade),))
        cur.execute("select * from Teams;")
        select_team = cur.fetchall()
        teamscol = [desc[0] for desc in cur.description]
        return redirect(url_for('getAdmin',dbteams=select_team,dbcol=teamscol))
    else:
        cur = getCursor()
        cur.execute("select ClubID, TeamGrade from Teams;")
        selectgrade = cur.fetchall()
        return render_template('newteam.html',choosegrade=selectgrade)
#This part allow admin to add new rugby team and a new opposition team for them to play the game.
#TeamID will be generated when a new team added to the system, same with the opposition team.
#Here use insert and select to add the new team data to the Teams table and get all the information from Teams table in order to do that.

@app.route('/admin/rugbygame', methods=['GET', 'POST'])
def addnewgame():
    if request.method == 'POST':
        print(request.form)
        fixturedate = request.form.get('FixtureDate')
        hometeam = request.form.get('HomeTeam')
        awayteam = request.form.get('AwayTeam')
        cur = getCursor()
        cur.execute("insert into Fixtures(FixtureDate, HomeTeam, AwayTeam) value (%s,%s,%s);",(fixturedate,hometeam,awayteam,))
        cur.execute("select * from Fixtures;") #Join table select teams join grade tables. TeamGrade and GradeID are dataset to join.
        ht = cur.fetchall()
        awyteam = [desc[0] for desc in cur.description]
        return render_template('admin.html',hoeteam=ht,awayt=awyteam)
    else:
        return render_template('newfixtures.html')

@app.route('/admin/eligibility', methods=['GET', 'POST'])
def eligibility():
    if request.method == 'GET':
        cur = getCursor()
        cur.execute("select ClubID, TeamID, MemberFirstName, MemberLastName, City, Email, MembershipStatus, AdminAccess from Members where MembershipStatus=1;")
        mberactive = cur.fetchall()
        mtive = [desc[0] for desc in cur.description]
        print(f"{mtive}")
        return render_template('eligibility.html',grade=mberactive,mg=mtive)