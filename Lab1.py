#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set fileencoding=utf8 :
'''
To scrape some text, namely the book title, from the webpage, and print it
@author: germanbnf@gmail.com
'''
import urllib2
from bs4 import BeautifulSoup
import telebot
import sys

class Client(object):
    #get web
    def get_webpage(self, page):
        '''obtenir plana web'''
        f = urllib2.urlopen(page)
        htmlpage = f.read()
        f.close()
        return htmlpage

    #search the book title
    def search_data(self, html):
        bs = BeautifulSoup(html, 'html.parser')
        htmlparse = bs.find("div" ,"dotd-title")
        result=htmlparse.find("h2").text
        return result.replace("\t","")


    #print result
    def main(self):
        webpage = self.get_webpage('https://www.packtpub.com/packt/offers/free-learning/')
        results = self.search_data(webpage)
        TOKEN = '350940549:AAEEuodqKgL6PBI_xeIQv8--agwyULjf_IM'
        mi_bot = telebot.TeleBot(TOKEN)
        mi_bot.send_message(255142257,results)
        print results


if __name__ == "__main__":
    cw = Client()
    cw.main()
