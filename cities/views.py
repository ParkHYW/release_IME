# cities/views.py

from django.shortcuts import render,get_object_or_404
from django.views.generic import TemplateView, ListView
from django.db.models import Q
from .models import *
from django.core.paginator import Paginator

# Create your views here.
class HomePageView(TemplateView):
    template_name= 'home.html'

class SearchResultsView(ListView):
    model = Search
    template_name = 'search_results.html'
    def get_queryset(self): # new
        query = self.request.GET.get('q')
        object_list = Search.objects.filter(
            Q(term__icontains=query) 
        )
        return object_list
# 페이지 연결



# 카테고리별 연결

def analytic(request):
    analytics = Analytics.objects.all()
    paginator = Paginator(analytics, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'analytics' : analytics,
        'posts':posts,

    }
    return render(request, 'detail/analy_main.html', context)



def analytics(request, id):
    detail_data = get_object_or_404(Analytics, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
        'href':detail_data.href,
        'firstkeyword': detail_data.firstkeyword,
        'secondkeyword': detail_data.secondkeyword,
        'lastkeyword': detail_data.lastkeyword,
    }
    return render(request, 'detail/Analytics.html', context)



# 카테고리별 연결
def myAnthropometry(request):
    anthropometrys = Anthropometry.objects.all()
    paginator = Paginator(anthropometrys, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'anthropometrys' : anthropometrys,
        'posts':posts,
    }
    return render(request, 'detail/Anthro_main.html', context)

def myAnthropometrys(request, id):
    detail_data = get_object_or_404(Anthropometry, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
        'href':detail_data.href,
        'firstkeyword': detail_data.firstkeyword,
        'secondkeyword': detail_data.secondkeyword,
        'lastkeyword': detail_data.lastkeyword,
    }
    return render(request, 'detail/Anthro.html', context)

# 카테고리별 연결
def myComputer(request):
    Computers = Computer.objects.all()
    paginator = Paginator(Computers, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'Computers' : Computers,
        'posts':posts,
    }
    return render(request, 'detail/computer_main.html', context)
def myComputers(request, id):
    detail_data = get_object_or_404(Computer, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
        'href':detail_data.href,
        'firstkeyword': detail_data.firstkeyword,
        'secondkeyword': detail_data.secondkeyword,
        'lastkeyword': detail_data.lastkeyword,
    }
    return render(request, 'detail/Computer.html', context)

    # 카테고리별 연결
def myDistribution(request):
    Distributions = Distribution.objects.all()
    paginator = Paginator(Distributions, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'Distributions' : Distributions,
        'posts':posts,
    }
    return render(request, 'detail/Distribution_main.html', context)

def myDistributions(request, id):
    detail_data = get_object_or_404(Distribution, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
        'href':detail_data.href,
        'firstkeyword': detail_data.firstkeyword,
        'secondkeyword': detail_data.secondkeyword,
        'lastkeyword': detail_data.lastkeyword,
    }
    return render(request, 'detail/Distributions.html', context)

#
def myHuman(request):
    Humans = Human.objects.all()
    paginator = Paginator(Humans, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'Humans' : Humans,
        'posts':posts,
    }
    return render(request, 'detail/Human_main.html', context)
def myHumans(request, id):
    detail_data = get_object_or_404(Human, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
        'href':detail_data.href,
        'firstkeyword': detail_data.firstkeyword,
        'secondkeyword': detail_data.secondkeyword,
        'lastkeyword': detail_data.lastkeyword,
    }
    return render(request, 'detail/Humans.html', context)

# 카테고리별 연결
def myManagement(request):
    Managements = Management.objects.all()
    paginator = Paginator(Managements, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    context = {
        'Managements' : Managements,
        'posts':posts,
    }
    return render(request, 'detail/Management_main.html', context)
def myManagements(request, id):
    detail_data = get_object_or_404(Management, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
        'href':detail_data.href,
        'firstkeyword': detail_data.firstkeyword,
        'secondkeyword': detail_data.secondkeyword,
        'lastkeyword': detail_data.lastkeyword,
    }
    return render(request, 'detail/Managements.html', context)

# 카테고리별 연결
def myManufacturing(request):
    Manufacturings = Manufacturing.objects.all()
    paginator = Paginator(Manufacturings, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'Manufacturings' : Manufacturings,
        'posts':posts,
    }
    return render(request, 'detail/Manufacturing_main.html', context)
def myManufacturings(request, id):
    detail_data = get_object_or_404(Manufacturing, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
        'href':detail_data.href,
        'firstkeyword': detail_data.firstkeyword,
        'secondkeyword': detail_data.secondkeyword,
        'lastkeyword': detail_data.lastkeyword,
    }
    return render(request, 'detail/Manufacturings.html', context)

# 카테고리별 연결
def myOperation(request):
    Operations = new_Operations.objects.all()
    paginator = Paginator(Operations, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    context = {
        'Operations' : Operations,
        'posts':posts,
    }
    return render(request, 'detail/Operation_main.html', context)
def myOperations(request, id):
    detail_data = get_object_or_404(new_Operations, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
        'href':detail_data.href,
        'firstkeyword': detail_data.firstkeyword,
        'secondkeyword': detail_data.secondkeyword,
        'lastkeyword': detail_data.lastkeyword,
    }
    return render(request, 'detail/Operations.html', context)

# 카테고리별 연결
def myQuality(request):
    Qualitys = Quality.objects.all()
    paginator = Paginator(Qualitys, 6)
    page = request.GET.get('page')
    posts = paginator.get_page(page)    
    context = {
        'Qualitys' : Qualitys,
        'posts':posts,
    }
    return render(request, 'detail/Quality_main.html', context)
def myQualitys(request, id):
    detail_data = get_object_or_404(Quality, pk=id)
    context = {
        'term' : detail_data.term,
        'meaning' : detail_data.meaning,
        'href':detail_data.href,
        'firstkeyword': detail_data.firstkeyword,
        'secondkeyword': detail_data.secondkeyword,
        'lastkeyword': detail_data.lastkeyword,
    }
    return render(request, 'detail/Qualitys.html', context)