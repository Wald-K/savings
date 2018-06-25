# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Client, Bank, Deposit

from .forms import ClientForm, DepositForm

def test(request):
	return render(request, 'savings/test.html', {'test':'Testy'})


# Create your views here.

# Bank Views - class views

class BankList(ListView):
	model = Bank
	template_name = "savings/bank_list.html"

class BankCreate(CreateView):
	model = Bank
	fields = ['name', 'abbreviation',]
	success_url = reverse_lazy('savings:bank_list')

class BankUpdate(UpdateView):
	model = Bank
	fields = ['name', 'abbreviation',]
	success_url = reverse_lazy('savings:bank_list')



class BankDelete(DeleteView):
	model = Bank
	success_url = reverse_lazy('savings:bank_list')



# Client Views - method views

def client_list(request):
	clients = Client.objects.all()


	data = {}
	data['client_list'] = clients
	return render(request, 'savings/client_list.html', data)


def client_create(request):
	form = ClientForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('savings:client_list')
	else:
		return render(request, 'savings/client_form.html', {'form': form})

def client_update(request, pk):
	client = get_object_or_404(Client, pk=pk)
	form = ClientForm(request.POST or None, instance = client)

	if form.is_valid():
		form.save()
		return redirect('savings:client_list')

	else:
		return render(request, 'savings/client_form.html', {'form':form})

def client_detail(request, pk):
	client = get_object_or_404(Client, pk=pk)
	deposits_list = client.deposit_set.all()


	return render(request, 'savings/client_detail.html', {'object':client, 'deposits_list': deposits_list})

def client_delete(request, pk):
	client = get_object_or_404(Client, pk=pk)

	if request.method=='POST':
		client.delete()
		return redirect('savings:client_list')

	return render(request, 'savings/client_confirm_delete.html', {'object':client})


def deposit_list(request, deposit_status):
	if deposit_status == 'hold':
		deposits = Deposit.objects.filter(closed = False)
	elif deposit_status == 'history':
		deposits = Deposit.objects.filter(closed = True)
	elif deposit_status == 'all':
		deposits = Deposit.objects.all()

	# deposits = Deposit.objects.filter(isactive=True)
	return render(request, 'savings/deposit_list.html', {'deposits_list': deposits, 'deposit_status':deposit_status})


def deposit_create(request):
	form = DepositForm(request.POST or None)

	if form.is_valid():
		form.save()
		return redirect('savings:deposit_list', deposit_status = 'hold')
	else:
		return render(request, 'savings/deposit_form.html',{'form': form} )




	# form = ClientForm(request.POST or None)

	# if form.is_valid():
	# 	form.save()
	# 	return redirect('savings:client_list')
	# else:
	# 	return render(request, 'savings/client_form.html', {'form': form})


class DepositCreate(CreateView):
	model = Deposit
	fields = '__all__'
	success_url = reverse_lazy('savings:deposit_list', kwargs={'deposit_status': 'hold'})