
import sqlite3
import random
import string
from app.orm import ORM
from app.util import hash_password
from app.comp import Comp
from app.comp_part import Comp_Part
from app.match import Match


class User(ORM):

    tablename = "users"
    fields = ["email", "password_hash", "first_name", "last_name", "phone_1",
              "phone_2", "profile"]

    def __init__(self, *args, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.email = kwargs.get('email')
        self.password_hash = kwargs.get('password_hash')
        self.first_name = kwargs.get('first_name')
        self.last_name = kwargs.get('last_name')
        self.phone_1 = kwargs.get('phone_1')
        self.phone_2 = kwargs.get('phone_2')
        self.profile = kwargs.get('profile')

    @classmethod
    def login(cls, email, password):
        return cls.select_one_where("WHERE email = ? AND password_hash = ?",
                                    # (email, hash_password(password)))
                                    (email, password))
    
    @classmethod
    def password_reset(cls, email):
        return cls.select_one_where("WHERE email = ?",
                                    # (email, hash_password(password)))
                                    (email, ))

    @classmethod
    def user_details(cls, user_id):
        return cls.select_one_where("WHERE user_id = ?",
                                    # (email, hash_password(password)))
                                    (user_id, ))

    @classmethod
    def user_delete(cls, user_id):
        return cls.delete("WHERE user_id = ?",
                                    # (email, hash_password(password)))
                                    (user_id, ))
    
    def user_account(cls, email, password, first_name, last_name, phone_1, phone_2):
        # Either insert or update users table record
        # i) Insert: First ensure supplied email add isn't already being used,
        # next insert record with supplied data attributes ie. email, password_hash,
        # first_name, last_name, phone_1, phone2
        # ii) Update: Update users table record with above listed attributes






    
    # @classmethod
    # def api_authenticate(cls, key):
    #     ak_account = cls.select_one_where("WHERE api_key = ?", (key, ))
    #     if ak_account is None:
    #         return None
    #     return ak_account

    # def create_api_key(self):
    #     self.api_key = ''.join(random.choices(string.ascii_uppercase + string.digits, k=15))
    #     return self.api_key

    # def set_password(self, password):
    #     self.password_hash = hash_password(password)

    # def get_account(self):
    #     return Account.select_one_where("WHERE pk = ?", (self.pk,))       

    # def deposit(self, deposit_amount):
    #     cur_balance = Account.select_one_where("WHERE pk = ?", (self.pk,))
        
    #     self.username = cur_balance.username
    #     self.password_hash = cur_balance.password_hash
    #     if cur_balance.balance is None:
    #         self.balance = deposit_amount
    #         self.api_key = cur_balance.api_key
    #         return deposit_amount
    #     else:
    #         self.balance = round(cur_balance.balance + deposit_amount,2)
    #         self.api_key = cur_balance.api_key
    #         return round(cur_balance.balance + deposit_amount, 2)

    # def get_positions(self):
    #     return Position.select_many_where("WHERE accounts_pk = ?", (self.pk, ))

    # def get_position_for(self, ticker):
    #     position = Position.select_one_where(
    #         "WHERE ticker = ? AND accounts_pk = ?", (ticker, self.pk))
    #     if position is None:
    #         return Position(ticker=ticker, accounts_pk=self.pk, shares=0)
    #     return position

    # def get_trades(self):
    #     return Trade.select_many_where("WHERE accounts_pk = ? ORDER BY time DESC", (self.pk, ))

    # def get_trades_for(self, ticker):
    #     return Trade.select_many_where("WHERE accounts_pk = ? and ticker = ? \
    #                                     ORDER BY time DESC", (self.pk, ticker))

    # def buy(self, ticker, amount):
    #     #Get account details
    #     account = self.get_account()
    #     #Check stock exists and if so retrieve current price
    #     quote_price = get_price(ticker)
    #     if not quote_price: 
    #     #    raise KeyError
    #         msg = "Input Ticker doesn't exist"
    #     else:
    #         #Check sufficient funds
    #         quote_price = float(quote_price)
    #         amount = float(amount)
    #         if not account.balance >= amount*quote_price:
    #             #raise ValueError
    #             msg = "Insufficient funds"
    #         else:
    #             #Insert Trade row
    #             new_trade = Trade(accounts_pk=self.pk, ticker=ticker, \
    #                               volume=amount, price=quote_price)
    #             new_trade.save()
                
    #             #Update or Insert Position row
    #             position = self.get_position_for(ticker)
    #             if position.shares == 0:
    #                 #Insert
    #                 new_position = Position(accounts_pk=self.pk, ticker=ticker, shares=amount)
    #             else:
    #                 #Update 
    #                 new_position = Position(pk=position.pk, accounts_pk=self.pk, ticker=ticker, \
    #                                         shares=position.shares + amount)
    #             new_position.save()
                    
    #             #Update balance on Account row
    #             new_balance = Account(pk=self.pk, username=account.username, \
    #                                 password_hash=account.password_hash, \
    #                                 balance=account.balance - (amount*quote_price), \
    #                                 api_key=account.api_key)
    #             new_balance.save()
    #             msg = "Buy transaction completed successfully"
    #     return msg

    # def sell(self, ticker, amount):
    #     #Get account and positions details
    #     account = self.get_account()
    #     position = self.get_position_for(ticker)
    #     amount = int(amount)
    #     #Check stock exists and if so retrieve current price
    #     quote_price = get_price(ticker)
    #     if not quote_price: 
    #     #    raise KeyError
    #         msg = "Input Ticker doesn't exist"
    #     else:
    #         #Check sufficient shares
    #         if position.shares == 0 or amount > position.shares :
    #         #    raise ValueError
    #             msg = "Insufficient shares"
    #         else:
    #             #Insert Trade row
    #             new_trade = Trade(accounts_pk=self.pk, ticker=ticker, \
    #                               volume=amount*-1, price=quote_price)
    #             new_trade.save()
                
    #             #Update Position row
    #             new_position = Position(pk=position.pk, accounts_pk=self.pk, ticker=ticker, \
    #                                     shares=position.shares - amount)
    #             new_position.save()
                    
    #             #Update balance on Account row
    #             new_balance = Account(pk=self.pk, username=account.username, \
    #                                 password_hash=account.password_hash, \
    #                                 balance=account.balance + (amount*quote_price), \
    #                                 api_key=account.api_key)
    #             new_balance.save()
    #             msg = "Sell transaction completed successfully"
    #     return msg
        
        