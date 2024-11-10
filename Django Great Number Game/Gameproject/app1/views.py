from django.shortcuts import render ,redirect
import random


def index(request):
    
    if "rand_num" not in request.session:
        request.session['rand_num']=random.randint(1,100)
        request.session['msg']=''
        request.session['won']=False
        
        
    
    context={
        'msg':request.session['msg'],
        'color':request.session['color'],
        'won':request.session['won'],
        'rand':request.session['rand_num'],
        
        
    }

    return render(request,'index.html',context)


def process(request):
    request.session['won']= False
    request.session['color']=''
    ran_num=int(request.session['rand_num'])
    user_num=int(request.POST['guessed'])        
    if user_num > ran_num:
        request.session['msg']="too high"
        
        request.session['color']='red'
        
    elif user_num < ran_num :
        request.session['msg']="too low"
        request.session['color']='blue'
       
    else :
        request.session['msg']="correct"
        request.session['color']='green'
        request.session['won']=True
        
    print(request.session['color'])
    return redirect('/')


def reset(request):
    del request.session['rand_num']
    request.session['won']=False

    return redirect('/')