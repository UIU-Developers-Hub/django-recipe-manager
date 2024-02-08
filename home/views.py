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
        return redirect('/h')   
    Z = Rm.objects.all()
    context = {'X' : Z}
        
    
    return render(request, "r.html" , context)
