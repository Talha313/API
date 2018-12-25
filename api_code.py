import sys
import requests
#import util
import os
import random
import getpass
#import samples
import sys, json

session_requests = requests.session()

def log_in(base_url, username, password):

    global session_requests
    headers = {'Content-type': 'application/x-www-form-urlencoded'}

    print('Get token:')
   # content = {username}&password={password}&grant_type=password
    content = 'username={0}&password={1}&grant_type=password'.format(username, password)
   # token_entity = requests.post(base_url + 'token', data=content).json()
    token_entity = session_requests.post(base_url, data=content, headers=headers).json()
  #  print(content)
   # print(token_entity)
    return  token_entity


def get_data(token_entity):
    global session_requests
    headers = {'Content-type': 'application/json, text/json'}

    token = token_entity['access_token']
   # print(token)

    url="https://dataapi.octoparse.com/api/alldata/GetDataOfTaskByOffset?taskId=2cb7f2de-eef8-4c26-8324-a192b81b1e2b&offset=0&size=1000"
    data=session_requests.get(url,headers={'Authorization': 'bearer ' + token})
    print(data.text)

if __name__ == '__main__':
     #if len(sys.argv) < 2:
      #   print('Please sepecify your username!')
       # os._exit(-1)
    #
    #user_name = sys.argv[1]
    #password = getpass.getpass('Password:')

    base_url = 'https://dataapi.octoparse.com/token'
    #base_url='http://dataapi.octoparse.com/help'
    token_entity=log_in(base_url,  'designsdw' , 'u3v89Dnf8')
    #print(token_entity)
    token=token_entity['access_token']
    print(token)
    get_data(token_entity)

    #start_test(base_url, token_entity)