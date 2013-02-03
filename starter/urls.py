from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Enable admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Main
    url(r'^$', 'apps.main.views.home', name='home'),

    # Auth
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'), 

    # Admin
    url(r'^admin/', include(admin.site.urls)),
)

# Serve local static files in dev environment (i.e. DEBUG = True)
urlpatterns += staticfiles_urlpatterns()
