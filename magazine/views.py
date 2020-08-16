from django.shortcuts import render

# landing page view
def landingPage(request):
    context = {}
    return render(request, 'magazine/index.html', context)

# about page view
def aboutPage(request):
    context = {}
    return render(request, 'magazine/about.html', context)

# article page view
def articlepage(request):
    context = {}
    return render(request, 'magazine/article.html', context)