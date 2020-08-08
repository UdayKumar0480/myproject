import pyqrcode
s = 56721652
url = pyqrcode.create(s)
url.svg("the_coder_point.svg",scale=10)