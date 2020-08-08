import requests
response = requests.get("https://www.google.co.in/url?sa=i&url=https%3A%2F%2Fwww.lovesove.com%2Froyal-girls-attitude-status-for-whatsapp-in-english%2F&psig=AOvVaw0pGpA-YwA58rswOZjVjlUo&ust=1588426645152000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCKDSocLkkukCFQAAAAAdAAAAABAD")
with open(r"D:\file.jpg",'wb') as img_file:
	s = img_file.write(response.content)
print(s)