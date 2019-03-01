'''
Using this as a base-line test of python and calling on APIs using python. 
Main source for this tut: https://www.dataquest.io/blog/python-api-tutorial/
'''
import requests

#Make a request to get the latest position of the IIS

response = requests.get("http://api.open-notify.org/iss-now.json")

# Print the status code of the response
print(response.status_code)