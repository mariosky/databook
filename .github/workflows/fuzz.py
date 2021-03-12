# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 13:39:36 2020

@author: mario
"""


from github import Github
import os

file = open("../../credits.md")
for line in file:
    print(line)

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
        print(file_content.url)
        if file_content.path[-3:] == ".md":
            print("selected: "+ file_content)

print("finished")