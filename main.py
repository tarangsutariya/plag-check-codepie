import requests
import json
authcode = 'Token 602e6e507b8eece6c68db86663866e76,Token 602e6e507b8eece6c68db86663866e76'
team_id = 1
probs = []
debug = True
print("enter problem ids : ")
curr = input()
while(curr!="-1"):
    probs.append(curr)
    curr=input()
webapp = "172.16.102.197"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://classroom.codingninjas.com/',
    'Origin': 'https://classroom.codingninjas.com',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'Authorization': authcode,
    'Connection': 'keep-alive',
}

params = {
    'problem_id': None,
    'offering_id': '1214669',
    'cv_id': '7183',
}

for prb in probs:
    params["problem_id"]=prb
    response = requests.get('https://api.codingninjas.com/api/v2/problem', params=params, headers=headers)
    res = response.json()
    for submission in res["data"]["problem"]["previous_submissions"]:
        if submission["is_best"] or debug:
            headers_submission = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'en-US,en;q=0.5',
            # 'Accept-Encoding': 'gzip, deflate, br',
            'Referer': 'https://classroom.codingninjas.com/',
            'Origin': 'https://classroom.codingninjas.com',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'Authorization': authcode,
            'Connection': 'keep-alive',
        }

            params_submission = {
                'submission_id': None,
            }
            params_submission["submission_id"]=submission["id"]
            sub = requests.get('https://api.codingninjas.com/api/v2/submitted_code', params=params_submission, headers=headers_submission)
            sub_details = sub.json()

            sub = {}
            sub["team_id"]=str(team_id)
            sub["prb_id"]=prb
            sub["code"] = (sub_details['data']['code_text'])
            if sub_details['data']["language_token"] == "py3":
                sub["lang"]="python"
            elif sub_details['data']["language_token"] == "java":
                sub["lang"]="java"
            elif sub_details['data']["language_token"] == "cpp":
                sub["lang"]="cpp"
            else:
                print("UNKNOWN LANGUAGE CODE")
                exit(0)
            json_data = json.dumps(sub)
            headers_flask = {'Content-type': 'application/json'}
            response = requests.post('http://%s:5000/post'%(webapp), data=json_data, headers=headers_flask)

            








# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/112.0',
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'en-US,en;q=0.5',
#     # 'Accept-Encoding': 'gzip, deflate, br',
#     'Referer': 'https://classroom.codingninjas.com/',
#     'Origin': 'https://classroom.codingninjas.com',
#     'Sec-Fetch-Dest': 'empty',
#     'Sec-Fetch-Mode': 'cors',
#     'Sec-Fetch-Site': 'same-site',
#     'Authorization': authcode,
#     'Connection': 'keep-alive',
# }

# params = {
#     'submission_id': '104710448',
# }




# response = requests.get('https://api.codingninjas.com/api/v2/submitted_code', params=params, headers=headers)

