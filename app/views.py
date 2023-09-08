from django.shortcuts import render
from app.models import *
from django.db.models import Q

# Create your views here.
def display_topics(request):
    QSTO=Topic.objects.all()

    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)
def display_webpage(request):
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter(pk=5)
    QSWO=webpage.objects.filter(topic_name='cricket')
    QSWO=webpage.objects.exclude(topic_name='cricket')
    QSWO=webpage.objects.all()[4:5:1]
    QSWO=webpage.objects.all().order_by('name')
    QSWO=webpage.objects.filter(topic_name='cricket').order_by('name')
    QSWO=webpage.objects.all().order_by('-name')
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter(name__startswith='k')
    QSWO=webpage.objects.filter(url__endswith='com')
    QSWO=webpage.objects.filter(url__contains='y')
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter(Q(name__startswith='k')& Q(url__endswith='com'))
    QSWO=webpage.objects.filter(Q(name__startswith='k')& Q(url__contains='g'))
    QSWO=webpage.objects.filter(Q(name__startswith='k')|Q(url__endswith='com'))
    QSWO=webpage.objects.filter(Q(name__startswith='p')& Q(url__endswith='com'))
    QSWO=webpage.objects.filter(Q(name__startswith='p')|Q(url__endswith='com'))
    QSWO=webpage.objects.filter(Q(name__startswith='p')|Q(url__contains='1'))
    QSWO=webpage.objects.all()
    QSWO=webpage.objects.filter(Q(topic_name='cricket')& Q(name__endswith='1'))

    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    QSARO=AccessRecord.objects.all()
    QSARO=AccessRecord.objects.filter(date='2023-08-01')
    QSARO=AccessRecord.objects.filter(date__gt='2023-08-01')
    QSARO=AccessRecord.objects.filter(date__lte='2023-08-01')
    QSARO=AccessRecord.objects.filter(date__year='2023')
    QSARO=AccessRecord.objects.filter(date__month='02')
    QSARO=AccessRecord.objects.filter(date__day='03')

    d={'QSARO':QSARO}
    return render(request,'display_accessrecord.html',d)

def insert_topics(request):
    topic_name=input('Enter topic_name: ')
    To=Topic.objects.get_or_create(topic_name=topic_name)[0]
    To.save()
    QSTO=Topic.objects.all()
    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)
def insert_webpage(request):
    tn=input('enter topic_name: ')
    na=input('enter name: ')
    ur=input('enter url: ')

    To=Topic.objects.get(topic_name=tn)

    wo=webpage.objects.get_or_create(topic_name=To,name=na,url=ur)[0]
    wo.save()
    QSWO=webpage.objects.all()
    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)
    

def insert_AccessRecord(request):
    pk=(input('enter pk here: '))
    wo=webpage.objects.get(pk=pk)
    wo.save()
    da=input('enter date: ')
    au=input('enter athor: ')
    Ao=AccessRecord.objects.get_or_create(name=wo,date=da,author=au)[0]
    Ao.save()
    QSARO=AccessRecord.objects.all()
    d={'QSARO':QSARO}
    return render(request,'display_accessrecord.html',d)

def update_webpage(request):
    webpage.objects.filter(name='kalyan').update(url='https://kalyan.in')
    webpage.objects.filter(name='polu').update(url='https://polu.in')
    CTO=webpage.objects.get(topic_name='cricket')
    webpage.objects.filter(name='polu').update(topic_name=CTO)
    QSWO=webpage.objects.all()

    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)
