import sqlite3
import os

DIRPATH = os.path.dirname(__file__)
DBFILENAME = "sqapp.db"
DBPATH = os.path.join(DIRPATH, DBFILENAME)

def seed(dbpath=DBPATH):

    # users INSERTS
    users = [
        ("Richard", "Speed", "07941783041", "rjspeed@icloud.com", "test_password", "full", "super"),
        ("Steve", "Brown", "07941119933", "sbrown@na.org", "test2_password", "full", "player"),
        ("Paul", "Burrell", "07948935671", "pburrell@babcock.co.uk", "test3_password", "full", "player"),
        ("Chris", "Gibbons", "07942768871", "cgibbons@hotmail.com", "test4_password", "full", "player"),
        ("Dave", "Grant", "07943780192", "dgrant2@hotmail.com", "test5_password", "full", "admin"),
        ("Christian", "Cardenas", "07941783041", "ccard@icloud.com", "test1_password", "full", "player"),
        ("Paul", "Drury", "07941934562", "pdrury@hotmail.com", "test6_password", "full", "player"),
        ("Mark", "Chester", "07942359933", "mchest15@icloud.org", "test7_password", "full", "player"),
        ("Paul", "Allen", "09048935671", "pallenx@hotmail.co.uk", "test8_password", "full", "player"),
        ("Matt", "Connor", "07920495871", "17mconn@yahoo.com", "test9_password", "full", "player"),
        ("Andrew", "Appleby", "07940093892", "aapple19@hotmail.com", "test10_password", "full", "player"),
        ("Ashley", "Brooks", "07941991122", "a.brooks@dbwoods.co.uk", "test11_password", "full", "player"),
        ("Andrew", "Appleby", "07919092067", "acappleby82@gmail.com", "test12_password", "full", "player"),
        ("Dave", "Moore", "", "davegmoore@aol.com", "test13_password", "full", "player"),
        ("Dean", "Revill", "", "dean.revill@jivili.com", "test14_password", "full", "player"),
        ("Aidy", "Greenberry", "", "aidangreenberry1983@gmail.com", "test15_password", "full", "player"),
        ("Ben", "Taylor", "07729542683", "bentaylortheonly@gmail.com", "test16_password", "full", "player"),
        ("Adam", "Whitney", "07779183249", "ad.whit123@gmail.com", "test17_password", "full", "player")]

    # comps INSERTS
    comps = [
        # ends 301218
        (1, "2018 5 Ending 301218", 1, "Div P", "01/10/2018", "30/12/2018", 1),
        (1, "2018 5 Ending 301218", 2, "Div 1", "01/10/2018", "30/12/2018", 1),
        (1, "2018 5 Ending 301218", 3, "Div 2", "01/10/2018", "30/12/2018", 1),
        # # ends 030319
        (2, "2019 1 Ending 030319", 1, "Div P", "01/01/2019", "03/03/2019", 1),
        (2, "2019 1 Ending 030319", 2, "Div 1", "01/01/2019", "03/03/2019", 1),
        (2, "2019 1 Ending 030319", 3, "Div 2", "01/01/2019", "03/03/2019", 1),
        # # ends 280419
        (3, "2019 2 Ending 280419", 1, "Div P", "04/03/2019", "28/04/2019", 1),
        (3, "2019 2 Ending 280419", 2, "Div 1", "04/03/2019", "28/04/2019", 1),
        (3, "2019 2 Ending 280419", 3, "Div 2", "04/03/2019", "28/04/2019", 1)]

    # comp_participant INSERTS
    comp_parts = [
        (1, 1, 1),
        (1, 1, 2),
        (1, 1, 3),
        (1, 1, 4),
        (1, 2, 5),
        (1, 2, 6),
        (1, 2, 7),
        (1, 2, 8),
        (1, 3, 9),
        (1, 3, 10),
        (1, 3, 11),
        (1, 3, 12),
        (2, 1, 4),
        (2, 1, 5),
        (2, 1, 6),
        (2, 1, 7),
        (2, 1, 8),
        (2, 1, 9),
        (2, 1, 10),
        (2, 1, 11)]

    with sqlite3.connect(dbpath) as conn:
        curs = conn.cursor()
        SQL = """INSERT INTO users (first_name, last_name, phone_1, email, password_hash, membership_type, profile) 
                 VALUES (?, ?, ?, ?, ?, ?, ?);"""
        for user in users:
             curs.execute(SQL, user)

        SQL = """INSERT INTO comps VALUES (?, ?, ?, ?, ?, ?, ?);"""
        for comp in comps:
            curs.execute(SQL, comp)

        SQL = """INSERT INTO comp_participants (comp_id, sub_comp_id, user_id) VALUES (?, ?, ?);"""
        for comp_part in comp_parts:
            curs.execute(SQL, comp_part)

if __name__ == "__main__":
    seed(DBPATH)
