# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:39:36 2020

@author: mario
"""


from github import Github
import os
import requests
import json


#file = open("../../credits.md")
#for line in file:
#    print(line)

g = Github( os.getenv("GITHUB_TOKEN"))
# Github Enterprise with custom hostname

# Then play with your Github objects:
repo = g.get_repo(os.getenv("GITHUB_REPO"))

contents = repo.get_contents("")
markdown_files = []

while contents:
    file_content = contents.pop(0)
    print(file_content.path)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        #print(file_content.path)
        if file_content.path[-3:] == ".md":
            #print("selected: "+ file_content.html_url)
            markdown_files.append(file_content)
        
print(markdown_files[0].html_url)
print(g.render_markdown(markdown_files[0].decoded_content.decode("utf-8") ))

payload = {'url': markdown_files[0].html_url,
           'title': markdown_files[0].name,
           'body': g.render_markdown(markdown_files[0].decoded_content.decode("utf-8"))
          }

r = requests.post('https://{}:5000/add-document'.format(os.getenv("SEARCH_HOST")),
                  json=payload,
                  auth=('user', os.getenv("API_USER_PASSWORD")))
print(r.status_code)
print(r.content)

#get the result code and print it
#print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
#data = webUrl.read()
#print (data)


print("finished")