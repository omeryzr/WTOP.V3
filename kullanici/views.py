from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from kullanici.forms import *
from django.forms.util import ErrorList

# Create your views here.

def kullanici_kayit(request):
    if request.method == 'POST':

            try:
                username = request.POST.get('username')
                password = request.POST.get('password')
                email = request.POST.get('email')
                member_user_auth = User.objects.create_user(username, email, password)
                member_user_auth.save()
                mmbr= Member(username=username, email=email, password=password)
                mmbr.save()
                return HttpResponseRedirect('/accounts/login/')
            except Exception as e:
                print e
                return HttpResponseRedirect('/404')
    return render_to_response('kullanici_kayit.html', context_instance=RequestContext(request))




@login_required
def kullanici_profil(request):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        return render_to_response('kullanici_profil.html', locals())
    except Exception as e:
        print e
        return HttpResponseRedirect('/404')

@login_required
def kullanici_bilgileri_guncelle(request):
    try:
        if Member.objects.filter(username=request.user.username):
            member = Member.objects.filter(username=request.user.username)[0]

        else:
            member = Member(username=request.user.username)
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')


    form_first_and_last_name = edit_profile_first_and_last_name_form(initial={  'first_name': request.user.first_name,
                                                                                'last_name': request.user.last_name,
                                                                                'email': member.email,
                                                                                'email': request.user.email,
                                                                                'points': member.points,
                                                                                'twitter': member.twitter,
                                                                                'facebook': member.facebook,
                                                                                'linkedn': member.linkedn,
                                                                                'googleplus': member.googleplus,
                                                                                'hakkinda': member.hakkinda,
                                                                                'bolum': member.bolum,
                                                                                'sinif': member.sinif,
                                                                                })

    if request.method == 'POST' and 'profile_photo' in request.POST:


            try:
                member.photo = request.FILES["photo"]
                member.save()
                print member.photo
                return HttpResponseRedirect('/kullanici/kullanici_profil')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')

    elif request.method == 'POST' and 'name_form' in request.POST:  # password form
        form_first_and_last_name = edit_profile_first_and_last_name_form(request.POST)
        if form_first_and_last_name.is_valid():
                try:
                    first_name = request.POST.get('first_name')
                    last_name = request.POST.get('last_name')
                    email = request.POST.get('email')
                    twitter = request.POST.get('twitter')
                    facebook = request.POST.get('facebook')
                    linkedn = request.POST.get('linkedn')
                    googleplus = request.POST.get('googleplus')
                    hakkinda = request.POST.get('hakkinda')
                    bolum = request.POST.get('bolum')
                    sinif = request.POST.get('sinif')
                    points = request.POST.get('points')
                    request.user.first_name = first_name
                    request.user.last_name = last_name
                    request.user.email = email
                    member.email = email
                    member.googleplus = googleplus
                    member.linkedn = linkedn
                    member.hakkinda = hakkinda
                    member.bolum = bolum
                    member.sinif = sinif
                    member.points = points
                    member.twitter = twitter
                    member.facebook = facebook
                    request.user.save()
                    member.save()
                    return HttpResponseRedirect('/kullanici/kullanici_profil')
                except Exception as e:
                    print e
                    return HttpResponseRedirect('/sorry')

    return render_to_response('kullanici_bilgileri_guncelle.html', locals(), context_instance=RequestContext(request))

def kullanici_sifre_degistir(request):
    try:
        member = Member.objects.filter(username=request.user.username)[0]
        member_pw = User.objects.filter(username=request.user.username)[0]
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')

    form = edit_member_profile_form()
    form_password = edit_member_password_form  # for change password

    if request.method == 'POST' and 'submit' in request.POST:  # normal form
        form = edit_member_profile_form(request.POST, request.FILES)
        if form.is_valid():
            try:
                member.profile_photo = request.FILES["profile_photo"]
                member.save()
                return HttpResponseRedirect('/kullanici/kullanici_profil')
            except Exception as e:
                print e
                return HttpResponseRedirect('/sorry')

    elif request.method == 'POST' and 'Change Password' in request.POST:  # password form
        form_password = edit_member_password_form(request.POST)
        if form_password.is_valid():
            if member.password == request.POST.get('old_password') and request.POST.get(
                    'new_password') == request.POST.get('confirm_password'):
                try:
                    member.password = request.POST.get('new_password')
                    member_pw.set_password(request.POST.get('new_password'))
                    member.save()
                    member_pw.save()
                    return HttpResponseRedirect('/kullanici/kullanici_profil')
                except Exception as e:
                    print e
                    return HttpResponseRedirect('/sorry')


    return render_to_response('kullanici_sifre_degistir.html',
                              {'form': form, 'form_password': form_password, 'request': request},
                              context_instance=RequestContext(request))



def list(request):
    member = Member.objects.get(username=request.user.username)
    print member
   # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'], member=member)
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('kullanici.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form


    if request.method == 'POST' and 'new_permission' in request.POST:
        member = Member.objects.get(username=request.POST.get('username'))
        document = Document.objects.get(id=int(request.POST.get('doc_id')))
        new_permission = Permission(member=member, document=document )
    #
    #     doc_list = Document.object.filter(id__in=Permission.objects.filter(member=member).values('document'))


    # Load documents for the list page
    documents = Document.objects.filter(member=member).all()
    # Render list page with the documents and the form
    return render_to_response(
        'list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )



def view_profile(request, username):
    print "sa"
    member = Member.objects.filter(username=username)[0]
    print member.username
    return render_to_response(
        'kullanici_profil.html', locals(),
        context_instance=RequestContext(request)
    )


