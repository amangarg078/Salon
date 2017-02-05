from django.shortcuts import render,get_object_or_404
from .models import SalonStore,Photo
from salon.forms import QueryForm,UploadForm,UploadFileForm
from django.http import HttpResponseRedirect
import re
from datetime import datetime
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    form=QueryForm()
    count=-1
    stores=[]
    if request.GET.get('name') or request.GET.get('locality'):
        
        name = request.GET.get('name')
        #name=re.findall('\w+',name)
        locality = request.GET.get('locality')
        #locality=re.findall('\w+',locality)
        print name
        print locality
        if name and (not locality):
            result = SalonStore.objects.filter(name__icontains=name)
        if locality and (not name):
            result = SalonStore.objects.filter(address_3__icontains=locality)
        if name and locality:
            result = SalonStore.objects.filter(name__in=name,address_3__in=locality).order_by('-date_created')
        print "search",result

        
        count=len(result)
        
        return render(request,'salon/index.html',{'result':result,'count':count,'form':form})
    if request.GET.get('all'):
        result= SalonStore.objects.all().order_by('-date_created')
        count=len(result)
        
        return render(request,'salon/index.html',{'result':result,'count':count,'form':form})

    return render(request,'salon/index.html',{'form':form,'count':count})


def upload_form(request):
   
    if request.method == 'POST':
        form=UploadForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
    
            address_1 = form.cleaned_data['address_1']
            address_2 = form.cleaned_data['address_2']
            address_3 = form.cleaned_data['address_3']
            state = form.cleaned_data['state']
            country= form.cleaned_data['country']
            contact_number= form.cleaned_data['contact_number']
            email= form.cleaned_data['email']
            date_created=datetime.now()
            date_modified=datetime.now()
            #store=SalonStore(name=name,address_1=address_1,address_2=address_2,address_3=address_3,state=state,country=country,contact_number=contact_number,email=email,date_modified=date_modified,date_created=date_created)
            s=form.save()
            print "ssss",s
            return HttpResponseRedirect(reverse('details',args=(s.pk,)))
        else:
            print form.errors
    else:
        form=UploadForm()
    return render(request,'salon/upload.html',{'form':form})

def uploadImages(request,id):
    
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            photo=Photo()
            return redirect('gallery')
    else:
        form = UploadFileForm()
    return render(request, 'salon/upload_image.html', {'form': form})

def salonDetails(request,id):
    salon=get_object_or_404(SalonStore,pk=id)
    return render(request,'salon/details.html',{'salon':salon})

def gallery(request,id):
    var=0
    salon=get_object_or_404(SalonStore,pk=id)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES )
        if form.is_valid():
            f=form.save(commit=False)
            f.salon_id=salon
            f.save()
            form = UploadFileForm()
            photos=Photo.objects.filter(salon_id=id).order_by('-date_created')
            print photos

            return render(request,'salon/gallery.html',{'photos':photos,'form':form})
    else:
        form = UploadFileForm()
    photos=Photo.objects.filter(salon_id=id).order_by('-date_created')
    return render(request,'salon/gallery.html',{'photos':photos,'form':form,'var':var})
