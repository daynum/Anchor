import requests
from xml.etree import ElementTree
import xmltodict
from xml.dom.minidom import parse, parseString
import json

def connect_to_url_download_data(url, headers=None, ):
    if not headers:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:101.0) Gecko/20100101 Firefox/101.0'}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    content = r.content.decode('utf-8')
    return content

def google_news_xml_parse_to_json(url, ):
    content = connect_to_url_download_data(url)
    xml_json_content = xmltodict.parse(content)
    news_list = xml_json_content['rss']['channel']['item']
    return news_list

def get_news_by_topic(topic_name, ):
    # MOCKING AWAY
    # with open("xml_api_data.json", "r", encoding='utf-8') as f:
    #     data = json.load(f)
    # return {topic_name: data['data'][topic_name]}

    url = ""
    if topic_name == "top_news":
        url = "https://news.google.com/rss/"
    elif topic_name.upper() in ["WORLD", "NATION", "BUSINESS", "TECHNOLOGY", "ENTERTAINMENT", "SPORTS", "SCIENCE", "HEALTH"]:
        # News by predefined topics
        url = "https://news.google.com/news/rss/headlines/section/topic/{}".format(topic_name)
    else:
        # News by query term
        url = "https://news.google.com/rss/search?q={}".format(topic_name)

    topic_name = topic_name.replace(' ', '_')
    return {topic_name: google_news_xml_parse_to_json(url)}

    #TODO: subscribe to custom topics
    custom_topic_id = {
        "TECHNOLOGY": "CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE",
    }
    custom_topic_url = "https://news.google.com/rss/topics/{}".format(topic_id[topic_name])

if __name__ == "__main__":
    # url = "https://news.google.com/rss/"
    url = "https://news.google.com/rss/topics/CAAqJQgKIh9DQkFTRVFvSUwyMHZNRE55YXpBU0JXVnVMVWRDS0FBUAE"
    google_news_xml_parse_to_json(url)