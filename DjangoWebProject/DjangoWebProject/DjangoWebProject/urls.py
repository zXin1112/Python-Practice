"""
Definition of urls for DjangoWebProject.
"""

from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
    # Examples:
    # url(r'^$', DjangoWebProject.views.home, name='home'),
    # url(r'^DjangoWebProject/', include('DjangoWebProject.DjangoWebProject.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
     #添加模块
     url(r'',include('learning_logs.urls',namespace='learning_logs')),
     url(r'',include('users.urls',namespace='users'))

]
