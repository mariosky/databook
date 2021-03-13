# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:39:36 2020

@author: mario
"""


from github import Github
import os
import requests

from bs4 import BeautifulSoup
import time


#file = open("../../credits.md")
#for line in file:
#    print(line)

g = Github( os.getenv("GITHUB_TOKEN"))
# Github Enterprise with custom hostname

# Then play with your Github objects:
repo = g.get_repo(os.getenv("GITHUB_REPO"))

contents = repo.get_contents("")

while contents:
    file_content = contents.pop(0)
    if file_content.type == "dir":
        contents.extend(repo.get_contents(file_content.path))
    else:
        #print(file_content.path)
        if file_content.path[-3:] == ".md":
            html_doc = g.render_markdown(file_content.decoded_content.decode("utf-8"))
            soup = BeautifulSoup(html_doc, 'html.parser')
            text = soup.get_text()


            payload = {'url': file_content.html_url,
                       'title': file_content.name,
                       'body': text
                      }

            r = requests.post('http://{}:5000/add-document'.format(os.getenv("SEARCH_HOST")),
                              json=payload,
                              auth=('user', os.getenv("API_USER_PASSWORD")))
            print(file_content.name, r.status_code)
            time.sleep(1)
print("done")
#get the result code and print it
#print ("result code: " + str(webUrl.getcode()))

# read the data from the URL and print it
#data = webUrl.read()
#print (data)


print("finished")