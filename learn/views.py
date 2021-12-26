from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Topic, Entry
from .forms import Topicform, Entryform
from .models import Entry
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404


def index(request):
    return render(request, 'index.html')


def vccd(request):
    return render(request, 'base.html')

@login_required()
def topics(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)

@login_required()
def topic(request, topic_id):
    topics = Topic.objects.get(id=topic_id)
    if topics.owner != request.user:
        raise Http404
    entries = topics.entries.all()
    # entries = topic.entry_set.order_by('-date_added')
    context = {'topics': topics, 'entries': entries}
    return render(request, 'topic.html', context)

@login_required()
def new_topic(request):
    if request.method != 'POST':
        form = Topicform()
    else:
        form = Topicform(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
           # return HttpResponseRedirect('learn:topics')
            return HttpResponseRedirect(reverse('learn:topics'))
            #return render( request,"topics.html")
    cotext = {'form': form}
    return render(request, 'new_topic.html', cotext)

@login_required()
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = Entryform()
    else:
        form = Entryform(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learn:topic1', args=[topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'new_entry.html', context)

@login_required()
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = Entryform(instance=entry)
    else:
        form = Entryform(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learn:topic1',args=[topic.id]))
    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'edit_entry.html', context)


@login_required()
def del_top(request,del_id):
    ac = Topic.objects.filter(id=del_id).delete()
    return HttpResponseRedirect("topics")
   #return render(request,'demo.html')