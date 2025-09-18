from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

def listar_pessoa(request):
    pessoas = Pessoa.objects.all()
    return render(request,'list.html',{'pessoas':pessoas})

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar')
        return render(request,'criar.html',{'form':form})
    else:
        form = PessoaForm()
        return render(request,'criar.html',{'form':form})

def deletar_pessoa(request,pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        pessoa.delete()
        return redirect('listar')
    return render(request,'confirmar_delete.html',{'pessoa':pessoa})

def atualizar_pessoa(request,pk):
    pessoa = Pessoa.objects.get(pk=pk)
    if request.method == 'POST':
        form = PessoaForm(request.POST,instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('listar')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request,'criar.html',{'form':form})