import requests

url = "https://webexapis.com/v1/webhooks"

payload="{\n      \"resource\" : \"messages\",\n      \"event\" : \"created\",\n      \"filter\" : \"roomId=Y2lzY29zcGFyazovL3VybjpURUFNOnVzLXdlc3QtMl9yL1JPT00vMWU0N2RlMTAtNTlkMy0xMWViLWE5MDctYWY0YTgzMDVmMWFj\",\n      \"targetUrl\" : \"https://fd91ea31ee89.ngrok.io\",\n      \"name\" : \"WebEx Team Learning Lab Webhook\"\n  }"
headers = {
  'Authorization': 'Bearer ODZhNjhmNjUtMzE5YS00YzYyLWE3YTQtNzk0Nzg2NmMyYzJhNDRlNDkwYjctYjdl_P0A1_4324cf20-3dc3-4497-af07-1b996464c625',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
