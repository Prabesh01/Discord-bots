import requests

line34=requests.post('https://jsonblob.com/api/jsonBlob', data='{ "hooks": "", "channel":"" }', headers={"Content-Type": "application/json", "Accept": "application/json"})
print('Keep this in line 34:')
print('blob = "'+line34.headers['Location']+'"')
print('')
line35=requests.post('https://jsonblob.com/api/jsonBlob', data='{"guild": "hoook"}', headers={"Content-Type": "application/json", "Accept": "application/json"})
print('Keep this in line 35:')
print('blobre = "'+line35.headers['Location']+'"')
print('')
line36=requests.post('https://jsonblob.com/api/jsonBlob', data='{"oa": ""}', headers={"Content-Type": "application/json", "Accept": "application/json"})
print('Keep this in line 36:')
print('bloboa = "'+line36.headers['Location']+'"')
print('')
line37=requests.post('https://jsonblob.com/api/jsonBlob', data='{"r": ""}', headers={"Content-Type": "application/json", "Accept": "application/json"})
print('Keep this in line 37:')
print('blobr = "'+line37.headers['Location']+'"')