from django.http import response
from django.shortcuts import render
import json
from django.conf import settings
import redis
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response

# Connecting to redis instance
redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0)


@api_view(['GET'])
def stock_data(request):
    if request.method == 'GET':
        data = []
        count = 0
        for key in redis_instance.keys("*"):
            try:
                data.append(
                    json.loads(redis_instance.get(key)))
                count += 1
            except Exception as e:
                print(e)
                continue
        date = redis_instance.get("DATE")
        response = {
            "count": count,
            "msg": f"Found {count} items.",
            "date": date,
            "data": data
        }
        return Response(response, status=200)
