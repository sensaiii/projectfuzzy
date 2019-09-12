from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse
from .sort import search,sorting,wordlist
import json
# Create your views here.
#view to render form to enter thr desired word
def searchview(request):
    context={}
    return render(request,'search/searchview.html',context)

#checks the apalhabets or words enterd  are in wordlist in realtime
def autocomplete(request):
    if request.is_ajax():
        query=request.Get.get('term','')
        results=sorting(search(query.lower()),query.lower())
        data=json.dumps(results)
    else:
        data='fail'
    type='application/json'
    return HttpResponse(data,type)
#retuns a json response of result of top 25 values conatining searched partial word
def getSearchResults(request):
    if request.method == 'GET':
        query = request.GET.get('term')  # for example: query = 'hello'
        if query:
            if len(search(query.lower())):
                searchResult = sorting(search(query.lower()), query.lower())
            elif len(search(query.lower())) == 0:
                return JsonResponse({'Search_Result': "Word not found."})
            else:
                return JsonResponse({'Search_Result': searchResult})
        else:
            return redirect('/')
