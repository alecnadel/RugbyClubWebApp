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
The first function which connect to the home page, it is a default page with '/' in the app route and use GET and POST methods allow the member
select the option and login to their dashboard. I created the function with POST method use if condition statement and return else would be
the GET request to read the member details from the database. 
