from django.shortcuts import render

# Create your views here.

def index(request):
    #all tickets, arranged in separate sections 
    #according to current ticket status
    return render(request, 'index.html')

def user_detail_view(request):
    #the current tickets assigned to a user
    #which tickets that user has filed
    #which tickets that user completed
    return render(request, 'index.html')

def submit_ticket_view(request):
    #When a ticket is filed/created, it should have the following settings:
    #Status: New
    #User Assigned: None
    #User who Completed: None
    #User who filed: Person who's logged in
    return render(request, 'index.html')

def ticket_view(request):
    #allows assigning a ticket to the currently logged in user
    #allows marking a ticket as invalid
    #allows marking a ticket as complete 
    return render(request, 'index.html')

def edit_ticket_view(request):
    #Title And Description ONLY
    return render(request, 'index.html')

'''
When a ticket is Done, these change as follows:

Status: Done
User Assigned: None
User who Completed: person who the ticket used to belong to
When a ticket is marked as Invalid, these change as follows:

Status: Invalid
User Assigned: None
User who Completed: None
...
