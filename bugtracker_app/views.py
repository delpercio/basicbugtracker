from django.shortcuts import render
from bugtracker_app.forms import AddTicketForm, LoginForm
from bugtracker_app.models import Ticket, CustomUser
from django.conf import settings


def login(request):
    form = LoginForm()
    return render(request,'login.html',{'form':form})

def index(request):
    new = Ticket.objects.filter(status='New')
    in_progress = Ticket.objects.filter(status='In Progress')
    done = Ticket.objects.filter(status='Done')
    return render(request, 'index.html',{
        'new': new,
        'inprogress': in_progress,
        'done': done
        })

def user_detail_view(request, user_id):
    #the current tickets assigned to a user
    #which tickets that user completed
    user_obj = CustomUser.objects.get(id=user_id)
    created_tickets = Ticket.objects.filter(created_by_id=user_obj)
    
    return render(request, "user_detail.html", {
        "user": user_obj,
        "created_tickets": created_tickets
        })

def submit_ticket_view(request):
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            Ticket.objects.create(
            title = data['title'],
            description = data['description'],
            created_by=request.user
            )
    form = AddTicketForm()
    return render(request,'submit.html',{'form': form})

def ticket_view(request,ticket_id):
    #allows assigning a ticket to the currently logged in user
    #allows marking a ticket as invalid
    #allows marking a ticket as complete post_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, "ticket_detail.html",{"ticket": ticket})
    
def edit_ticket_view(request):
    #Title And Description ONLY
    return render(request, 'edit_ticket.html')

def claim_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.assigned_to = request.user
    ticket.save()
    return render(request, 'index.html')

def complete_ticket(request, ticket_id):
    ...
