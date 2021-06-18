import requests
import json
import sys
from iicsRestAPIFunc import get_session_id, JSON_HEADERS, get_job_list
from exportByExcel import exportExcelFile
from jsonMerge import jsonMerge

def main ():
    username = 'username@iics.co.kr'
    password = 'passw@rd'
    taskTypeList = ['DMASK', 'DRS', 'DSS', 'MTT', 'PCS']


    login_response = get_session_id(username, password)
    session_id = login_response[0]
    server_url = login_response[1]

    JSON_HEADERS['icSessionId']=session_id

    task_lists = None
    for taskType in taskTypeList:
        json_task_list = get_job_list(session_id, server_url, taskType)
        task_lists = jsonMerge(json_task_list, task_lists)

    
    exportExcelFile(task_lists)
    #start_job(session_id, server_url, taskId, taskType)

main()