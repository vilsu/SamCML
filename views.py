from django.template import Context, Template
from django.http import Http404, HttpResponse
from django.db import connection
import random   # to get random session-id
from types import *     # to get IntType for if-loops
from django.contrib.sessions.models import Session
from django.contrib import auth

import codes

# TODO session
# pk = random.getrandbits(100)
#s = Session.objects.get(pk)

# see when the session expires by s.expire_date
# to get session data by s.session_data
# to understand the data by s.get_decoded()


def getTitles():
    if GET.user:
        title = "Codes by ", {{ GET.user }}
    if GET.tag:
        title = "Codes by ", {{ GET.tag }}


def getVotes():
    votes = codes.upvote - codes.downvote


def getAnswers():


def getViewCounts():






# identify user by openID
def _get_username(request):
   username = Author.objects.where('openID') 
   return render_to_response('homepage.html',
                              request.session,
                              {'Author': username})

def my_homepage_view(request):
    user = request.user.username 
    t = Template(open('/home/noa/build/SamCML/templates/index.html','r').read())
    c = Context({"name": user})
    html = t.render(c) 
    return HttpResponse(html)

# identify user by email to get openID
cursor = connection.cursor()
def _get_openid(request):
    if request.user.is_authenticated():
        # Force Django to open the database:
        openID = Author.objects.where('email')
        # why rendering?
        # why not: return request.session(openID)
        return render_to_response('homepage.html', 
                                   request.session, 
                                   {'Author': openID})


















# perhaps unnecessarry because of Django's comments framework
def post_comment(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')

    if 'comment' not in request.POST:
        raise Http404('Comment not submitted')

    if request.session.get('has_commented_within_15_seconds', False):
        return HttpResponse("You've already commented in 15 seconds.")

    c = comments.Comment(comment=request.POST['comment'])
    c.save()
    request.session['has_commented'] = True
    return HttpResponse('Thanks for your comment!')



















def login(request):
    if request.method != 'POST':
        raise Http404('Only POSTs are allowed')
    try:
        m = Member.objects.get(username=request.POST['username'])
        if m.password == request.POST['password']:
            request.session['user_id'] = m.id
            return HttpResponseRedirect('/you-are-logged-in/')
    except Member.DoesNotExist:
        return HttpResponse("Your username and password didn't match.")

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        pass
    return HttpResponse("You're logged out.")

def login_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("/account/loggedin/")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")

