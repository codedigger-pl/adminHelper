from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin

from rest_framework.routers import DefaultRouter

from users.views import UserHomepage
from users.apiViewsets import PersonGroupViewset, PersonViewset, UserViewset
from alarm.apiViewsets import AlarmZoneViewset, AlarmOrderViewset, AlarmRuleViewset, AlarmRequestViewset
from acs.apiViewsets import ACSOrderViewset, ACSRequestViewset, ACSRuleViewset, ACSZoneViewset

router = DefaultRouter(trailing_slash=False)
router.register(r'personGroups', PersonGroupViewset)
router.register(r'persons', PersonViewset)
router.register(r'users', UserViewset)

router.register(r'alarmZones', AlarmZoneViewset)
router.register(r'alarmRules', AlarmRuleViewset)
router.register(r'alarmOrders', AlarmOrderViewset)
router.register(r'alarmRequests', AlarmRequestViewset)

router.register(r'ACSZones', ACSZoneViewset)
router.register(r'ACSRules', ACSRuleViewset)
router.register(r'ACSOrders', ACSOrderViewset)
router.register(r'ACSRequests', ACSRequestViewset)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'adminHelper.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', UserHomepage.as_view(), name='homepage'),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^users/', include('users.urls')),
    url(r'^alarm/', include('alarm.urls')),
    url(r'^acs/', include('acs.urls')),

    # including API urls
    url(r'^api/', include(router.urls, namespace='api')),
    url(r'^api/rest-auth/', include('rest_auth.urls'))

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
