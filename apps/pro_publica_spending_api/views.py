from django.shortcuts import render, redirect
import requests

# Create your views here.
def index(request):
    url = ("https://projects.propublica.org/free-the-files/markets.json")
    response = requests.get(url)
    print("Response: " + str(response))
    spending = response.json()
    print("Spending: " + str(spending))
    sorted_spending = sorted(spending)
    context = {
        'response': response,
        'spending': spending,
        'sorted_spending': sorted_spending,
    }
    return render(request, 'pro_publica_spending_api/index.html', context)

def comms(request):
    url = ("https://projects.propublica.org/free-the-files/committees.json")
    response = requests.get(url)
    print("Response: " + str(response))
    comms = response.json()
    print("Committees: " + str(comms))
    context = {
        'response': response,
        'comms': comms,
    }
    return render(request, 'pro_publica_spending_api/comms.html', context)