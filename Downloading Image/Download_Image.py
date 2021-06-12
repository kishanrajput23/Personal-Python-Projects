import requests
url =input("Enter the image of url ")
post =requests.get(url)

#file handling....
open('ramshyam.jpg','wb').write(post.content)
print("FILE DOWNLOAD SUCCESSFULLY.....")
