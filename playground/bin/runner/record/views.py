#django libs
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.core.context_processors import csrf
from django.shortcuts import render, render_to_response, RequestContext,HttpResponseRedirect


#from django.forms.models import modelformset_factory
from django.utils.datastructures import SortedDict
from django.core import serializers


# Create your views here.
from .forms import RecordForm
from .models import Record

#from django.utils import simplejson as json
import json

def record(request):
    form=RecordForm(request.POST or None)
    if request.user.is_authenticated():
        user = request.user
        if form.is_valid():
            record=form.save(commit=False)
            record.user=user
            record.save()
            messages.success(request, 'Your record has been saved succesfully!')
            return HttpResponseRedirect('/records/')
        else:
            messages.error(request, 'Please enter all the fields below!')
    else:
        messages.error(request, 'Please sign in!')
    return render_to_response("record.html",
        locals(),
        context_instance=RequestContext(request))


def records(request):
    data=list()
    des_temp=list()# asigning list of descriptions to javascript function
    dis_temp=list()# asigning list of distances to javascript function
    if request.user.is_authenticated():
        user = request.user.id
        records = Record.objects.filter(user=user)
        for i in range(records.count()):
            r=Record.objects.get(pk=records[i].id)
            rf=RecordForm(instance=r)
            x=build_pretty_data_view(form_instance=rf, model_object=r,
                                exclude=('reg_date',),
                                append=('user',))
            data.append(x)
            des_temp.append(r.description)
            dis_temp.append(r.distance)
    else:
        messages.error(request, 'Please sign in!')
    des = json.dumps(des_temp)
    dis = json.dumps(dis_temp)
    return render_to_response('records.html',
                          RequestContext(request,
                                         {'data':data,'des':des, 'dis':dis, }))


'''some utils'''

def build_pretty_data_view(form_instance, model_object, exclude=(), append=()):
    '''
    function for displaying beautifully data from the database
    '''
    i=0
    sd=SortedDict()

    for j in append:
        try:
            sdvalue={'label':j.capitalize(),
                     'fieldvalue':model_object.__getattribute__(j)}
            sd.insert(i, j, sdvalue)
            i+=1
        except(AttributeError):
            pass

    for k,v in form_instance.fields.items():
        sdvalue={'label':"", 'fieldvalue':""}
        if not exclude.__contains__(k):
            if v.label is not None:
                sdvalue = {'label':v.label,
                           'fieldvalue': model_object.__getattribute__(k)}
            else:
                sdvalue = {'label':k,
                           'fieldvalue': model_object.__getattribute__(k)}
            sd.insert(i, k, sdvalue)
            i+=1
    return sd
