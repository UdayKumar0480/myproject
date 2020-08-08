from urllib.request import urlopen
#data = input("Enter the your url: ")
http = urlopen("http://aptrongurgaon.in/all-courses.html").read()
print(http)