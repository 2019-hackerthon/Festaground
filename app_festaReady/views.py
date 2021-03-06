from django.shortcuts import render, get_object_or_404, redirect
from app_festa.models import Festa, RegisterNum
from app_festaReady.models import Accompany, Ticket, Commenta, Commenttic
from app_festaNow.models import Now, Team, Commentn, Commentt, Home, Commenth
import datetime
from django.utils import timezone
from django.core.paginator import Paginator

# Create your views here.
def ready_main(request, festa_id) :
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_ready/ready_main.html', {'festa': festa})


#동행구하기 게시판    
def list_accompany(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    accompanies = Accompany.objects.filter(festa = festa.id)
    accompany_list = Accompany.objects.all()
    search = request.GET.get('search', '')
    if search:
        accompany_list = accompany_list.filter(title__icontains=search)
    paginator = Paginator(accompany_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'festa_ready/list_accompany.html', {'accompanies':accompanies, 'posts':posts, 'search':search, 'festa':festa})


def create_accompany(request, festa_id) :
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method == "POST":
        festa = get_object_or_404(Festa, pk = festa_id)
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        area = request.POST.get('area')
        description = request.POST.get('description')
        password = request.POST.get('password')
        image = request.FILES.get('image')
        accompany = Accompany(festa=festa, title=title, writer=writer, area=area, description=description, image=image, password=password)
        accompany.save()
        return redirect('list_accompany', festa.id)        
    return render(request, 'festa_ready/create_accompany.html', {'festa':festa})


def detail_accompany(request, festa_id, accompany_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    accompany = Accompany.objects.get(pk=accompany_id)
    commentas_list = Commenta.objects.filter(accompany = accompany_id)
    return render(request, 'festa_ready/detail_accompany.html', {'accompany':accompany, 'commentas': commentas_list, 'festa':festa})


def edit_accompany(request, festa_id, accompany_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    accompany = Accompany.objects.get(pk=accompany_id)
    return render(request, 'festa_ready/edit_accompany.html', {'accompany': accompany, 'festa':festa})


def update_accompany(request, festa_id, accompany_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method == "POST":
            false = 0 
            accompany = Accompany.objects.get(id = accompany_id)
            if request.POST.get('password') == accompany.password:
                title = request.POST.get('title')
                writer = request.POST.get('writer')
                area = request.POST.get('area')
                description = request.POST.get('description')
                accompany.title = title
                accompany.writer = writer
                accompany.area = area
                accompany.description = description
                accompany.save()
                return redirect('detail_accompany', festa.id, accompany.pk)
            return render(request, 'festa_ready/edit_accompany.html', {'accompany': accompany, 'festa':festa, 'fail':false})


def delete_accompany(request, festa_id, accompany_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    accompany = Accompany.objects.get(pk = accompany_id)

    if request.method == "POST":
        if request.POST.get('password') == accompany.password:
            accompany.delete()
            return redirect('list_accompany', festa_id)
        else:
            return redirect('incorrect_accompany', festa_id)
    return render(request, 'festa_ready/delete_accompany.html', {'festa':festa}) 


#티켓게시판
def ticket(request, festa_id) :
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_ready/ticket.html', {'festa':festa})


def list_ticket(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    tickets = Ticket.objects.filter(festa = festa.id)
    ticket_list = Ticket.objects.all()
    search = request.GET.get('search', '')
    if search:
        ticket_list = ticket_list.filter(title__icontains=search)
    paginator = Paginator(ticket_list, 5)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'festa_ready/list_ticket.html', {'tickets':tickets, 'posts':posts, 'search':search, 'festa':festa})


def create_ticket(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        festa = get_object_or_404(Festa, pk = festa_id)
        title = request.POST.get('title')
        writer = request.POST.get('writer')
        password = request.POST.get('password')
        deal_type = request.POST.get('deal_type')
        description = request.POST.get('description')
        image = request.FILES.get('image')
        ticket = Ticket(festa=festa, title=title, writer=writer, deal_type=deal_type, description=description, image = image, password=password)
        ticket.save()
        return redirect('detail_ticket', festa.id, ticket.pk)        
    return render(request, 'festa_ready/create_ticket.html', {'festa':festa})


def detail_ticket(request, festa_id, ticket_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    ticket = Ticket.objects.get(pk=ticket_id)
    commenttics_list = Commenttic.objects.filter(ticket = ticket_id)
    return render(request, 'festa_ready/detail_ticket.html', {'ticket':ticket, 'commenttics': commenttics_list, 'festa':festa})


def edit_ticket(request, festa_id, ticket_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    ticket = Ticket.objects.get(pk=ticket_id)
    return render(request, 'festa_ready/edit_ticket.html', {'ticket': ticket, 'festa':festa})


def update_ticket(request, festa_id, ticket_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method == "POST":
            ticket = Ticket.objects.get(id = ticket_id)
            false = 0
            if request.POST.get('password') == ticket.password:
                title = request.POST.get('title')
                writer = request.POST.get('writer')
                deal_type = request.POST.get('deal_type')
                description = request.POST.get('description')
                ticket.title = title
                ticket.writer = writer
                ticket.deal_type = deal_type
                ticket.description = description
                ticket.save()
                return redirect('detail_ticket', festa.id, ticket.pk)
            return render(request, 'festa_ready/edit_ticket.html', {'ticket': ticket, 'festa':festa, 'fail':false})


def delete_ticket(request, festa_id, ticket_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method == "POST":
        ticket = Ticket.objects.get(pk = ticket_id)
        ticket.delete()
        return redirect('list_ticket', festa.id)


#댓글
def create_commenta(request, festa_id, accompany_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        festa = get_object_or_404(Festa, pk = festa_id)
        writer = request.POST.get('writer')
        content = request.POST.get('content')
        password = request.POST.get('password')
        accompany = get_object_or_404(Accompany, pk=accompany_id)
        commenta = Commenta(festa=festa, writer=writer, content=content, password=password, accompany=accompany)
        commenta.save()
        return redirect('detail_accompany', festa.id, accompany.id)   

        
def create_commenttic(request, festa_id, ticket_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    if request.method=="POST":
        festa = get_object_or_404(Festa, pk = festa_id)
        writer = request.POST.get('writer')
        content = request.POST.get('content')
        password = request.POST.get('password')
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        commenttic = Commenttic(festa=festa, writer=writer, content=content, password=password, ticket=ticket)
        commenttic.save()
        return redirect('detail_ticket', festa.id, ticket.id)   


def delete_commenta(request, festa_id, accompany_id, commenta_id):
    noConfirm="AS"
    festa = get_object_or_404(Festa, pk = festa_id)
    accompany = get_object_or_404(Accompany, pk=accompany_id)
    commenta = Commenta.objects.get(pk = commenta_id)

    if request.method == "POST":
        if request.POST.get('password') == commenta.password:
            commenta.delete()
            return redirect('detail_accompany', festa_id, accompany_id)
        else:
            false=0
            return render(request, 'festa_ready/delete_commenta.html', {'festa':festa,'accompany':accompany, 'fail':false})
    return render(request, 'festa_ready/delete_commenta.html', {'festa':festa, 'accompany':accompany})   


def delete_commenttic(request, festa_id, ticket_id, commenttic_id):
    noConfirm="AS"
    festa = get_object_or_404(Festa, pk = festa_id)
    ticket = get_object_or_404(Ticket, pk=ticket_id)
    commenttic = Commenttic.objects.get(pk = commenttic_id)

    if request.method == "POST":
        if request.POST.get('password') == commenttic.password:
            commenttic.delete()
            return redirect('detail_ticket', festa_id, ticket_id)
        else:
            false=0
            return render(request, 'festa_ready/delete_commenttic.html', {'festa':festa,'ticket':ticket, 'fail':false})
    return render(request, 'festa_ready/delete_commenttic.html', {'festa':festa, 'ticket':ticket})   
    

#비밀번호 오류 페이지
def incorrect_accompany(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_ready/incorrect_accompany.html', {'festa':festa})


def incorrect_ticket(request, festa_id):
    festa = get_object_or_404(Festa, pk = festa_id)
    return render(request, 'festa_ready/incorrect_ticket.html', {'festa':festa})



