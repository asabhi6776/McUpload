from django.shortcuts import render
from core.models import *
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django import forms
from django.conf import settings 


# Create your views here.
class StoreFileForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(StoreFileForm, self).__init__( *args, **kwargs)
        for name, field in self.fields.items():
            if 'class' in field.widget.attrs:
                field.widget.attrs['class'] += 'form-control form-control-lg form-control-solid'
            else:
                field.widget.attrs.update({'class': 'form-control form-control-lg form-control-solid'})
    
    class Meta:
        model  = StoreFile
        exclude =[]
        
    def clean_file(self):
        file = self.cleaned_data.get("file")
        ext = file.name.split('.')[-1]
        if file in (None, ''):
            raise forms.ValidationError("Please upload file")
        if ext.lower() not in settings.FILE_SUPPORTED_LIST:
            raise forms.ValidationError("file extension not supported")
        return self.cleaned_data.get("file")
 
@login_required       
def add_file(request):
    cid = request.GET.get("id", None)
    if cid != None:
        try:
            instance = StoreFile.objects.get(id=cid)
            title = "Edit StoreFile"
            title2 = "List of StoreFile"
        except:
            instance = None
            title = "Add StoreFile"
            title2 = "List of StoreFile"
    else:
        instance = None
        title = "Add StoreFile"
        title2 = "List of StoreFile"
    if request.method == "POST":
        form = StoreFileForm(request.POST,request.FILES, instance=instance)
        print(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    else:

        form = StoreFileForm(instance=instance)
    return render(request, "add_form_new.html",
                  {"form": form, "title": title, "title2": title2, "side_url": "/"})


@login_required 
def file_list(request):
    objects = StoreFile.objects.all()
    return render(request, "list.html", {"object_list": objects})
    


