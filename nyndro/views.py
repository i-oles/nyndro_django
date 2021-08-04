from django.shortcuts import get_object_or_404, render
from .models import Practice, Session
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.list import ListView
from django.views.generic.dates import ArchiveIndexView
from .forms import PracticeDetailForm


class PracticeListView(ListView):
    model = Practice

# in progress
class PracticeHistoryListView(ArchiveIndexView):
    model = Practice
    queryset = Practice.session_set
    context_object_name = 'session_list'
    #ordering = ['-date_created']

"""
def practice_history(request, practice_id):
    practice = get_object_or_404(Practice, pk=practice_id)
    session_list = practice.session_set.all().order_by('-session_date')
    return render(request, 'nyndro/practice_history.html', {'session_list': session_list})
"""

def practice_detail(request, practice_id):
    practice = get_object_or_404(Practice, pk=practice_id)
    if request.method == "POST":
        form = PracticeDetailForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.practice = practice
            instance.save()
            session = Session.objects.latest('id')
            practice.current_value += session.session_value
            practice.save()
            return HttpResponseRedirect(reverse('nyndro:practice_detail', args=[practice.id]))
    else:
        form = PracticeDetailForm()
    context = {'practice': practice, 'form': form, }
    return render(request, 'nyndro/practice_detail.html', context)

