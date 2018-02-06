""" Define URL patterns for potfonebks"""

from django.conf.urls import url

from . import views
from django.contrib.auth import views as auth_views

from potfonebks import views as core_views


urlpatterns = [
    # Home page
    url(r'^$', views.index, name='index'),
    # Show all contacts
    url(r'^contacts/$', views.contacts, name='contacts'),
    # Detail page for contact
    url(r'^contacts/(?P<contact_id>\d+)/$', views.contact, name='contact'),
    # Page for adding a new contact
    url(r'^new_contact/$', views.new_contact, name='new_contact'),
    # Page for editing contact
    url(r'^edit_contact/(?P<contact_id>\d+)/$',
        views.edit_contact, name='edit_contact'),
    url(r'^delete/(?P<cont_id>\d+)/$',
        views.delete_contact, name='delete_contact'),
]
