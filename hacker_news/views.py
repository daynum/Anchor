from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
import json
from django.views.decorators.csrf import csrf_exempt

from . import fetch_rss_return_json

# Create your views here.
@csrf_exempt
def index(request):
    return render(request, "hacker-news.html")

def get_news_for_topic(topic):
    return fetch_rss_return_json.get_top_hacker_news()

@csrf_exempt
def topic_page(request, topic):
    topic = request.POST["topic"]
    return JsonResponse({"news_list": get_news_for_topic(topic)[topic]})
