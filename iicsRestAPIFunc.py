import requests
import json
import sys


JSON_HEADERS={'Content-Type': 'application/json; charset=utf-8', 'Accept': 'application/json; charset=utf-8'}

def get_session_id(username, password):
    '''Authenticate with username and password and
       retrieve icSessionId and serverUrl that are used for Subsequent API calls'''
    session_id = ''
    data = {'@type': 'login', 'username': username, 'password': password}
    url = "https://dm-ap.informaticacloud.com/ma/api/v2/user/login"
    headers = {'Content-Type':'application/json', 'Accept':'application/json'}
    # We need to pass data in string instead of dict so that the data gets posted directly.
    r = requests.post(url, data=json.dumps(data), headers=headers)

    print('API Response Status Code: ' + str(r.status_code))

    if r.status_code == 200:
        print('login has been successfully')
        session_id = r.json()["icSessionId"]
        server_url = r.json()["serverUrl"]
        print('Session Id: ' + session_id)
    else:
        print('Login API call failed:')
        print(r.headers)
        print(r.json())
        sys.exit(1)

    return session_id, server_url

def get_job_list(session_id, server_url, taskType):
    '''Use Session Id and Server URL from the user login API 
       and find the job list'''
    url = server_url + "/api/v2/task"
    data = {'type':taskType}
    r = requests.get(url, params=data, headers=JSON_HEADERS)

    if r.status_code == 200:
        print (r.json())

        if len(r.json()) > 0:
            print('Job list have been successfully find and listed')
            return r.json()
        else:  
            print('Job list have been successfully but no rows')
            return None
    else:
        print('Job failed to find with status: ' + str(r.status_code))
        print(r.content)

def start_job(session_id, server_url, taskId, taskType):
    '''Use Session Id and Server URL from the user login API 
       and start the specified job'''
    url = server_url + "/api/v2/job"
    data = {'@type':'job', 'taskId':taskId, 'taskType':taskType}
    r = requests.post(url, data=json.dumps(data), headers=JSON_HEADERS)

    if r.status_code == 200:
        print('Job has been successfully started')
        print(r.headers)

    else:
        print('Job failed to start with status: ' + str(r.status_code))
        print(r.content)

""" 
def main ():
    username = 'iicsusername@iics.co.kr'
    password = 'passw@rd'
    taskId = '0001Z2Z000000011115' # example ) Explorer -> Mapping Task -> properties -> SAAS Task ID:
    taskType = 'MTT' #MTT-Mapping configuration task. DRS-Data replication task. DSS-Data synchronization task.



    login_response = get_session_id(username, password)
    session_id = login_response[0]
    server_url = login_response[1]

    JSON_HEADERS['icSessionId']=session_id

    get_job_list(session_id, server_url, taskType)
    #start_job(session_id, server_url, taskId, taskType)

main()
""" 