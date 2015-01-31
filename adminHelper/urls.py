from django.conf.urls import patterns, include, url
from django.contrib import admin

from users.views import UserHomepage
from users.urls import router as users_router

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adminHelper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', UserHomepage.as_view(), name='homepage'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('users.urls')),

    # including API urls
    url(r'^api/users/', include(users_router.urls, namespace='api'))

)
