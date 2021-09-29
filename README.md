# ExportSubmittableFiles
Small hacky python script to export files and history from Submittable.

# INSTALL
- Add the Submittable Python client:

```
pip3 install submittable_api_client
```

- In case you're using Python3, you'll need to change or comment out the old print statements from the Submittable API library (there are a few of these in the code):

```
# vi /usr/local/lib/python3.9/site-packages/submittable_api_client/submittable_api_client.py
...
query_uri = "%s%s" % (BASE_API_URI, CATEGORIES_URI)
# print query_uri
response = requests.get(query_uri, auth=(self.username, self.apitoken))
```

- Change the USERNAME and TOKEN variables in the script:

```
TOKEN = "you@example.com"
USERNAME_EMAIL = "FFFFFFFFF"
```

- Run the script:

```
ExportSubmittableFiles$ python3 ExportSubmittableFiles.py
```

- You'll have a list of JSONs of each history message at files/history that look like this:

```json
{"submission_id": 21352069, 
"title": "Submission Title", 
"filename": "files/submissions/21081169_2021-08-27_ae8cb2fe-f0b9-40c2-a861-ccea399dfeea_AUTHOR_NAME__DATE_Submission file name.docx", 
"history": [{"date": "2021-09-27T10:59:40", "message": "None"}, 
{"date": "2021-09-27T10:59:4", "message": "Hi ,<br /><br />Thank you... We have received your submission and look forward to reviewing it.<br/><br />Thanks!<br/>"}]}
```

- Submission files are at files/submissions (as stated in the history JSON "filename" section).

- Another db.json will contain all history values in one file (if you require quick import to another database).


# LICENSE

MIT THING, NO GUARANTEE, JUST A SMALL HACK, HOPE YOU FIND IT USEFUL.

