# RugbyClubWebApp Project Documentation
#Code in HTML, CSS(bootstrap) Python(Flask) and MySQL(database) to store and allow users to add data.

This project is building a webpage with required functionalities for rugby clubs.
The rugby club webapp have several functions on the page and back-end login for club admin access.
It has two parts of login interface. Standard club member and club admin. Club admin has all the member features plus
other admin only features when they login to their dashboard.
Standard member select their member name(first and last name) in the drop down menu of the home page, and then click
login to see their dashboard.
Same login process with the club admin, when they select their name, the system recognise whether they are club admin or not
through the unique member id the database assign it to them. 

Standard member can see their member details, the three lastest club news announcements and the upcoming fixtures if they are
part of a team. The fixture show the rugby game information of which team is playing against another team. It shows the date
when the game will be play, system assigned fixture id identify the uniqueness of that game and the home team and away team names.

Club admin also a club member has all the member features plus add a new member to the club, edit existing member details, re-activate
or de-activate a member for their club membership, add new news, add new team, add a new opposition team, add new fixture, 
assign a member to a team and check a member that is part of the team eligibility to play on that team with the age restriction to play the game.

Above are the high level overview of what the webapp is capable of and the features from two login interfaces, member and admin.
I have structured my webapp across multiple functions and routes. My goal is to make the app minimal, easy to navigate and 
with plain background colour throughout the pages.
The first function which connect to the home page, it is a default page with '/' in the app route to use GET and POST methods allow the member
select the option and login to their dashboard. I created the function with POST method use if condition statement and return statement else would be
the GET request to read the member details from the database. 

My assumption was getting the return data from database display on the login page which it did not happen when I have a missing variable in the return statement.
The design of the page was plain background with the submit button as login in blue to give it a nice contrasting colour to the rest of the page.
The design decision made based on simple to use and simple solution and make it work rather than make it pretty. Minimal but still does the job and look
professional. The validaity of this function is making the variable matching with the Jinja template language and call the variable name correctly from html template.
When a user execute the use of system, it does what the function intend to do which bring the user in this case, the club member to their dashboard with their
name and correct details.

In the next part, my code function structure covered return the data from members table which show all the correct member details when they login. Also,
it included how the member can update their contacts in their account.
I give it a route as /member to link the function to the members html template where read the information as a form. In this function, I used multiple 
executions to draw data from different tables in the database to return the club news data and fixtures data. The tricky part was thinking how to display 
two different teams with different team name to match them with future games. I assume using a join table method to make the teams join the fixtures table
and the relationship between the two tables were home team and away team match the team id. It was an assumption made prior to draw out the function and 
execute the query to test whether it will display the way I want for the upcoming fixtures.
With the update member contact function, it uses two if condition statements and return with different app route which bring you to a new page for the form.
I put the update contacts button in the same table as member details which more related and look more clean on the page, also for the user (member) when checking
their details, can easily know where to update their contacts.
The first else condition to check if the member have valid id or not, assume they have, else it will bring the user back to the front page. Assuming this function
was part of the authentication for the member login and evidence as a member.
The second part of the condition statement also connect to previous if statement to read out the data through GET request. When the user submit the form 
update the ocntacts it will bring them back to their member page and they will see the changes made because of the GET request here read the data out 
from the database table.

For the club admin, I made the code structure and functions according to how I want to present it on the browser page. 
Start with the main function of the admin, it connect to the admin html template where the club admin recognised from their memberID give it a unique value
and check if they have admin access. I assume the validaity of the function to define the capability of a admin within the system which is a key page that connect
with other functions. The layout of the admin page I have decided to make it to one side with all the buttons have a space between them and with line of space for
each element. Also, give it a colourful design of the buttons to have a great contrast to the white background. It is easily for the admin to select which function
they like to go in.

The other parts of the admin functions where I thought that would be the nature flow of a webpage.
Club admin page function followed by add news item function and members list display on the page. 
The route with add news function return with the name add news html template where it has all the key dataset for admin to add a new news item.
I assume the news use textarea to make the input box larger when get the news, it can display clearly and edit any mistake easily before post to the members.
The design element again here to make it simple, use minimal colour with mainly the layout and structure of input containers. 
The redirect route bring the user back to the admin page and they can see the new news item being added. 
The view member, add member and update member within the admin page are interrelated as you see their app routes with '/' that is similar.
Add member and update member are the sub-route of view member as they are part of the same page which extended from view member.
The design logic also clear that use light yellow border with white background create a hint of simplicity and easy to read. 
The update member function has a similar code structure to the member update contacts as my assumption was both are being update and both updating
data from the database use UPDATE as keyword for the MySQL query in python function and redirect it back to the view member page to see the changes made
once the update command executed.
My assumption with the view member page also combined with the report all active members page as thinking when the admin add a new member or update a member 
can update their membership status. Through that route it can display all the active members If the club admin set all members to active in the form setting.
Return to the admin page and refresh, then go back to the view club member page to see all the active members to print if needed.
Assumption made here also take the design decision and page structure into consideration with less page and one less function to write, make it easier to integrate
with the two. I would assume that does the job and still easy to use for the user to get around the page between view member, add members and update member details
from the club admin functions.

The next function add new team also linked to the admin page as the app route suggested along with the add new fixtures. As those app route put the route function
design logic in mind. Part of the admin page extend to another page and once the information either update or add to the existing database then bring the user
back to the default page which the admin page. 
It renders template making connection to their html template to receive any data as I used Jinja templating language to get the variable name from python.
Lastly, same as the rest of admin function, grade eligibility checks if a member eligible to play in a team. The function also has the similar app route which
is the child page of the admin page. The variable names are given meaning to both python and Jinja template in html as Jinja call out the data pass through python
and MySQL query. 
Again, with the design element to the page, for simplicity and user friendly, i choose white background for consistency with minimalist design idea in mind
to make the page look tidy but not boring. 

Overall, the webapp build around simple solution principle and user friendly in mind, but not focus on make it look elegant or pretty in any shape or form.
Most assumption and design element take simplicity into consideration and sound structure of the page. With different app route well connected and python functions
interconnect with MySQL queries and execute the queries to add or update the data on user command.



