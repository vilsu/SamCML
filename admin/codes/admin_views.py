from mysite.codes.models import Code 

from django.template import RequestContext
from django.conf import settings
from django.shortcuts import render_to_response
from django.contrib.admin.views.decorators import staff_member_required


def index(request):
    #stuff = yourApp.objects.all().order_by('-pub_date')[:5]
    t = loader.get_template('SamCML/templates/index.html')
    c = Context({
        'MEDIA_URL': settings.MEDIA_URL,
        #'some_stuff': stuff
    })
    return render_to_response('base/default.html',
                            {
                            'MEDIA_URL': settings.MEDIA_URL,
                            },
                            RequestContext(request))


def report(request):
    return render_to_response(
        "admin/codes/report.html", # TODO
        {'book_list' : Book.objects.all()},
        RequestContext(request, {}),    # ensures that information about the current user is available to the template
    )
report = staff_member_required(report)

