from django.shortcuts import render, redirect  
from .forms import SampleNameForm  
from .models import SampleName  
# Create your views here.  
def emp(request):  
    if request.method == "POST":  
        form = SampleNameForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = SampleNameForm()  
    return render(request,'index.html',{'form':form})  
def show(request):  
    samplenames = SampleName.objects.all()  
    return render(request,"show.html",{'samplenames':samplenames})  
def edit(request, id):  
    samplename = SampleName.objects.get(id=id)  
    form = SampleNameForm(instance=samplename) 
    return render(request,'edit.html', {'samplename':samplename,'form':form})  
def update(request, id):  
    samplename = SampleName.objects.get(id=id)  
    form = SampleNameForm(request.POST, instance = samplename)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'edit.html', {'samplename': samplename})  
def destroy(request, id):  
    samplename = SampleName.objects.get(id=id)  
    samplename.delete()  
    return redirect("/show")  