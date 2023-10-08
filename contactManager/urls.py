from django.urls import path
from .views import *

urlpatterns = [
    path('', contactList),
    # path('base/', base),
    path('contactList/', contactList, name='contactList'),
    # path('test/', test, name='test'),

    path('addContact', addContact, name='addContact'),
    path('addContactPost/', addContactPost, name='addContactPost'),

    path('selectContact/<int:contact_id>', selectContact, name='selectContact'),

    path('editContact/<int:contact_id>', editContact, name='editContact'),
    path('editContactPost/<int:contact_id>', editContactPost, name='editContactPost'),

    path('favoriteList/', favoriteList, name='favoriteList'),
    path('delContact/<int:contact_id>', delContact, name='delContact'),

    path('createGroup/', createGroup, name='createGroup'),
    path('createGroupPost/', createGroupPost, name='createGroupPost'),
    path('selectGroup/<int:group_id>', selectGroup, name='selectGroup'),
    path('listGroup/', listGroup, name='listGroup'),
    path('editGroup/<int:group_id>', editGroup, name='editGroup'),
    path('addContactInGroup/<int:group_id>', addContactInGroup, name='addContactInGroup'),
     path('addContactInGroupPost/<int:group_id>', addContactInGroupPost, name='addContactInGroupPost'),

    path('testListContact/', testListContact, name='testListContact'),
    path('testListContactPost/', testListContactPost, name='testListContactPost')
    # path('main', index, name='main')

]