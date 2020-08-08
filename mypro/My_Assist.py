'''
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
	print("Speak: ")
	audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		print("you said: {}".formattext())
	except:
		print("Sorry,Speak Again")
		
		
'''		
		

		
import speech_recognition
import webbrowser
r = speech_recognition.Recognizer()
with speech_recognition.Microphone(device_index=1) as source:
	print("Speak: ")
	audio = r.listen(source)
	try:
		text = r.recognize_google(audio)
		webbrowser.open("www."+text+".com")
		print("you said: {}".format(text))
	except:
		print("Sorry,Speak Again")