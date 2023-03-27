from django.shortcuts import render, redirect,get_object_or_404
from .forms import SignUpForm, LoginForm,InstructionForm
from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Instruction



def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_admin:
                login(request, user)
                return redirect('adminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('user')
            
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})


def admin(request):
    #return render(request,'admin.html')
    allInstruction=Instruction.objects.all()
    template = loader.get_template('admin.html')
    context = {
    'allInstruction': allInstruction,
      }
    return HttpResponse(template.render(context,request))


def customer(request):
    #return render(request,'user.html')
    allInstruction=Instruction.objects.all()
    template = loader.get_template('user.html')
    context = {
    'allInstruction': allInstruction,
      }
    return HttpResponse(template.render(context,request))

def delete(request,id):
    deleteInstruction=Instruction.objects.get(id=id)
    deleteInstruction.delete()
    allInstruction=Instruction.objects.all()
    template = loader.get_template('admin.html')
    context = {
    'allInstruction': allInstruction,
      }
    return HttpResponse(template.render(context,request))

def admin_edit(request,id):
    editinstruction=Instruction.objects.get(id=id)
    template = loader.get_template('edit.html')
    context = {
    'editinstruction': editinstruction,
      }
    return HttpResponse(template.render(context,request))

def update(request, id):
    edit_instruction = get_object_or_404(Instruction, id=id)
    if request.method == 'POST':
        form = InstructionForm(request.POST, instance=edit_instruction)
        if form.is_valid():
            form.save()
            allInstruction=Instruction.objects.all()
            template = loader.get_template('admin.html')
            context = {
            'allInstruction': allInstruction,
            }
            return HttpResponse(template.render(context,request))
    else:
        form = InstructionForm(instance=edit_instruction)
        context = {'edit_instruction': edit_instruction, 'form': form}
        return render(request, 'edit.html', context)



def employee(request):
    return render(request,'employee.html')


 
def add(request):  
    if request.method == "POST":  
        form = InstructionForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                allInstruction=Instruction.objects.all()
                template = loader.get_template('admin.html')
                context = {
                'allInstruction': allInstruction,
                }
                return HttpResponse(template.render(context,request))  
            except:  
                pass  
    else:  
        form = InstructionForm()  
    return render(request,'add.html',{'form':form})  


