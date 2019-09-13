# users INSERTS

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Richard", "Speed", "07941783041", "rjspeed@icloud.com", "test_password", "full", "super");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Ashley", "Brooks", "07941991122", "abrooks@dbwood.com", "test1_password", "full", "player");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Steve", "Brown", "07941119933", "sbrown@na.org", "test2_password", "full", "player");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Paul", "Burrell", "07948935671", "pburrell@babcock.co.uk", "test3_password", "full", "player");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Chris", "Gibbons", "07942768871", "cgibbons@hotmail.com", "test4_password", "full", "player");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Dave", "Grant", "07943780192", "dgrant2@hotmail.com", "test5_password", "full", "admin");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Christian", "Cardenas", "07941783041", "ccard@icloud.com", "test_password", "full", "super");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Paul", "Drury", "07941934562", "pdrury@hotmail.com", "test1_password", "full", "player");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Mark", "Chester", "07942359933", "mchest15@icloud.org", "test2_password", "full", "player");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Paul", "Allen", "09048935671", "pallenx@hotmail.co.uk", "test3_password", "full", "player");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Matt", "Connor", "07920495871", "17mconn@yahoo.com", "test4_password", "full", "player");

INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile)
VALUES ("Andrew", "Appleby", "07940093892", "aapple19@hotmail.com", "test5_password", "full", "admin");

# comps INSERTS

INSERT INTO comps 
VALUES (1, "2019 Leagues Session 1", 1, "Div A", "01/01/2019", "31/01/2019", 1);

INSERT INTO comps 
VALUES (1, "2019 Leagues Session 1", 2, "Div B", "01/01/2019", "31/01/2019", 1);

INSERT INTO comps 
VALUES (1, "2019 Leagues Session 1", 3, "Div C", "01/01/2019", "31/01/2019", 1);

INSERT INTO comps 
VALUES (2, "2019/20 Handicap", 1, "R8", "01/10/2019", "15/11/2019", 0);

# comp_participant INSERTS

INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 1, 1);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 1, 2);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 1, 3);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 1, 4);

INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 2, 5);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 2, 6);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 2, 7);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 2, 8);

INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 3, 9);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 3, 10);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 3, 11);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (1, 3, 12);

INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (2, 1, 4);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (2, 1, 5);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (2, 1, 6);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (2, 1, 7);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (2, 1, 8);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (2, 1, 9);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (2, 1, 10);
INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) 
VALUES (2, 1, 11);






