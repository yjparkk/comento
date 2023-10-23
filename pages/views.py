from django.shortcuts import render

# mainpage
def mainpage(request):
    return render(request, 'pages/mainpage.html')

# about
def company_info(request):
    return render(request, 'pages/about/info.html')

def company_mission(request):
    return render(request, 'pages/about/vision-mission.html')

def company_map(request):
    return render(request, 'pages/about/map.html')

#about