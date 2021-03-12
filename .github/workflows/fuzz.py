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
for repo in g.get_user().get_repos():
    print(repo.name)