# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


from .models import ContactCreate
from .forms import ContactForm

# Create your views here.


def index(request):
    """The home page for potfonebks"""
    return render(request, 'potfonebks/index.html')


@login_required
def contacts(request):
    """Show all contacts"""
    contacts = ContactCreate.objects.filter(
        owner=request.user).order_by('name')
    context = {'contacts': contacts}
    return render(request, 'potfonebks/contacts.html', context)


@login_required
def contact(request, contact_id):
    """ Show a single contact detail"""
    contact = ContactCreate.objects.get(id=contact_id)
    # contact must belong to current user
    if contact.owner != request.user:
        raise Http404

    details = (
        # contact.image,
        contact.mobile_phone,
        contact.phone,
        contact.email,
        contact.address
    )
    context = {'contact': contact, 'details': details}
    return render(request, 'potfonebks/detail.html', context)


@login_required
def new_contact(request):
    """ Add new contact."""
    if request.method != 'POST':
        # blank form. no data sumitted
        form = ContactForm()
    else:
        # post submitted data/processed data
        form = ContactForm(request.POST)
        if form.is_valid():
            new_contact = form.save(commit=False)
            new_contact.owner = request.user
            new_contact.save()
            return HttpResponseRedirect(reverse('potfonebks:contacts'))

    context = {'form': form}
    return render(request, 'potfonebks/new_contact.html', context)


@login_required
def edit_contact(request, contact_id):
        # Edit existing contact
    contact = ContactCreate.objects.get(id=contact_id)
    if contact.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # pre-fill form with the current contact.
        form = ContactForm(instance=contact)
    else:
        # Process data
        form = ContactForm(instance=contact, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(
                'potfonebks:contact',
                args=[contact.id])
            )
    context = {'contact': contact, 'form': form}
    return render(request, 'potfonebks/edit_contact.html', context)


@login_required
def delete_contact(request, cont_id):
    contact = ContactCreate.objects.get(id=cont_id)
    if contact.owner != request.user:
        raise Http404

    if contact:
        contact.delete()
        return HttpResponseRedirect(reverse('potfonebks:contacts'))
    return render(request, 'potfonebks/contacts.html')
    #     return HttpResponseRedirect(reverse(render(request,
    #                                                'potfonebks:contacts')))
    # else:
    #     return render(request, 'potfonebks/contacts.html')
