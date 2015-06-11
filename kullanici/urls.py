
from django.conf.urls import patterns, url
from kullanici import views
import django.contrib.auth

urlpatterns = patterns('',
                    url(r'^kullanici_kayit/$', 'kullanici.views.kullanici_kayit'),
                    url(r'^kullanici_profil/$', 'kullanici.views.kullanici_profil'),
                    url(r'kullanici_bilgileri_guncelle/$', 'kullanici.views.kullanici_bilgileri_guncelle'),
                    url(r'kullanici_sifre_degistir/$', 'kullanici.views.kullanici_sifre_degistir'),
                    url(r'^list/$', 'kullanici.views.list', name='list'),
                    url(r'^kullanici_profil/(.+)$', 'kullanici.views.view_profile'),

                      )


