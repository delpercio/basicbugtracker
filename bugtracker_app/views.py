from django.shortcuts import render
from bugtracker_app.forms import AddTicketForm
from bugtracker_app.models import Ticket

# Create your views here.
def login(request):
    #login view required 
    return render(request,'login.html')

def index(request):
    new = Ticket.objects.filter(status='New')
    in_progress = Ticket.objects.filter(status='In Progress')
    done = Ticket.objects.filter(status='Done')
    return render(request, 'index.html',{
        'new': new,
        'inprogress': in_progress,
        'done': done
        })

def user_detail_view(request):
    #the current tickets assigned to a user
    #which tickets that user has filed
    #which tickets that user completed
    return render(request, 'user_detail.html')

def submit_ticket_view(request):
    #When a ticket is filed/created, it should have the following settings:
    #Status: New
    #User Assigned: None
    #User who Completed: None
    #User who filed: Person who's logged in
    if request.method == 'POST':
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            Ticket.objects.create(
            title = data['title'],
            description = data['description'],
            )
    form = AddTicketForm()
    return render(request,'submit.html',{'form': form})

def ticket_view(request):
    #allows assigning a ticket to the currently logged in user
    #allows marking a ticket as invalid
    #allows marking a ticket as complete 
    return render(request, 'ticket_detail.html')

def edit_ticket_view(request):
    #Title And Description ONLY
    return render(request, 'edit_ticket.html')

'''
When a ticket is Done, these change as follows:

Status: Done
User Assigned: None
User who Completed: person who the ticket used to belong to
When a ticket is marked as Invalid, these change as follows:

Status: Invalid
User Assigned: None
User who Completed: None
'''
