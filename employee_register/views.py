from django.shortcuts import render,redirect
from .forms import AssetForm
from .models import Assets
# Create your views here.
def asset_list(request):
    context = {'asset_list': Assets.objects.all()}
    return render(request, 'asset_register/asset_list.html', context)

def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                post.title= request.POST.get('title')
                post.content= request.POST.get('content')
                post.save()
                
                return render(request, 'asset_register/asset_form.html')  

        else:
                return render(request,'asset_register/asset_form.html')

def asset_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = AssetForm()
        else:
            asset = Assets.objects.get(pk=id)
            form = AssetForm(instance=asset)
        return render(request, 'asset_register/asset_form.html', {'form':form})
    else:
        if id == 0:
            form = AssetForm(request.POST)
        else:
            asset = Assets.objects.get(pk=id)
            form = AssetForm(request.POST, instance = asset)
        
        if form.is_valid():
            form.save()
        return redirect('/asset/list')

def asset_delete(request,id):
    asset = Assets.objects.get(pk=id)
    asset.delete()
    return redirect('/asset/list')