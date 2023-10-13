from django.shortcuts import render
from django.http import HttpResponse
from contactManager.models import *
from .forms import UserForm
from django.shortcuts import redirect
import requests
import json
import os

# Create your views here.



def index(request):
    menu = ["About site", "Add contact", "Feedback"]
    allContact = Contact.objects.all()
    data = {"listContact": allContact, "title":"Main page", "menu":menu}
    return render(request, 'contactManager/index.html', context=data)

# def about(request):
#     data = {'title':'About of site'}
#     return render(request, 'contactManager/about.html', context=data)

# def base(request):
#     return render(request, 'contactManager/base.html')

# def test(request):
#     return render(request, 'contactManager/test.html')

def contactList(request):
    allContact = Contact.objects.all()
    count = allContact.count()
    data = {"listContact": allContact, "count":count}
    return render(request, 'contactManager/contactList.html', context=data)

def addContact(request):
    return render(request, 'contactManager/addContact.html')

def addContactPost(request):
    name = request.POST.get("name")
    email = request.POST.get("email")
    phoneNumber = request.POST.get("phoneNumber")
    birthday = request.POST.get("birthday")
    position = request.POST.get("position")
    note = request.POST.get("note")
    is_favoriteOn = request.POST.get("is_favorite")
    if (is_favoriteOn == 'on'):
        is_favorite = True
    else:
        is_favorite = False

    contact = Contact(name=f'{name}', email=f'{email}',
                      birthday=f'{birthday}', position=f'{position}',
                      note=f'{note}', phoneNumber=f"{phoneNumber}",
                      is_favorite=f'{is_favorite}')
    contact.save()
    return redirect(contactList)

def selectContact(request,contact_id):
    contact = Contact.objects.get(id = contact_id)
    data = {'contact': contact}
    return render(request, 'contactManager/selectContact.html', context=data)

def editContact(request, contact_id):
    contact = Contact.objects.get(id = contact_id)
    data = {'contact': contact}
    return render(request, 'contactManager/editContact.html', context=data)

def editContactPost(request, contact_id):
    contact = Contact.objects.get(id = contact_id)
    contact.name = request.POST.get("name")
    contact.email = request.POST.get("email")
    contact.phoneNumber = request.POST.get("phoneNumber")
    contact.birthday = request.POST.get("birthday")
    contact.position = request.POST.get("position")
    contact.note = request.POST.get("note")
    is_favoriteOn = request.POST.get("is_favorite")
    if (is_favoriteOn == 'on'):
        contact.is_favorite = True
    else:
        contact.is_favorite = False 
    
    contact.save()
    # return HttpResponse("Hello mir")
    return redirect(contactList)

# def favoriteList(request):
#     favoriteContact = Contact.objects.filter(is_favorite = True)
#     responseApi = requests.get('https://randomuser.me/api/')
#     # statusCode = responseApi.status_code
#     statusCode = responseApi.text
#     data = {'listContact': favoriteContact, 'title':'Список избранных контактов','statusCode': statusCode}
#     return render(request, 'contactManager/favoriteList.html',context=data)


def favoriteList(request):
    weatherApi = open('weather.json', encoding='utf-8')
    jsonResult = json.loads(weatherApi.read()) 
    temp = (jsonResult['fact'])['temp']
    data = {'temp': temp}
    return render(request, 'contactManager/favoriteList.html',context=data)

def delContact(request, contact_id):
    contact = Contact.objects.get(id = contact_id)
    contact.delete()
    # contactList(request)
    return redirect(contactList)

def createGroup(request):
    return render(request, 'contactManager/Group/createGroup.html')

def createGroupPost(request):
    name = request.POST.get('name')
    group = Group(name=f'{name}')
    group.save()
    return redirect(listGroup)

def listGroup(request):
    allGroup = Group.objects.all()
    data = {'listGroup':allGroup}
    return render(request, 'contactManager/Group/listGroup.html', context=data)

def selectGroup(request, group_id):
    group = Group.objects.get(id = group_id)
    contactOfGroup = Contact.objects.filter(group_id = group_id)
    data = {'group':group, 'listContact': contactOfGroup}
    return render(request, 'contactManager/Group/selectGroup.html', context=data)

def editGroup(request, group_id):
    group = Group.objects.get(id = group_id)
    data = {'group':group}
    return render(request, 'contactManager/Group/editGroup.html', context=data)

def editGroupPost(request, group_id):
    group = Group.objects.get(id = group_id)
    group.name = request.POST.get('name')
    group.save()
    return redirect(listGroup)

def addContactInGroup(request,group_id):
    group = Group.objects.get(id = group_id)
    allContact = Contact.objects.all()
    data = {'group':group, 'listContact':allContact}
    return render(request, 'contactManager/Group/addContactInGroup.html', context=data)

def addContactInGroupPost(request, group_id):
    contactListId = request.POST.getlist('contactListId')
    groupObj = Group.objects.get(id = group_id)
    result = list(map(int, contactListId))
    contactList = Contact.objects.filter(pk__in = result)
    for c in contactList:
        c.group = groupObj
        c.save()
    
    return redirect(listGroup)

def testListContact(request):
    allContact = Contact.objects.all()
    data = {"listContact": allContact}
    return render(request, 'contactManager/testListContact.html', context=data)
    

def testListContactPost(request):
    contactList = request.POST.getlist('contactListId')
    return HttpResponse(f"""
                <div>Contacts: {contactList}</div>
            """)



    


