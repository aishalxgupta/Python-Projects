# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 17:14:57 2022

@author: ONWER
"""


import requests
 
class Currency_convertor:
    
    rates = {}
    def __init__(self, url):
        data = requests.get(url).json()
 
      
        self.rates = data["rates"]
 
    
    def convert(self, from_currency, to_currency, amount):
        initial_amount = amount
        if from_currency != 'EUR' :
            amount = amount / self.rates[from_currency]
 
        
        amount = round(amount * self.rates[to_currency], 2)
        print('{} {} = {} {}'.format(initial_amount, from_currency, amount, to_currency))
        
        
      
        