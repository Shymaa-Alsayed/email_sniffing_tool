# -*- coding: utf-8 -*-
"""
Created on Tue Mar  3 21:59:04 2020

@author: LEGION
"""
# import necessary dependencies
from flask import Flask, render_template, request
import shortcut_using_api


# create flask app
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/Reveal_Email', methods=['POST'])
def Reveal_Email():
    display_msg=''
    rem_credits='Remaining credit: '
    def process(name, domain,apikey):
        splitted = name.lower().split()
        f_name = splitted[0]
        l_name = splitted[1]
        if apikey!="":
            display_msg,credits = shortcut_using_api.generate_email(f_name, l_name, domain, apikey)
        else:
            display_msg,credits = shortcut_using_api.generate_email(f_name, l_name, domain, '29ZR5ZE2TB6BJKYO7M8C')
        return display_msg,credits


    if request.method == 'POST':
        name = request.form['name']
        domain = request.form['domain']
        apikey=request.form['apikey']
        display_msg,credits = process(name, domain,apikey)
        rem_credits=rem_credits+str(credits)
    return render_template('result.html', display_msg=display_msg,rem_credits=rem_credits)


if __name__ == '__main__':
    app.run(debug=True)
