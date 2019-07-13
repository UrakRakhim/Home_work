from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import UserRegister,UserUpdateForm,ProfileUpdateForm




def register(request):
    if request.method=='POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created  for {username}!. You able to Login')
            # username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form=UserRegister()
        # messages.INFO(request,f'NOT  Supported for !')
    return render(request,'users/register.html',{'form':form})


@login_required
def Profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance='request.user')
        p_form=ProfileUpdateForm(request.POST,
                                 request.FILES,
                                 instance='request.user.profile')
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has updated')
            return redirect('profile')
    else:
        u_form = UserUpdateForm( instance='request.user')
        p_form = ProfileUpdateForm( instance='request.user.profile')
    context={
        'u_form':u_form,
        'p_form':p_form
        }
    return  render(request,'users/profile.html',context)
# messages.DEBUG
# messages.ERROR
# messages.SUCCESS
# messages.WARNING
# messages.INFO