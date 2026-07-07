from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import TransactionForm
from .models import Transaction


@login_required
def transaction_list_view(request):
    transactions = Transaction.objects.all().order_by('-issue_date')
    return render(request, 'transaction_list.html', {'transactions': transactions})


@login_required
def issue_book_view(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.status = 'Issued'
            transaction.save()
            messages.success(request, 'Book issued successfully.')
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'issue_book.html', {'form': form})


@login_required
def return_book_view(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.status = 'Returned'
        transaction.save()
        messages.success(request, 'Book returned successfully.')
        return redirect('transaction_list')
    return render(request, 'transaction_confirm_return.html', {'object': transaction})
