import requests
import re 

def list_topics(re_pattern=None):
    admin_url ='http://localhost:8080/admin'

    topics = requests.get(f"{admin_url}/v2/persistent/public/default").json()

    if re_pattern:
        filtered_topics = [topic for topic in topics if re.match(re_pattern, topic)]
        return filtered_topics
    else:
        return topics