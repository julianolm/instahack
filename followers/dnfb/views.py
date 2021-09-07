from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import UserNameForm
from .auxiliar_scripts.dnfb import do_not_follow_user_back, DNFBError


def home(request):
    form = UserNameForm()
    context = {'form':form}
    return render(request, 'dnfb/index.html', context)

# def dnfb(request):
#     if request.method=='GET':
#         return render(request, 'dnfb/index.html')
#
#     elif request.method=='POST':
#         username = request.POST['username']
#         context = {'username':username}
#         return render(request, 'dnfb/index.html', context)

def dnfb(request):
    context = {}
    form = UserNameForm(request.GET) # received form containig data
    if form.is_valid():
        username = form.cleaned_data['username']
        try:
            dumbs_list = do_not_follow_user_back(username)
        except DNFBError as error:
            context['error'] = error.message
        else:
            context['username'] = username
            context['dumbs_list'] = dumbs_list

    context['form'] = UserNameForm() # new empty search form to be rendered in the page
    return render(request, 'dnfb/index.html', context)