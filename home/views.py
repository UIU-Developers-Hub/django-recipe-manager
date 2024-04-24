from django.shortcuts import render, redirect
from .models import Rm

def receipes(request): #function name receipes#
    if request.method == 'POST':
        data = request.POST
        name = data.get('Receipe__name')
        des = data.get('Receipe_description')
        img = request.FILES.get('Receipe_img')
        
        #saving data in model
        Rm.objects.create (
            r_name = name,
            r_des = des,
            r_img = img
        )
     
        # Redirect to a success page or another appropriate page
        return redirect('get_post_res')   
    Z = Rm.objects.all()

    if request.GET.get('Search'):
        Z = Z.filter(r_name__icontains = request.GET.get('Search')) 
         
    context = {'X' : Z}
        
    
    return render(request, "r.html" , context)


def update_res(request,id):
    Z = Rm.objects.get(id = id)
    if request.method == 'POST':
        data = request.POST
        name = data.get('Receipe__name')
        des = data.get('Receipe_description')
        img = request.FILES.get('Receipe_img')
        Z.r_name = name
        Z.r_des = des
        if img:
         Z.r_img = img
        Z.save()
        return redirect('get_post_res')
    context = {'X1' : Z}
    return render(request, "update_r.html" , context)
def delete_res(request, id):
     Z = Rm.objects.get(id = id)
     Z.delete()
     return redirect('get_post_res')