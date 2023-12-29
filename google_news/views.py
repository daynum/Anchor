from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt

from . import fetch_rss_return_json

# Create your views here.
@csrf_exempt
def index(request):
    # suppose we fetched here from DB what topics and search queries, user had added to their account
    # we need all that topics and search queries and then fetch news for all of them here, top news also if needed
    # and then send that whole dict to template webpage to display nicely.

    # For now I'm hardcoding 2 topics and 2 search terms along with top news
    pull_news_for = {
        "topics": ["technology", "science"],
        "search_terms": ["open_ai", "world news"],
        "defaults": ["top_news"],
    }

    # having dummy data to not call api again and again
    data = {}
    data["all_topics"] = ["technology", "open_ai", "world_news", "science", "india", "nation"]
    data["top_news"] = get_news_for_topic(topic="top_news")["top_news"]
    print(data.keys())
    return render(request, "google-news.html", data)

def get_news_for_topic(topic):
    return fetch_rss_return_json.get_news_by_topic(topic_name=topic)

@csrf_exempt
def topic_page(request, topic):
    # it needs topic and news data

    ## TO-DO: Birng JSON data here, can't be done with HTML only 
    topic = request.POST["topic"]

    return JsonResponse({"news_list": get_news_for_topic(topic)[topic]})