"""This is scraper"""
# !/usr/bin/env python
# -*- coding: utf-8 -*-
# pylint: disable=import-error
# pylint: disable=superfluous-parens

import urllib2
import threading
from bs4 import BeautifulSoup


class ScrapThread(threading.Thread):
    """This is thread class"""
    def __init__(self, word, url, number):
        """This initializes the thread"""
        threading.Thread.__init__(self)
        self.word = word
        self.url = url
        self.number = number

    def run(self):
        """This is run method of thread"""
        url = self.url
        req = urllib2.Request(url, headers={'User-Agent': "Magic Browser"})
        con = urllib2.urlopen(req)
        # print con.read()
        soup = BeautifulSoup(con, "html.parser")
        # # print(soup.findAll('a', soup.findAll(text='data')))
        # print(soup.findAll(text='you'))
        for item in soup.find_all('a'):
            temp = item.string
            if temp is not None:
                if self.word.lower() in temp.lower():
                    print(self.number, "->", temp)


def main():
    """This is main function"""
    thread1 = ScrapThread("microsoft", 'https://www.reddit.com/r/programming/', "1")
    thread2 = ScrapThread("technology", 'https://www.nytimes.com/section/technology', "2")
    thread3 = ScrapThread("microsoft", 'http://news.ycombinator.com', "3")
    thread4 = ScrapThread("may", 'http://www.theguardian.com/us/technology?', "4")

    thread1.start()
    thread2.start()
    thread3.start()
    thread4.start()


if __name__ == "__main__":
    main()
