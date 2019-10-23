
from flask import Flask, render_template, request, redirect, session, jsonify
from app.user import User
# from app import views
# from app import util
# from datetime import datetime, timedelta

app = Flask(__name__)
app.secret_key = "The session needs this!"

# 1.HOMEPAGE
# i) LOGON BUTTON - POST: SEND - EMAIL/PASSWORD / REC - MSG (SUCCESS OR NOT) & PK FOR STATE 
@app.route('/api/login', methods=['POST'])
def login():
    if not request.json or 'email' not in request.json or 'password' not in request.json:
        return jsonify({"error": "bad request"}), 400
    user = User.login(request.json['email'], request.json['password'])
    if not user:
        return jsonify({"msg": "access denied"})
    msg = "Access granted, user_id for use in REACT f-end: {}".format(user.user_id)
    return jsonify({"msg": msg})


# ii) PASSWORD RESET - POST: SEND - EMAIL / REC - MSG (SUCCESS OR NOT)
@app.route('/api/password_reset', methods=['POST'])
def password_reset():
    if not request.json or 'email' not in request.json:
        return jsonify({"error": "bad request"}), 400
    user = User.password_reset(request.json['email'])
    if not user:
        return jsonify({"msg": "no record of specified email"})
    # TO-DO: Send reset link to given email - probably done in front-end after having
    # returned success message
    return jsonify({"msg": "password reset link sent to specified email"})


# 2.ACCOUNT CREATE/EDIT/DELETE
# i) USER LOGS ON & LOADS ACCOUNT PAGE - POST: SEND - USER_ID(PK) / REC - USER DETAILS
@app.route('/api/user_details', methods=['POST'])
def user_details():
    if not request.json or 'user_id' not in request.json:
        return jsonify({"error": "bad request"}), 400
    user = User.user_details(request.json['user_id'])
    if not user:
        return jsonify({"error": "access denied"})    
    msg = "Email: {}, Password: {}, First_Name: ${}, Last_Name: ${}, \
          Phone_1: ${}, Phone_2: ${}".format(user.email, user.password_hash, \
          user.first_name, user.last_name, user.phone_1, user.phone_2)
    return jsonify({"msg": msg})

# ii) UPDATE BUTTON - POST: SEND - USER_ID(PK), EMAIL, PASSWORD, FIRST_NAME, LAST_NAME,
#     PHONE_1 / REC - MSG (SUCCESS OR NOT)
# Different dependent on whether inserting a new user record (from Create Account link)
# or if updating an existing record (from successful logon)
@app.route('/api/user_account', methods=['POST'])
def user_account():
    if not request.json or 'user_id' not in request.json or 'email' not in request.json
    or 'password' not in request.json or 'first_name' not in request.json 
    or 'last_name' not in request.json or 'phone_1' not in request.json:
        return jsonify({"error": "bad request"}), 400
    user = User.user_account(request.json['user_id'], request.json['email'], 
           request.json['password'], request.json['first_name'], request.json['last_name'],
           request.json['phone_1'], request.json['phone_2'])
    if not user:
        return jsonify({"error": "access denied"})    
    return jsonify({"msg": "account updated" })

# iii) DELETE BUTTON - POST: SEND - USER_ID(PK) / REC - MSG (SUCCESS OR NOT)
# Remove table users record
@app.route('/api/user_delete', methods=['POST'])
def user_delete():
    if not request.json or 'user_id' not in request.json:
        return jsonify({"error": "bad request"}), 400
    user = User.user_delete(request.json['user_id'])
    if not user:
        return jsonify({"error": "access denied"})    
    return jsonify({"msg": msg})

# 3.CONTACT DETAILS - ON PAGE LOAD - GET: ALL CONTACT DETAIS FROM USERS TABLE
@app.route('/api/contacts', methods=['GET'])
def contacts():
    # Retrieve & return all contact details from users table
    return jsonify({'message':msg})

# 4.INTERNAL LEAGUES
# i) ON PAGE LOAD - GET: COMP NAME/ID
@app.route('/api/comp_names', methods=['GET'])
def comp_names():
    # To pop League Session listbox: retrieve & return all comp.comp_id / comp.comp_name
    # combos where comp.league = True order by end_date desc
    return jsonify({'message':msg})

# ii) AFTER COMP NAME LISTBOX SELECT - POST: SEND COMP_ID / REC - SUB_COMP_ID / NAME 
@app.route('/api/subcomp_names', methods=['POST'])
def subcomp_names():
    # To pop Division listbox: retrieve & return all comp.sub_comp_id / comp.sub_comp_name
    # combos where comp.comp_id = supplied comp_id
    if not request.json or 'comp_id' not in request.json:
    
        return jsonify({"error": "bad request"}), 400
    return jsonify({"msg": msg})

# iii) AFTER SUB COMP NAME LISTBOX SELECT - POST: SEND SUB_COMP_ID / 
# REC - ALL MATCH DETAILS FOR SELECTED SUB_COMP_ID
@app.route('/api/league_matches', methods=['POST'])
def league_matches():
    if not request.json or 'sub_comp_id' not in request.json:
        return jsonify({"error": "bad request"}), 400
    return jsonify({"msg": msg})




# d) UPDATE RESULT BUTTON - POST: RESULT DETAILS
# e) PLAYER CLICK: GET: PLAYER CONTACT DETAILS
 






















# 5.COMP ADMIN
# a) ON PAGE LOAD - GET: COMP DETAILS FOR COMP NAME LISTBOX IN SUB COMP ADMIN FRAME
 
# i) COMP ADMIN FRAME
# a) COMP CREATE BUTTON - POST: COMP DETAILS TO STORE IN COMP TABLE
# b) COMP DELETE BUTTON - POST: COMP DETAILS TO REMOVE FROM COMP TABLE
 
# ii) SUB COMP ADMIN FRAME
# a) COMP NAME LISTBOX - GET: COMP DETAILS
# b) SUB COMP CREATE BUTTON - POST: SUB COMP DETAILS TO STORE IN COMP TABLE
# c) SUB COMP DELETE BUTTON - POST: SUB COMP DETAILS TO REMOVE FROM COMP TABLE
 
# iii) PLAYER ALLOCATION FRAME
# a) COMP NAME LISTBOX - GET: COMP DETAILS
# b) SUB COMP NAME LISTBOX - GET: SUB COMP DETAILS
# c) PLAYER LISTBOX - GET: USER DETAILS
# d) ADD PLAYER BUTTON - POST: COMP & USER DETAILS TO STORE IN COMP_PARTICIPANTS TABLE
# e) REMOVE PLAYER BUTTON - POST: COMP & USER DETAILS TO REMOVE FROM COMP_PARTICIPANTS TABLE; REMOVE RECORDS FROM MATCHES TABLE
# f) CREATE MATCHES BUTTON - POST: COMP DETAILS TO POP RECORDS IN MATCH TABLE FOR THAT COMP, IF EXIST TELL THE USER THAT HE IS ABOUT TO OVERWRITE EXISTING RECORDS
# (SOMEHOW COMPARE EXISTING RECORDS WITH NEW RECORDSET AND JUST POP NEW RECORDS IN MATCH TABLE)
 
# 6.CONTACT DETAILS
# GET: ALL CONTACT DETAILS
 













# T.TRADER CODE

# @app.route('/api/get_api_key', methods=['POST'])
# def get_api_key():
#     if not request.json or 'username' not in request.json or 'password' not in request.json:
#         return jsonify({"error": "bad request"}), 400
#     account = Account.login(request.json['username'], request.json['password'])
#     if not account:
#         return jsonify({"error": "access denied"})
    
#     return jsonify({"username": account.username, "api_key": account.api_key})

# @app.route('/api/<api_key>/balance', methods=['GET'])
# def balance(api_key):
#     if Account.api_authenticate(api_key) == None:
#         msg = "Invalid login credentials, pls retry"
#     else: 
#         pk = Account.api_authenticate(api_key).pk   
#         retrieve_bal = Account(pk=pk)
#         msg = "Your current balance = {}".format(retrieve_bal.get_account().balance)
#     return jsonify({'message':msg})

# @app.route('/api/<api_key>/deposit', methods=['POST'])
# def deposit(api_key):
#     if Account.api_authenticate(api_key) == None:
#         msg = "Invalid login credentials, pls retry"
#     else: 
#         if not request.json or 'amount' not in request.json:
#             return jsonify({"error": "bad request"}), 400
#         pk = Account.api_authenticate(api_key).pk
#         account_deposit = Account(pk=pk)
#         new_bal = account_deposit.deposit(float(request.json['amount']))
#         account_deposit.save()
#         msg = "New Balance = {}".format(new_bal)
#     return jsonify({'message':msg})    

# @app.route('/api/price/<ticker>', methods=['GET'])
# def price(ticker):    
#     quote = util.get_price(ticker)
#     if not quote: 
#         msg = "The Ticker Symbol entered does not exist"
#     else:
#         msg = "Current price for Ticker Symbol: {} = ${}".format(ticker, quote)
#     return jsonify({'message':msg})

# @app.route('/api/<api_key>/buy', methods=['POST'])
# def buy(api_key):    
#     if Account.api_authenticate(api_key) == None:
#         msg = "Invalid login credentials, pls retry"
#     else: 
#         if not request.json or 'ticker' not in request.json or 'volume' not in request.json:
#             return jsonify({"error": "bad request"}), 400
#         pk = Account.api_authenticate(api_key).pk
#         buy_txn = Account(pk=pk)
#         msg = buy_txn.buy(request.json['ticker'], request.json['volume'])
#     return jsonify({'message':msg}) 

# @app.route('/api/<api_key>/sell', methods=['POST'])
# def sell(api_key):
#     if Account.api_authenticate(api_key) == None:        
#         msg = "Invalid login credentials, pls retry"
#     else: 
#         if not request.json or 'ticker' not in request.json or 'volume' not in request.json:
#             return jsonify({"error": "bad request"}), 400
#         pk = Account.api_authenticate(api_key).pk
#         sell_txn = Account(pk=pk)
#         msg = sell_txn.sell(request.json['ticker'], request.json['volume'])
#     return jsonify({'message':msg})  

# @app.route('/api/<api_key>/trades/<ticker>', methods=['GET'])
# def trades(api_key, ticker):
#     if Account.api_authenticate(api_key) == None:
#         msg = "Invalid login credentials, pls retry"
#     else: 
#         pk = Account.api_authenticate(api_key).pk
#         user_trades = Account(pk=pk)
#         trades = user_trades.get_trades_for(ticker)
#         msg = {'trades':[]}
#         for trade in trades:
#             msg['trades'].append("Date/Time: {}, Ticker Symbol: {}, No. of Shares: {}, Price per Share: {}". \
#                           format((datetime.fromtimestamp(trade.time) - \
#                           timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S'), \
#                           trade.ticker, trade.volume, trade.price))
#     return jsonify({'message':msg}) 

# @app.route('/api/<api_key>/trades', methods=['GET'])
# def alltrades(api_key):        
#     if Account.api_authenticate(api_key) == None:    
#         msg = "Invalid login credentials, pls retry"
#     else: 
#         pk = Account.api_authenticate(api_key).pk
#         user_trades = Account(pk=pk)
#         trades = user_trades.get_trades()
#         msg = {'trades':[]}
#         for trade in trades:
#             msg['trades'].append("Date/Time: {}, Ticker Symbol: {}, No. of Shares: {}, Price per Share: {}". \
#                           format((datetime.fromtimestamp(trade.time) - \
#                           timedelta(hours=2)).strftime('%Y-%m-%d %H:%M:%S'), \
#                           trade.ticker, trade.volume, trade.price))
#     return jsonify({'message':msg}) 

# @app.route('/api/<api_key>/positions', methods=['GET'])
# def allpositions(api_key):      
#     if Account.api_authenticate(api_key) == None:    
#         msg = "Invalid login credentials, pls retry"
#     else: 
#         pk = Account.api_authenticate(api_key).pk
#         user_positions = Account(pk=pk)
#         positions = user_positions.get_positions()
#         msg = {'positions':[]}
#         for position in positions:
#             valuation = Position()  
#             getval = valuation.current_value(position.ticker, position.shares)     
#             msg['positions'].append("Ticker Symbol: {}, Shares: {}, Valuation: ${}".format(position.ticker, position.shares, getval))
#     return jsonify({'message':msg}) 

# @app.route('/api/<api_key>/positions/<ticker>', methods=['GET'])
# def positions(api_key, ticker):
#     if Account.api_authenticate(api_key) == None:    
#         msg = "Invalid login credentials, pls retry"
#     else: 
#         pk = Account.api_authenticate(api_key).pk
#         user_position = Account(pk=pk)
#         position = user_position.get_position_for(ticker)
#         valuation = Position()  
#         getval = valuation.current_value(ticker, position.shares)      
#         msg = "Ticker Symbol: {}, Shares: {}, Valuation: ${}".format(position.ticker, position.shares, getval)
#     return jsonify({'message':msg}) 

# @app.route('/api/company/<company>', methods=['GET'])
# def company(company):
#     companies = util.get_ticker(company)
#     if not companies: 
#         msg = "No matches for input Company Name"
#     else:
#         msg = {'company':[]}
#         for co in companies:
#             msg['company'].append(co)
#     return jsonify({'message':msg})

# @app.route('/api/createaccount/<name>/<password>', methods=['GET'])
# def createaccount(name, password):
#     new_account = Account(username=name)
#     new_account.set_password(password)
#     ak = new_account.create_api_key()
#     new_account.save()
#     msg = "Account successfully created, API api_key = {}".format(ak)
#     return jsonify({'message':msg})

def run():
    app.run(debug=True)
