from django.shortcuts import render,redirect
from .forms import EmployeeForm
from .models import Assets
# Create your views here.
def asset_list(request):
    context = {'asset_list': Assets.objects.all()}
    return render(request, 'asset_register/asset_list.html', context)

def asset_form(request,id=0):
    if request.method == 'GET':
        if id == 0:
            form = EmployeeForm()
        else:
            asset = Assets.objects.get(pk=id)
            form = EmployeeForm(instance=asset)
        return render(request, 'asset_register/asset_form.html', {'form':form})
    else:
        if id == 0:
            form = EmployeeForm(request.POST)
        else:
            asset = Assets.objects.get(pk=id)
            form = EmployeeForm(request.POST, instance = asset)
        
        if form.is_valid():
            form.save()
        return redirect('/asset/list')

def asset_delete(request,id):
    asset = Assets.objects.get(pk=id)
    asset.delete()
    return redirect('/asset/list')