import requests 
from parse import parse
import sys, zlib
import base64
from github import Github
from pprint import pprint

#empty list for storing input
repository_inputs=[]

#Getting input from the user
for i in sys.stdin:
    repository_inputs.append(i)
    
# iterate through the list of input repository
for i in repository_inputs:
    repo_name = i
    
    #removing trailing spaces
    repo_name=str(repo_name).strip()
        
    #Sending API request to github
    r= requests.get('https://api.github.com/repos/{0}/commits?per_page=1'.format(repo_name))
    
    #receving the json response
    commit = r.json()[0]['commit']['committer']
    
    #extracting last author name
    last_author_name=commit['name']
    
    #extracting last date of commit
    date_last_commit=commit['date']
    
    #generating a clone Url
    clone_url='https://github.com/{}.git'.format(repo_name)
    
    #printing the extracted details as tsv
    sys.stdout.write(repo_name+'\t'+clone_url+'\t'+date_last_commit+'\t'+last_author_name+'\t')
    sys.stdout.write('\n')

