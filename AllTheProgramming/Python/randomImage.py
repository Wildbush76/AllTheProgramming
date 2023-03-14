from googleapiclient.discovery import build
from urllib import request
import random
api = "AIzaSyDi2Ja7tZ62TtHBHSL56JMbytWf6WYMtJQ"
cse = "f09cc7c37953d4b57"

def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']
with open("search.txt","w") as file:
    sear = google_search("sexy obama",api,cse, searchType = "image",start = random.randint(0,99))
    url = sear[0]['link']
    print(url)
    response = open(request.urlretrieve(url)[0],"rb")
    with open("yes.jpg","wb") as file:           
        file.write(response.read())
    response.close()
