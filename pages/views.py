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

# support
def support_inquiry(request):
    return render(request, 'pages/support/inquiry.html')

def support_feedback(request):
    return render(request, 'pages/support/feedback.html')

# faqs
def faqs_company(request):
    return render(request, 'pages/faqs/company.html')

def faqs_product(request):
    return render(request, 'pages/faqs/product.html')