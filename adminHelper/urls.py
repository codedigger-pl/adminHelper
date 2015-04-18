from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from users.views import UserHomepage

from rest_framework.routers import DefaultRouter
from users.apiViewsets import PersonGroupViewset, PersonViewset, UserViewset
from alarm.apiViewsets import AlarmZoneViewset

router = DefaultRouter(trailing_slash=False)
router.register(r'personGroups', PersonGroupViewset)
router.register(r'persons', PersonViewset)
router.register(r'users', UserViewset)

router.register(r'alarmZones', AlarmZoneViewset)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adminHelper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', UserHomepage.as_view(), name='homepage'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/', include('users.urls')),
    url(r'^alarm/', include('alarm.urls')),

    # including API urls
    url(r'^api/', include(router.urls, namespace='api')),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
