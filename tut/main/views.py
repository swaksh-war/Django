from django.shortcuts import render,HttpResponse

# Create your views here.
def base(response):
    return render(response,'main/base.html')

def about(response):
    return render(response,'main/about.html')

def home(response):
    return render(response,'main/home.html')

def userprofile(response):
    
    # backend
    game = response.GET.get("game",None)
    hoursplayed = response.GET.get("hoursplayed",0)
    
    djlist=[]
    for x in range(10):
        y={
            "game" : game,
            "hoursplayed" : hoursplayed
        }
        djlist.append(y)
    
    # data to frontend
    djuserprofile={
        "djlist":djlist
    }
    
    print(djuserprofile)
    
    return render(response,'main/userprofile.html',djuserprofile)

