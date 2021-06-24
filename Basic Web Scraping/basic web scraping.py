#printing the text..
import requests
import bs4
link =input("Enter the url: ")
page =requests.get(link)
print(page.text)

#print the text in a readable form..
soup =bs4.BeautifulSoup(page.text,'html.parser')
text_format =soup.prettify()
print(text_format)

#print the list of image tag....
image_list =soup.find_all('img')
print(image_list)

#print the no of image tag.....
count_the_image =len(image_list)
print(count_the_image)



