import app
sample_event_json = {'id': 'Y2lzY29zcGFyazovL3VzL1dFQkhPT0svNzY0ZjZiMmYtNmJiNC00MDQ5LTk0MjMtOTcyNWMxMTgyY2Fj', 'name': 'Sample_Lambda', 'targetUrl': 'https://s180oeyv4f.execute-api.us-east-1.amazonaws.com/Test_Stage/test_webex', 'resource': 'messages', 'event': 'created', 'orgId': 'Y2lzY29zcGFyazovL3VzL09SR0FOSVpBVElPTi8xZWI2NWZkZi05NjQzLTQxN2YtOTk3NC1hZDcyY2FlMGUxMGY', 'createdBy': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS85NGQ2YzdkZS1iMjc1LTQ1NTktYWJlNC0wNTZlN2JmNDQxZDA', 'appId': 'Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OL0MzMmM4MDc3NDBjNmU3ZGYxMWRhZjE2ZjIyOGRmNjI4YmJjYTQ5YmE1MmZlY2JiMmM3ZDUxNWNiNGEwY2M5MWFh',
                     'ownedBy': 'creator', 'status': 'active', 'created': '2022-08-30T20:46:38.551Z', 'actorId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kNTIwYWEyOC1mMDY2LTRkYjUtYTU5NS1lN2M5NDk5MjE3Yzc', 'data': {'id': 'Y2lzY29zcGFyazovL3VzL01FU1NBR0UvOGMxN2NjMjAtMjhhOC0xMWVkLTllMDktMTNmZDcwMmUxNzFk', 'roomId': 'Y2lzY29zcGFyazovL3VzL1JPT00vOTQ1OGRkNDAtODIwMi0xMWVjLTg1NjctMGQ1NDk0YTFlNWEy', 'roomType': 'direct', 'personId': 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS9kNTIwYWEyOC1mMDY2LTRkYjUtYTU5NS1lN2M5NDk5MjE3Yzc', 'personEmail': 'coangel@cisco.com', 'created': '2022-08-30T21:13:08.834Z'}}

app.main(sample_event_json, {})