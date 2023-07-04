from django.shortcuts import render
from django.http import HttpResponse
from .models import City, Detail

# Create your views here.
def home(request):
    msg = "<h3>Home이 보이냐?</h3>"
    return HttpResponse(msg)

def index(request) :
    return render(request,
                  "tourapp/index.html",
                  {})
    
def index(request) :
    return render(request,
                  "tourapp/index.html",
                  {})
    
def result(request) :
    return render(request,
                  "tourapp/result.html",
                  {})

    
def testing(request) :
    return render(request,
                  "tourapp/testing.html",
                  {})
    
def getCityList(request) :
    city_list  = City.objects.all()

    return render(request,
                  "tourapp/city.html",
                  {'city_list' : city_list})
    
def getDetailList(request) :
    detail_list = Detail.objects.all()
    return render(request,
                  "tourapp/detail.html",
                  {'detail_list' : detail_list})
    
def select(request) :
    return render(request,
                  "tourapp/select.html",
                  {})
    
def citycheck1(request) :
    
    if request.method == "POST" :
        citynumber = request.POST["citynumber"]

    elif request.method == "GET" :
        citynumber = request.GET["citynumber"]
        
    citycheck = City.objects.get(citynumber=citynumber)    
    
    return render(request,
                  "tourapp/citycheck1.html",
                  {"citynumber": citynumber, "citycheck" : citycheck})

def citydetailJoin(request) :
    
    citydetail = Detail.objects.select_related()
                                                                    
    return render(request,
                  "tourapp/citycheck2.html",
                  {"citydetail":citydetail})
    
def citydetailJoincheck(request) :
    
    if request.method == "POST" :
        citynumber = request.POST["citynumber"]

    elif request.method == "GET" :
        citynumber = request.GET["citynumber"]
    
    citydetailcheck = Detail.objects.select_related().filter(location__citynumber=citynumber)
                                                                    
    return render(request,
                  "tourapp/citycheck3.html",
                  {"citydetailcheck":citydetailcheck, 
                   "sql" : citydetailcheck.query})
    
def resultcheck(request) :
    
    if request.method == "POST" :
        totalScore = request.POST["totalScore"]

    elif request.method == "GET" :
        totalScore = request.GET["totalScore"]
    
    citydetailcheck = Detail.objects.select_related().filter(location__citynumber=totalScore)                                      
    return render(request,
                  "tourapp/result.html",
                  {"citydetailcheck":citydetailcheck, 
                   "sql" : citydetailcheck.query})
    
def JLtour2(request) :
    return render(request,
                    "tourapp/JLtour2.html",
                    {}) 
    
def profile(request) :
    return render(request,
                    "tourapp/profile.html",
                    {}) 
    
def calendar(request) :
    return render(request,
                    "tourapp/calendar.html",
                    {}) 