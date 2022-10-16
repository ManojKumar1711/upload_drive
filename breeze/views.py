from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from .forms import FileForm
from .models import File
# Create your views here.


def home(request):
    return render(request,"breeze/base.html")

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name,uploaded_file)
        context['url'] = fs.url(name)
    return render(request,'breeze/upload.html',context)

def files(request):
    files = File.objects.all()
    return render(request,'breeze/file_list.html',{'files':files})

def upload_file(request):
    if request.method == 'POST':
        form = FileForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('files')
    else:
        form = FileForm()
    return render(request,'breeze/upload_file.html',{'form':form})
