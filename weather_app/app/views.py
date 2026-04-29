from django.shortcuts import render
from django.http import JsonResponse
import json
import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Create your views here.
def weather(request):
    if request.method == 'POST':

        data = json.loads(request.body)

        lat = data.get('lat')
        lon = data.get('log')

        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={os.getenv("API_KEY")}'

        res = requests.get(url)
        return JsonResponse(res.json())
    return render(request,'main.html')