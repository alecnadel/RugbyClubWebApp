# RugbyClubWebApp Project Documentation
#Code in HTML, CSS(bootstrap) Python(Flask) and MySQL(database) to store and allow users to add data.

This project is building a webpage with the required functionalities for rugby clubs.
The rugby club web app has several functions on the page and back-end login for club admin access.
It has two parts of the login interface. Standard club member and club admin. Club admin has all the member features plus
other admin-only features when they login to their dashboard.
Standard members select their member’s name (first and last name) in the drop-down menu of the home page, and then click
log in to see their dashboard.
Same login process with the club admin, when they select their name, the system recognises whether they are club admin or not
through the unique member id, the database assigns it to them. 

Standard member can see their member details, the three latest club news announcements and the upcoming fixtures if they are
part of a team. The fixture shows the rugby game information of which team is playing against another team. It shows the date
when the game will be played, the system assigned fixture id identify the uniqueness of that game and the home team and away team names.

Club admin also a club member has all the member features plus add a new member to the club, edit existing member details, re-activate
or de-activate a member for their club membership, add new club news, add a new team, add a new opposition team, add new fixture,
assign a member to a team and view all active members to check whether a member that is in a team 
that they are eligible to play the game or not from the date they entered based on their age.

Above are the high-level overview of what the web app is capable of and the features from two login interfaces, member, and admin.
I have structured my web app across multiple functions and app routes. My goal is to make the app minimalistic, easy to navigate and 
with white background colour throughout the pages.
The first function which connects to the home page is a default page with '/' in the app route to use GET and POST methods allow the member
to select the option and log in to their dashboard. I created the function with POST method use if condition statement and return statement else would be
the GET request to read the member details from the database. 

My assumption was getting the return data from the database display on the login page which did not happen when I have a missing variable in the return statement.
The design of the page was the heading text-centre with the submit button as login in blue to give it a nice contrasting colour to the rest of the page.
The design decision is made based on simple to use and simple solutions and make it work rather than make it pretty. Minimal but still does the job and look
professional. The validity of this function is making the variable match with the Jinja template language and calling the variable name correctly from the Html template.
When a user executes the use of the system, it does what the function intends to do which bring the user in this case, the club member to their dashboard with their
name and correct details.

In the next part, my code function structure covered returning the data from the member's table which show all the correct member details when they log in. Also,
it included how the member can update their contacts in their account.
I give it a route as /member to link the function to the members Html template were read the information as a form. In this function, I used multiple 
executions to draw data from different tables in the database to return the club news data and fixtures data. The tricky part was thinking about how to display 
two different teams with different team names to match them with future games. I assume using a join table method to make the teams join the fixtures table
and the relationship between the two tables were the home team and away team match the team id. It was an assumption made before drawing out the function and 
executing the query to test whether it will display the way I want for the upcoming fixtures.

With the update member contact function, it uses two if condition statements and return with a different app route which brings you to a new page for the form.
I put the update contacts button in the same table as member details which are more related and look cleaner on the page, also for the user (member) when checking
their details can easily know where to update their contacts.
The first else condition is to check if the member has a valid id or not, assume they have, else it will bring the user back to the front page. Assuming this function
was part of the authentication for the member login and proof they are a member.
The second part of the condition statement also connects to the previous if statement to read out the data through getting requests. When the user submits the form 
update the contacts it will bring them back to their member page and they will see the changes made because of the GET request here read the data out 
from the database table.

For the club admin, I made the code structure and functions according to how I wanted to present it on the browser page. 
Starting with the main function of the admin, it connects to the admin Html template where the club admin recognised from their member id give it a unique value
and check if they have admin access. I assume the validity of the function to define the capability of an admin within the system which is a key page that connects
with other functions. For the layout of the admin page, I have decided to make it to one side and move to the centre a bit 
with all the buttons having a space between them and with a line of space for each element. 
Also, give it a colourful design of the buttons to have a great contrast to the white background. It is easy for the admin to select which function they like to go in.

The other parts of the admin functions where I thought that would be the natural flow of a webpage.
Club admin page function followed by add news item function and members lists displays on the page. 
The route with add news function return with the name adds news Html template where it has all the key dataset for admin to add a new news item.
I assume the news use a text area to make the input box larger when getting the news, it can display clearly and edit any mistake easily before post to the club.
The design element again here is to make it simple, use fewer colours with mainly the layout and structure of input fields. 
The redirect route brings the user back to the admin page and they can see the new news item is added. 
The view member, add member and update member within the admin page are interrelated as you see their app routes with '/' that is similar.
Add member and update member are the sub-route of view member as they are part of the same page which extended from view member.
The design logic is also clear that using a light-yellow border with white background create a hint of simplicity and is easy to read. 
The update member function has a similar code structure to the member update contacts as my assumption was both are being updated and both updating
data from the database use UPDATE as the keyword for the MySQL query in python function and redirect it back to the view member page to see the changes made
once the update command is executed.

My assumption with the view member page also combined with the report all active members page as thinking when the admin adds a new member or update a member 
can update their membership status. Through that route, it can display all the active members If the club admin set all members to active in the form set.
Return to the admin page and refresh, then go back to the view club member page to see all the active members print if needed.
But in reality, I made some changes to the view all active members as from the assumption. I create a new button and associated app route
to show directly all the active members only will show on that page. And making sure the format of the page is printing friendly use portrait or landscape.
An assumption made here also take the design decision and page structure into consideration with fewer pages and one less function to write, 
making it easier to integrate with the two. I would assume that does the job and is still easy to use for the user to get around the page between 
view members(active or inactive), add members and update member details and view all active members from the club admin functions.

The next function adds a new team also linked to the admin page as the app route suggested along with the add new fixtures. As those app routes put the route function
design logic in mind. Part of the admin page extends to another page and once the information is either updated or add to the existing database then bring the user
back to the default page which is the admin page. 
It renders the template making the connection to their Html template to receive any data as I used Jinja templating language to get the variable name from python.
With the added new fixture, my assumption was separated into two pages, home team fixture and away team fixture. But in the end, I decided to combine it as add new fixture
with one button access and admin can select all the team names from the drop down menu in the hometeam or awayteam, vice versa. 
But bear in mind as club admin should see the new fixture should not be the same team playing and the team you selected must be the same grade.
Which admin can see in the team name selection next to the team name it says the grade name of the team. 
For example: junior, senior or under 18s or Master. 

Lastly, same as the rest of the admin function, grade eligibility checks if a member is eligible to play in a game from the team based on the date they entered.
The function also has a similar app route which is the child page of the admin page. The variable names are given meaning to both python and Jinja template 
in Html as Jinja call out the data pass through python and MySQL query. 
Again, with the design element to the page, for simplicity and user friendly, I choose the white background for consistency and keep all the input field 
on the left with a minimalist design idea in mind to make the page look tidy but not boring. 

Overall, the web app builds around a simple solution principle and user friendly in mind but does not focus on making it look elegant or pretty in any shape or form.
Most assumptions and design elements take simplicity into consideration and the sound structure of the page. With different app routes well connected and python functions
interconnect with MySQL queries and execute the queries to add or update the data on the user command.




