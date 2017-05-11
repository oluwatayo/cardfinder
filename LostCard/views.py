from django.views import generic
from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from .models import Card, CardFound
from django.core.mail import send_mass_mail, BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from . import messages
##################
def home(request):
    return render(request, 'LostCard/index1.html')

def lost_form(request):
    return render(request, 'LostCard/lost_form.html')

def found_form(request):
    return render(request, 'LostCard/found_form.html')

def about(request):
    return render(request, 'LostCard/about.html')

class LostIndexView(generic.ListView):
    template_name = 'LostCard/lost_cards.html'
    context_object_name = 'all_cards'

    def get_queryset(self):
        return Card.objects.all()


class LostDetailView(generic.DetailView):
    model = Card
    template_name = 'LostCard/details.html'

class FoundIndexView(generic.ListView):
    template_name = 'LostCard/found_cards.html'
    context_object_name = 'all_cards_found'

    def get_queryset(self):
        return CardFound.objects.all()

class FoundDetailView(generic.DetailView):
    model = CardFound
    template_name = 'LostCard/found_details.html'


def mail(request):
    if request.method == 'POST' :
        name = request.POST['user_name']
        subject = request.POST['subject']
        email_address = request.POST['user_mail']
        message = request.POST['message']
        admin_message = "We Got Your Message. We Promise to Get back to you as soon as possible. Thanks"
        context = {
            'mail_sent':admin_message,
        }
        try:
            datatuple = (
                ("Message From "+name+" || Subject: "+subject, message, 'cardfinder01@gmail.com', ['cardfinder01@gmail.com']),
                ('From Cardfinder', admin_message, 'cardfinder01@gmail.com', [email_address]),
            )
            send_mass_mail(datatuple)
        except BadHeaderError:
               return HttpResponse('Invalid header found OR Mail Server Down. Please try again')
        return render(request, 'LostCard/index1.html', context)

def found_form_submit(request):
    #submitting details for a found card by a finder
    if (request.method == 'POST') or (request.method == 'FILES'):
        card_sta = request.POST['cardtype']
        all_cards_found = CardFound.objects.all()
        all_cards = Card.objects.all()
        for card in all_cards_found:
            if card_sta is card.value:
                card_spec1 = card.specsfound_set.create()
                card_spec1.Org_Name = request.POST['organisation']
                card_spec1.holder_name = request.POST['holdername']
                card_spec1.id_card = request.POST['id']

                card_spec1.email_add_founder = request.POST['email']
                card_spec1.phone_no = request.POST['phone_number']
                card_spec1.save()

                for ccc in all_cards:
                    if ccc.value is card.value:
                       for cd in ccc.specs_set.all():
                           if cd.holder_name.lower() == card_spec1.holder_name.lower() and cd.Org_Name.lower() == card_spec1.Org_Name.lower() \
                                   and cd.id_card.lower() == card_spec1.id_card.lower():
                               try:
                                   message = messages.message_perfect_owner()
                                   message += "\n" + card_spec1.email_add_founder + "\n" + card_spec1.phone_no
                                   message1 = messages.message_perfect_finder()
                                   message1 += "\n" + cd.email_add + "\n" + cd.phone_no
                                   datatuple = (
                                       ("About your Missing Card", message ,
                                        'cardfinder01@gmail.com', [cd.email_add]),
                                       ('About the card you found', message1, 'cardfinder01@gmail.com',
                                        [card_spec1.email_add_founder]),
                                   )
                                   send_mass_mail(datatuple)
                               except BadHeaderError:
                                   return HttpResponse('Invalid header found OR Mail Server Down. Please try again')
                               return render(request, 'LostCard/index1.html',{'info':message1})
                           elif cd.holder_name.lower() == card_spec1.holder_name.lower() \
                                   and cd.Org_Name.lower() == card_spec1.Org_Name.lower():
                               try:
                                   message = messages.message_not_perfect_owner()
                                   message += "\n" + card_spec1.email_add_founder + "\n" + card_spec1.phone_no
                                   message1 = messages.message_not_perfect_finder()
                                   message1 += "\n" + cd.email_add + "\n" + cd.phone_no
                                   datatuple = (
                                       ("About your Missing Card", message ,
                                        'cardfinder01@gmail.com', [cd.email_add]),
                                       ('About the card you found', message1, 'cardfinder01@gmail.com',
                                        [card_spec1.email_add_founder]),
                                   )
                                   send_mass_mail(datatuple)
                               except BadHeaderError:
                                   return HttpResponse('Invalid header found OR Mail Server Down. Please try again')
                               return render(request, 'LostCard/index1.html',{'info':message1})
                           elif cd.holder_name.lower() == card_spec1.holder_name.lower() and cd.id_card.lower() == card_spec1.id_card.lower():
                               try:
                                   message = messages.message_not_perfect_owner()
                                   message += "\n" + card_spec1.email_add_founder + "\n" + card_spec1.phone_no
                                   message1 = messages.message_not_perfect_finder()
                                   message1 += "\n" + cd.email_add + "\n" + cd.phone_no
                                   datatuple = (
                                       ("About your Missing Card", message ,
                                        'cardfinder01@gmail.com', [cd.email_add]),
                                       ('About the card you found', message1, 'cardfinder01@gmail.com',
                                        [card_spec1.email_add_founder]),
                                   )
                                   send_mass_mail(datatuple)
                               except BadHeaderError:
                                   return HttpResponse('Invalid header found OR Mail Server Down. Please try again')
                               return render(request, 'LostCard/index1.html',{'info': message1})
                           else:
                               try:
                                   message = messages.no_match_found()
                                   send_mail(
                                       'CardFinder',
                                        message,
                                       'cardfinder01@gmail.com',
                                       [card_spec1.email_add_founder],
                                   )

                               except BadHeaderError:
                                   return HttpResponse('Invalid header found OR Mail Server Down. Please try again')
                               return render(request, 'LostCard/index1.html',{'info':message})
                    else:
                        try:
                            message_out = messages.no_match_found()
                            send_mail(
                                'CardFinder',
                                message_out,
                                'cardfinder01@gmail.com',
                                [card_spec1.email_add_founder],
                            )

                        except BadHeaderError:
                            return HttpResponse('Invalid header found OR Mail Server Down. Please try again')
                        return render(request, 'LostCard/index1.html', {'info': message_out})


def lost_form_submit(request):
    #submitting detatils for a missing card
    if request.method == 'POST':
        card_value = request.POST['cardtype']
        all_cards = Card.objects.all()
        all_cards_found = CardFound.objects.all()
        for card in all_cards:
            if card_value is card.value:
                card_spec1 = card.specs_set.create()
                card_spec1.Org_Name = request.POST['organisation']
                card_spec1.holder_name = request.POST['holdername']
                card_spec1.id_card = request.POST['id']
                card_spec1.email_add = request.POST['email']
                card_spec1.phone_no = request.POST['phone_number']
                card_spec1.save()

                for found in all_cards_found:
                    if found.value is card_value:
                        for i in found.specsfound_set.all():
                            if i.holder_name.lower() == card_spec1.holder_name.lower() and i.Org_Name.lower() == card_spec1.Org_Name.lower() \
                                    and i.id_card.lower() == card_spec1.id_card.lower():
                                try:
                                    message = messages.message_perfect_lost_finder()
                                    message += "\n" + card_spec1.email_add + "\n" + card_spec1.phone_no
                                    message1 = messages.message_perfect_lost_owner()
                                    message1 += "\n" + i.email_add_founder + "\n" + i.phone_no
                                    datatuple = (
                                        ("About your Missing Card", message1,
                                         'cardfinder01@gmail.com', [card_spec1.email_add]),
                                        ('About the card you found', message, 'cardfinder01@gmail.com',
                                         [i.email_add_founder]),
                                    )
                                    send_mass_mail(datatuple)
                                except BadHeaderError:
                                    return HttpResponse('Invalid header found OR Mail Server Down. Please try again')
                                return render(request, 'LostCard/index1.html', {'info': message1})
                            elif (i.holder_name.lower() == card_spec1.holder_name.lower() \
                                    and i.Org_Name.lower() == card_spec1.Org_Name.lower()) or \
                                 (i.holder_name.lower() == card_spec1.holder_name.lower() and i.id_card.lower() == card_spec1.id_card.lower()) :
                                try:
                                    message = messages.message_not_perfect_lost_finder()
                                    message += "\n" + card_spec1.email_add + "\n" + card_spec1.phone_no
                                    message1 = messages.message_not_perfect_lost_owner()
                                    message1 += "\n" + i.email_add_founder + "\n" + i.phone_no
                                    datatuple = (
                                        ("About your Missing Card", message1,
                                         'cardfinder01@gmail.com', [card_spec1.email_add]),
                                        ('About the card you found', message, 'cardfinder01@gmail.com',
                                         [i.email_add_founder]),
                                    )
                                    send_mass_mail(datatuple)
                                except BadHeaderError:
                                    return HttpResponse('Invalid header found OR Mail Server Down. Please try again')
                                return render(request, 'LostCard/index1.html', {'info': message1})
                            else:
                                try:
                                    message = messages.no_match_lost()
                                    send_mail(
                                        'CardFinder',
                                        message,
                                        'cardfinder01@gmail.com',
                                        [card_spec1.email_add],
                                    )

                                except BadHeaderError:
                                    return HttpResponse('Invalid header found OR Mail Server Down. Please try again')
                                return render(request, 'LostCard/index1.html', {'info': message})
                    else:
                        try:
                            message_out = messages.no_match_lost()
                            send_mail(
                                'CardFinder',
                                message_out,
                                'cardfinder01@gmail.com',
                                [card_spec1.email_add],
                            )

                        except BadHeaderError:
                            return HttpResponse('Invalid header found OR Mail Server Down. Please try again')
                        return render(request, 'LostCard/index1.html', {'info': message_out})

                return render(request, 'LostCard/index1.html')
       # return render(request, 'lostcard/index1.html', {'context':card_value})








