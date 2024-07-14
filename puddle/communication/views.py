from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms import MessageForm
from .models import Message

@login_required
def send(request, to=None):
    if request.method == "POST":
        form = MessageForm(request.POST)
        to_user = User.objects.filter(username=form.data.get("reciever")).first()
        if not to_user:
            form.add_error("reciever", "Recipient does not exist!")
        if request.user == to_user:
            form.add_error("reciever", "You cannot send a message to yourself")
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.recipient = to_user
            message.save()
            return redirect("/inbox")
        elif not to_user:
            form.add_error("reciever", "Recipient does not exist")
    else:
        form = MessageForm()
        if to:
            form.fields["reciever"].initial = to
    return render(request, "communication/send.html", {"form": form})

@login_required
def inbox(request):
    messages = Message.objects.filter(recipient=request.user)
    return render(request, "communication/inbox.html", {"messages": messages})

    

@login_required
def message_detail(request, message_id):
    message = Message.objects.get(pk=message_id)

    if message.sender != request.user and message.recipient != request.user:
        return redirect("/inbox")

    if message.recipient == request.user:
        message.read = True
        message.save()

    return render(request, "communication/message_detail.html", {"message": message})

@login_required
def delete_message(request, message_id):
    message = get_object_or_404(Message, pk=message_id)
    if request.user != message.sender and request.user != message.recipient:
        return redirect("/inbox")
    message.delete()    
    return redirect("/inbox")