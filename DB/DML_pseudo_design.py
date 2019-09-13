# To Auto Pop matches table
Approach: 2 types of insert dependent on competition.league value
1. competition.league = true
For a given comp_id & sub_comp_id combination (to be selected by user)
loop through each record in comp_participants ensuring each user_id has a 
match created (a record populated in table matches) against every other user_id 

2. competition.league = false (ie. knockout)
i. For 1st round = for a given comp_id & sub_comp_id combination (to be selected by user)
loop through each record in comp_participants ensuring each user_id has a 
match created (a record populated in table matches) against one other user_id,
to be selected at random

ii. For subsequent rounds = for a given comp_id (to be selected by user)
loop through each record in matches for the previous round to identify the winners.
a) create new records in comp_participants re the list of winners
b) perform step i) above

# Basic Operations:
1. Login screen validation of user email & password: retrieval of data from users table 
# SELECT count(*) user_count  
# FROM users
# WHERE email = ??? and password = ??? 

2. Retrieval & potential update of user details for current user from table users - 'Account' Nav tab 
# SELECT *  
# FROM users
# WHERE email = ??? and password = ??? 

# UPDATE users
# SET all details = whatever is on screen
# WHERE user_id = (logged in user, NB. user_id should be in state) 

3. Retrieval of all user contacts details from table users - 'Contacts' Nav tab 
# SELECT first_name, last_name, email, phone_1, phone_2 
# FROM users
# ORDER BY last_name  

4. Retrieval of match details for selected comp_id/sub_comp_id
-  'Leagues' Nav tab - 'Current' Nav tab
-  'Knockout Comps' Nav tab - 'Current' Nav tab
Whether table matches records are updatable dependent on current user_id, ie. can't 
post/edit another players matches     

# SELECT comp.comp_name, comp.sub_comp_name, comp_participants.points, matches.*
# FROM comps, comp_participants, matches
# WHERE comp.comp_id = ???
# AND comp.sub_comp_id = ???
# AND comp.comp_id = comp_participants.comp_id
# AND comp.sub_comp_id = comp_participants.sub_comp_id
# AND comp.comp_id = matches.comp_id
# AND comp.sub_comp_id = matches.sub_comp_id

5. Insert of tables comps & comp_participants -  'New Competition Setup' tab
Dependent on if the user is a) creating a new comp and sub_comp OR b) adding sub_comps 
to an existing comp

i) COMPS table

a)
INSERT INTO comps (comp_id, comp_name, sub_comp_id, sub_comp_name, start_date, end_date, league)
VALUES (
    max(comp.comp_id)+1,
    input by user: picked up from text field,
    1,
    input by user: picked up from text field,
    input by user, picked up from date picker,
    input by user, picked up from date picker,
    input by user, picked up from league/knockout radio button
)

a)
INSERT INTO comps (comp_id, comp_name, sub_comp_id, sub_comp_name, start_date, end_date, league)
VALUES (
    indirectly input by user, related to selection below,
    input by user: picked up from drop down,
    max(comp.sub_comp_id)+1 for the selected comp_id,
    input by user: picked up from text field,
    input by user, picked up from date picker,
    input by user, picked up from date picker,
    input by user, picked up from league/knockout radio button
)

ii) COMP_PARTICIPANTS table








Problems:
1. League format: what happens if a resut is entered incorrectly ? We can provide 'edit result' 
functionality but how can we edit the comp_participants.points value ?
Answer = after every result entry/edit, to repopulate the points value
from every result logged against those 2 players, not simply update the points
value with the latest match points

