from django.shortcuts import render
from django.views.generic import TemplateView
import requests
from django.contrib import messages
from django.http import Http404
from django.http import HttpResponse




def home(request):
    try:
        count = 'all'
        url = "https://covid-193.p.rapidapi.com/statistics"
        querystring = {"country":count}
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "b1bf9d0c40mshdaf9e4c83043868p15144bjsn0440754bb25b"
            }

        response = requests.request("GET", url, headers=headers, params=querystring).json()

        data = response['response']

        d = data[0]

        print(d)

        context = {
            'all': d['cases']['total'],
            'recovered': d['cases']['recovered'],
            'deaths': d['deaths']['total'],
            'new': d['cases']['new'],
            'critical': d['cases']['critical']
        }
        return render(request, 'dashboard/index.html',context)
    except:
        raise Http404("Please enter a valid country!")
    

def getstats(request):
    url = "https://covid-193.p.rapidapi.com/statistics"
    count = request.GET['country']
    if count == None:
        messages.success(request, 'Your profile has been updated!')
        return render(request, 'dashboard/index.html')
    else:
        querystring = {"country":count}
        headers = {
            'x-rapidapi-host': "covid-193.p.rapidapi.com",
            'x-rapidapi-key': "b1bf9d0c40mshdaf9e4c83043868p15144bjsn0440754bb25b"
            }

        response = requests.request("GET", url, headers=headers, params=querystring).json()

        data = response['response']

        d = data[0]

        print(d)

        context = {
            'all': d['cases']['total'],
            'recovered': d['cases']['recovered'],
            'deaths': d['deaths']['total'],
            'new': d['cases']['new'],
            'critical': d['cases']['critical']
        }
    return render(request, 'dashboard/result.html',context)  

