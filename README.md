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

# LICENSE

MIT THING, NO GUARANTEE, JUST A SMALL HACK, HOPE YOU FIND IT USEFUL.

