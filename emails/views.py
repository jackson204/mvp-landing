from django.shortcuts import render
from django.http import HttpResponse, Http404, request
# Create your views here.
# Model -> View -> Template
# Model -> View -> React.js / Vue.js
from .forms import EmailEntryForm
from .models import EmailEntry


def email_entry_get_view(request, id=None, *args, **kwargs):
    # get a single item stored in the database
    # print(args, kwargs)
    try:
        obj = EmailEntry.objects.get(id=id)
    except EmailEntry.DoesNotExist:
        raise Http404
    # return HttpResponse(f"<h1>Hello {obj.email}</h1>")
    return render(request, "get.html", {"object": obj, "email": "aaa@gmailc.om"})


def email_entry_create_view(request, *args, **kwargs):
    # if request.method == "POST":
    #        DONT DO THIS!
    #     print(dict(request.POST))
    #     data = dict(request.POST)
    #     try:
    #         del data['csrfmiddlewaretoken']
    #     except:
    #         pass
    #     obj = EmailEntry(**data)
    #     obj.save()
    form = EmailEntryForm(request.POST or None)
    if form.is_valid():
        '''
        obj = form.save(commit=False) # Model Instance
        # obj.name = "Justin"
        obj.save()
        new_id = obj.id
        '''
        form.save()
        form = EmailEntryForm()
        # return HttpResponseRedirect(f"/email/{new_id}")
    return render(request, "form.html", {"form": form})


def email_entry_list_view():
    return


def email_entry_update_view():
    return


def email_entry_destroy_view():
    return
