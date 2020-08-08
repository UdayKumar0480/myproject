import random
import pywhatkit as kit
s = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890@#$"
passwordlen = 16
password = "".join(random.sample(s,passwordlen))
print(password)
kit.sendwhatmsg("+916302258525",password,13,44)
print('send message successfully')