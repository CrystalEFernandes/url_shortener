from django.shortcuts import render
from .utils import generate_alias
from datetime import timedelta
from django.utils.timezone import now
from django.http import JsonResponse,HttpResponseBadRequest,HttpResponseRedirect,HttpResponseNotFound
import json

url_mapping={}
ttl_mapping={}
analytics_mapping={}

# Create your views here.
def shorten_url(request):
    if request.method=='POST':
        long_url=request.POST.get('long_url')
        custom_alias=request.POST.get('custom_alias')
        ttl_seconds=int(request.POST.get('ttl_seconds',120))
        alias=generate_alias(long_url,custom_alias)
        expiration_time=now()+timedelta(seconds=ttl_seconds)
        url_mapping[alias]=long_url
        ttl_mapping[alias]=expiration_time
        analytics_mapping[alias]={'access_count':0,'access_times':[]}

        return JsonResponse({'short_url':f'http://localhost:8000/{alias}'})
    return HttpResponseBadRequest()

def redirect_to_long_url(request,alias):
    if alias in url_mapping and now()<ttl_mapping[alias]:
        analytics_mapping[alias]['access_count'] += 1
        analytics_mapping[alias]['access_times'].append(now().isoformat())

        return HttpResponseRedirect(url_mapping[alias])
    return HttpResponseNotFound("expired or doesnt exist")

def get_analytics(request,alias):
    if alias in analytics_mapping and now()<ttl_mapping[alias]:
        return JsonResponse({
            "alias":alias,
            "long_url":url_mapping[alias],
            "access_count":analytics_mapping[alias]['access_count'],
            "access_time":analytics_mapping[alias]['access_times'],
        })
    return HttpResponseNotFound("expired or doesnt exist")

def update_url(request, alias):
    if request.method == 'PUT':
        if alias in url_mapping and now() < ttl_mapping[alias]:
            try:
                data = json.loads(request.body)
                custom_alias = data.get('custom_alias')
                ttl_seconds = int(data.get('ttl_seconds', (ttl_mapping[alias] - now()).total_seconds()))

                if ttl_seconds <= 0:
                    return HttpResponseBadRequest("expired")

                if custom_alias and custom_alias != alias:
                    if custom_alias in url_mapping:
                        return HttpResponseBadRequest("Custom alias already in use.")
                    url_mapping[custom_alias] = url_mapping.pop(alias)
                    ttl_mapping[custom_alias] = ttl_mapping.pop(alias)
                    analytics_mapping[custom_alias] = analytics_mapping.pop(alias)
                    alias = custom_alias

                expiration_time = now() + timedelta(seconds=ttl_seconds)
                ttl_mapping[alias] = expiration_time

                return JsonResponse({'status': 'success'})
            except (ValueError, KeyError):
                return HttpResponseBadRequest("Invalid data provided.")
        
        return HttpResponseNotFound("expired or doesnt exist")
    
    return HttpResponseBadRequest("invalid")


def delete_url(request,alias):
    if request.method=='DELETE':
        if alias in url_mapping:
            del url_mapping[alias]
            del ttl_mapping[alias]
            del analytics_mapping[alias]
            return JsonResponse({'status':'deleted'})
    return HttpResponseBadRequest()