#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name:
# Collaborators:
# Time:

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
import pytz


#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# NewsStory
class NewsStory(object):
    """docstring for NewsStory"""
    def __init__(self, guid, title, description, link, pubdate):
        super(NewsStory, self).__init__()
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
# PhraseTrigger
class PhraseTrigger(Trigger):
    """docstring for PhraseTrigger"""
    def __init__(self, phrase):
        super().__init__()
        phrase = phrase.lower()
        self.phrase = phrase
    def is_phrase_in(self, text):
        # 转小写
        text = text.lower()
        # 去掉标点
        # text = ''.join(c for c in text if c not in string.punctuation)
        _ = lambda c : c if c not in string.punctuation else ' '
        text = list(map(_, text))
        text = ''.join(text)
        # 去掉重复空格
        text = text.split()
        text = ' '.join(text)
        # 单词必须相同，cow不能是cow
        # if self.phrase in text:
        phrase_list = self.phrase.split()
        text_list = text.split()
        if len(text_list) > len(phrase_list):
            sub_slices = []
            for i in range(len(text_list)-len(phrase_list)+1):
                # print('aaaa')
                sub_slices.append(text_list[i:i+len(phrase_list)])
            # print(sub_slices)
            return phrase_list in sub_slices
        elif len(text_list) == len(phrase_list):
            return text_list == phrase_list
        else:
            return False

# Problem 3
# TitleTrigger
class TitleTrigger(PhraseTrigger):
    """docstring for TitleTrigger"""
    def __init__(self, phrase):
        super().__init__(phrase)
    def evaluate(self, newsStory):
        return super().is_phrase_in(newsStory.get_title())

# Problem 4
# DescriptionTrigger
class DescriptionTrigger(PhraseTrigger):
    """docstring for DescriptionTrigger"""
    def __init__(self, phrase):
        super().__init__(phrase)
    def evaluate(self, newsStory):
        return super().is_phrase_in(newsStory.get_description())


# TIME TRIGGERS

# Problem 5
# TimeTrigger
# Constructor:
#        Input: Time has to be in EST and in the format of "%d %b %Y %H:%M:%S".
#        Convert time from string to a datetime before saving it as an attribute.
class TimeTrigger(Trigger):
    """docstring for TimeTrigger"""
    def __init__(self, pubdate):
        super().__init__()
        pubdate = datetime.strptime(pubdate, "%d %b %Y %H:%M:%S")
        pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))
        '''
        try:
            # ancient_time = datetime(1987, 10, 15)
        # pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))
        
            pubdate = datetime.strptime(pubdate, "%d %b %Y %H:%M:%S")
            # pubdate.replace(tzinfo=pytz.timezone("GMT"))
            pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))
            # pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%d %b %Y %H:%M:%S")
            pubdate = pubdate.replace(tzinfo=pytz.timezone("EST"))
        '''
        self.pubdate = pubdate

# Problem 6
# BeforeTrigger and AfterTrigger
class BeforeTrigger(TimeTrigger):
    """docstring for BeforeTrigger"""
    def __init__(self, pubdate):
        super().__init__(pubdate)
    def evaluate(self, newsStory):
        pubdate = newsStory.get_pubdate()
        if pubdate.tzinfo is None:
            pubdate = pubdate.replace(tzinfo=pytz.timezone('EST'))
        return pubdate < self.pubdate

class AfterTrigger(TimeTrigger):
    """docstring for AfterTrigger"""
    def __init__(self, pubdate):
        super().__init__(pubdate)
    def evaluate(self, newsStory):
        pubdate = newsStory.get_pubdate()
        if pubdate.tzinfo is None:
            pubdate = pubdate.replace(tzinfo=pytz.timezone('EST'))
        return pubdate > self.pubdate

# COMPOSITE TRIGGERS

# Problem 7
# NotTrigger
class NotTrigger(Trigger):
    """docstring for NotTrigger"""
    def __init__(self, trigger):
        super().__init__()
        self.trigger = trigger
    def evaluate(self, newsStory):
        return not self.trigger.evaluate(newsStory)

# Problem 8
# AndTrigger
class AndTrigger(Trigger):
    """docstring for AndTrigger"""
    def __init__(self, trigger1, trigger2):
        super().__init__()
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, newsStory):
        return self.trigger1.evaluate(newsStory) and self.trigger2.evaluate(newsStory)

# Problem 9
# OrTrigger
class OrTrigger(Trigger):
    """docstring for OrTrigger"""
    def __init__(self, trigger1, trigger2):
        super().__init__()
        self.trigger1 = trigger1
        self.trigger2 = trigger2
    def evaluate(self, newsStory):
        return self.trigger1.evaluate(newsStory) or self.trigger2.evaluate(newsStory)

#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # Problem 10
    # This is a placeholder
    # (we're just returning all the stories, with no filtering)
    # return stories
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered_stories.append(story)
                break
    return filtered_stories

#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)
    # Problem 11
    # line is the list of lines that you need to parse and for which you need
    # to build triggers
    # print(lines) # for now, print it so you see what it contains!
    
    trigger_dict = dict()
    trigger_list = []
    for line in lines:
        args = line.split(',')
        # args = ["t1","TITLE","election"]
        if args[0] != "ADD":
            print(args)
            if args[1].upper() == "TITLE":
                trigger_dict[args[0]] = TitleTrigger(args[2])
            elif args[1].upper() == "DESCRIPTION":
                trigger_dict[args[0]] = DescriptionTrigger(args[2])
            elif args[1].upper() == "AFTER":
                trigger_dict[args[0]] = AfterTrigger(args[2])
            elif args[1].upper() == "BEFORE":
                trigger_dict[args[0]] = BeforeTrigger(args[2])
            elif args[1].upper() == "NOT":
                trigger_dict[args[0]] = NotTrigger(trigger_dict[args[2]])
            elif args[1].upper() == "AND":
                trigger_dict[args[0]] = AndTrigger(trigger_dict[args[2]], trigger_dict[args[3]])
            elif args[1].upper() == "OR":
                trigger_dict[args[0]] = OrTrigger(trigger_dict[args[2]], trigger_dict[args[3]])
        elif args[0] == "ADD":
            for i in range(1, len(args)):
                trigger_list.append(trigger_dict[args[i]])
    # print(trigger_dict)
    return trigger_list


SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        print(triggerlist)
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()

