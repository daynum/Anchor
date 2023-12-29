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

def hacker_news_xml_parse_to_json(url, ):
    content = connect_to_url_download_data(url)
    xml_json_content = xmltodict.parse(content)
    news_list = xml_json_content['rss']['channel']['item']
    return news_list

def get_top_hacker_news():
    url = "https://news.ycombinator.com/rss"
    return {"top_news": hacker_news_xml_parse_to_json(url)}

if __name__ == "__main__":
    # url = "https://news.google.com/rss/"
    url = "https://news.ycombinator.com/rss"
    print(hacker_news_xml_parse_to_json(url))