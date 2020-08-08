#pip install speedtest-cli
#pip install pywhatkit
import speedtest
import pywhatkit as kit
test = speedtest.Speedtest()
download = test.download()
upload = test.upload()
print(f"Download Speed: {download}\nUpload Speed: {upload}")
R = (f"Download Speed: {download} \n Upload Speed: {upload}")
#print(f"Upload Speed: {upload}")
kit.sendwhatmsg("+916302258525",R,11,13) 