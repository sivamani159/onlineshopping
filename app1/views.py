from django.shortcuts import render

# Create your views here.

def home(request):
    data={'msg':'this is homepage'}
    return render(request,'app1/home.html',data)

def ajio(request):
    category=['MEN','WOMEN','KIDS']
    data={'category':category}
    return render(request,'app1/ajio.html',data)
    
def gopaldigitals(request):
    items=['LAPTOPS','MOBILES','TELEVISIONS','ACCESORIES']
    data={'items':items}
    return render(request,'app1/gopaldigitals.html',data)
    
