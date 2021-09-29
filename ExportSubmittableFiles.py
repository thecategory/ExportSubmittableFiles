from submittable_api_client.submittable_api_client import SubmittableAPIClient
import os
import json

TOKEN = "accc0e3c524d49308613f2ec9fe149f7"
USERNAME_EMAIL = "dk@thecategory.com"

def make_dirs():
  if not os.path.exists('files'):
      os.makedirs('files')
  if not os.path.exists('files/submissions'):
      os.makedirs('files/submissions')
  if not os.path.exists('files/history'):
      os.makedirs('files/history')

def save_submission_file(client, item):
    file = client.submission_file(item.submission_id, item.files[0].guid)
    file_name = "files/submissions/" + str(item.submission_id) + "_" + item.time_created[0:10] + "_" + item.submitter.first_name + "_" + item.submitter.last_name + "__" + item.files[0].file_name
    with open(file_name, 'wb') as f:
      f.write(file.content)
    return file_name

def save(client, res):
  db = []
  for item in res.items:
    submission_file_name = save_submission_file(client, item)
    hists = client.submission_history(item.submission_id)
    safe_title = item.title.replace('/', '_')
    file_name = str(item.submission_id) + "_" + item.submitter.first_name + "_" + item.submitter.last_name + "_" + safe_title + ".json"
    history = []
    print(file_name)
    for hist in hists.items:
          message = {"date": str(hist.history_date[0:18]), "message":str(hist.email_message)}
          history.append(message)
    content = {'submission_id':item.submission_id,
        'title':safe_title,
        'filename':submission_file_name,
        'history':history}
    with open("files/history/" + file_name, 'wb') as f:
      f.write(bytes(json.dumps(content), 'utf-8'))
    db.append(content)
  with open("db.json", 'wb') as f:
    f.write(bytes(json.dumps(db), 'utf-8'))
  
def export(client):
  res = client.submissions(per_page=100000,  direction="desc")
  save(client, res)
  for page_num in range(res.total_pages):
      print(page_num)
      res = client.submissions(per_page=100000,  direction="desc", page=page_num + 1)
      save(res)

def main():
  client = SubmittableAPIClient(username=USERNAME_EMAIL, apitoken=TOKEN)
  make_dirs()
  export(client)

main()

