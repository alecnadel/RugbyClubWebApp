


INSERT INTO Clubs VALUES 
(23, 'Crusaders Rugby', 'Orangetheory Stadium','95 Jack Hinton Drive, Addington, Christchurch 8024', 08008227369, 'admin@crusaders.co.nz'),
(12, 'Cashmere Rugby Club', 'Centenial Park', '25 Lyttleton St, Somerfield, Christchurch 8024', 033884567, 'admin@cashmererugby.co.nz'),
(6, 'Lincoln Area Rugby', 'Lincoln Domain', 'Meijer Drive, Halswell, Lincoln 7608', 033165487, 'admin@lincolnRC.co.nz');

INSERT INTO Grades VALUES
(1, 'Juniors', 11, 15), 
(3, 'Under 18s', 16, 17),
(5, 'Seniors', 18, 99),
(6, 'Masters', 35, 99); 

INSERT INTO Teams VALUES
(101, 23, 'Junior Crusaders', 1),
(102, 23, 'Crushers', 6),
(103, 23, 'Southern Boot', 3),
(123, 23, 'Between the Posts', 5),
(125, 6, 'Midgets', 3),
(143, 12, 'ScrumTime', 5),
(133, 12, 'Black Ferns', 6),
(152, 6, 'All Blacks', 1);


INSERT INTO Members VALUES
(5646, 23, 123, 'Antoine', 'Dupont', '123 Columbo St', 'Sydenham', 'Christchurch', 'antoine@crusadersrugby.co.nz', 0214567892, '2001-12-08', 1, 0),
(5643, 23, 123, 'Aaron', 'Smith', '47 Westminster St', 'St Albans', 'Christchurch', 'aaron@allblack.co.nz', 02224638546, '1987-04-26', 1, 1),
(5623, 23, 123, 'Beauden', 'Barrett', '34 Main Sth Rd', 'Islington', 'Christchurch', 'beauden@allblack.co.nz', 0274658254, '1999-06-07', 1, 0),
(5689, 23, 102, 'Grant', 'Fox', '4567 Gingerbread Lane', 'Bowenvale', 'Christchurch', 'foxy@crusaders.co.nz', 0214568274, '1975-11-21', 1, 0); 

INSERT INTO Fixtures VALUES
(235, '2021-09-21 16:35:00', 101, 125, 0, 0),
(231, '2021-08-24 17:00:00', 103, 143, 12, 7),
(232, '2021-08-25 19:35:00', 123, 125, 35, 12),
(237, '2021-09-22 16:35:00', 102, 125, 0, 0);


INSERT INTO ClubNews VALUES
(4, 23, 'All Blacks find areas to improve ahead of Pumas rematch', 'By Joe Bloggs', '2021-09-15', "A different approach can be expected from Argentina on Saturday when taking on the All Blacks at Suncorp Stadium in Brisbane in the Fortinet Rugby Championship. That's the feeling lock Scott Barrett, 45 Tests, has ahead of the game. The South Americans, who have endured more obstacles than any of their Championship opponents in arriving at the tournament, have not scored a point against the All Blacks in the two outings since last year's triumph when winning their first Test against them.
That would add to the desperation they brought to the Test. They'll look at their tape and present different pictures. They'll probably turn up with a little more of an edge he said. But while the Pumas would be looking to get better, so would the All Blacks."),
(3, 23, 'Aaron Smith to miss rest of Fortinet rugby championship', 'By Superman', '2021-06-28', "All Blacks halfback Aaron Smith won't be joining the All Blacks in Australia for the remainder of the Fortinet Rugby Championship. 32-year-old Smith stayed in New Zealand to be with his family awaiting the birth of his second child. He will join his Manawatū Turbos team this week to train and play in the Bunnings Warehouse NPC this season. Smith says he's excited about playing for the Turbos and can't wait to get back on the field.");  





