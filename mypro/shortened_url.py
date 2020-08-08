import pyshorteners
from flask import request
url = input("Please Enter your url: ")
s = pyshorteners.Shortener()
print("Your shortened url is::  ",s.tinyurl.short(url))
