from django.shortcuts import render

# Create your views here.
def staticdata(request):
    print("hhelo")
    my_d={'name':'Sidhesh','loc':'pune','age':22}
    return render(request,'testapp/index.html',my_d)