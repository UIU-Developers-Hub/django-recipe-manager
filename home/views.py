from django.shortcuts import render, redirect
from .models import Rm

def receipes(request):
    if request.method == 'POST':
        data = request.POST
        r_name = data.get('r_name')
        r_des = data.get('r_des')
        r_img = request.FILES.get('r_img')

        # Validate form data
        if r_name and r_des and r_img:
            # Create a new Rm instance
            Rm.objects.create(
                r_name=r_name,
                r_des=r_des,
                r_img=r_img
            )
            # Redirect to a success page or another appropriate page

        return redirect('/')   

    return render(request, "r.html")
