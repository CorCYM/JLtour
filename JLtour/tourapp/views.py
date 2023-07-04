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
    
    
    
def cartView(request) :
    ### request 데이터 받아오기
    if request.method == "POST" :
        cart_no = request.POST["cart_no"]
        cart_prod = request.POST["cart_prod"]

    elif request.method == "GET" :
        cart_no = request.GET["cart_no"]
        cart_prod = request.GET["cart_prod"]
        
### 한건 조회하기(상세)
# - get(Cart.cart_no = 전달받은 request 값)
# select * from cart
# Where cart_no = request.cart_no값
#   And cart_prod = request.car_prod값
    cart = Cart.objects.get(cart_no = cart_no,
                                 cart_prod = cart_prod)
    
    return render(request, 
                  "oracleapp/cart/cart_view.html",
                  {"cart_no": cart_no, "cart_prod":cart_prod, "cart": cart })
    

    