from django.shortcuts import render, reverse
from bugtracker_app.forms import AddTicketForm, LoginForm
from bugtracker_app.models import Ticket, CustomUser
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login , authenticate, logout


def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
        if user:
            auth_login(request, user)
            return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
    form = LoginForm()
    return render(request, "login.html", {"form": form})


@login_required
def index(request):
    new = Ticket.objects.filter(status='New')
    in_progress = Ticket.objects.filter(status='In Progress')
    done = Ticket.objects.filter(status='Done')
    invalid = Ticket.objects.filter(status='Invalid')
    return render(request, 'index.html',{
        'new': new,
        'inprogress': in_progress,
        'done': done,
        'invalid': invalid
        })

@login_required
def user_detail_view(request, user_id):
    #the current tickets assigned to a user
    #which tickets that user completed
    user_obj = CustomUser.objects.get(id=user_id)
    created_tickets = Ticket.objects.filter(created_by_id=user_obj)
    in_progress = Ticket.objects.filter(assigned_to_id=user_obj)
    completed_tickets = Ticket.objects.filter(completed_by_id=user_obj)
    
    return render(request, "user_detail.html", {
        "user": user_obj,
        "created_tickets": created_tickets,
        "in_progress": in_progress,
        "completed_tickets": completed_tickets
        })

@login_required
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
            return HttpResponseRedirect(reverse('homepage'))
    form = AddTicketForm()
    return render(request,'submit.html',{'form': form})

@login_required
def ticket_view(request,ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    return render(request, "ticket_detail.html",{"ticket": ticket})

@login_required  
def edit_ticket_view(request,ticket_id):
    context = {}
    edits = Ticket.objects.get(id=ticket_id)

    if request.method == "POST":
        form = AddTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            edits.title = data['title']
            edits.description = data['description']
            edits.save()
            return HttpResponseRedirect(reverse('ticket_view', args=[edits.id]))
    form = AddTicketForm(
        initial={'title': edits.title, 'description': edits.description}
    )
    context.update({'form':form})
    return render(request,'submit.html',context)


@login_required
def claim_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.assigned_to = request.user
    ticket.status = 'In Progress'
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_view', args=[ticket.id]))
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def complete_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.completed_by = request.user
    ticket.assigned_to = None
    ticket.status = 'Done'
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_view', args=[ticket.id]))
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def invalid_ticket(request, ticket_id):
    ticket = Ticket.objects.get(id=ticket_id)
    ticket.completed_by = None
    ticket.assigned_to = None
    ticket.status = 'Invalid'
    ticket.save()
    return HttpResponseRedirect(reverse('ticket_view', args=[ticket.id]))
    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
