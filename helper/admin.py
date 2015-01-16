from django.contrib import admin

from .models import (SysUser,
                     Person, PersonGroup,
                     ACSConfirm, ACSOrder, ACSRequest, ACSRule, ACSZone,
                     AlarmConfirm, AlarmOrder, AlarmRequest, AlarmRule, AlarmZone,
                     Key, KeyConfirm, KeyOrder, KeyRequest, KeyRule)

admin.site.register(SysUser)

admin.site.register(Person)
admin.site.register(PersonGroup)

admin.site.register(ACSZone)
admin.site.register(ACSRule)
admin.site.register(ACSRequest)
admin.site.register(ACSOrder)
admin.site.register(ACSConfirm)

admin.site.register(AlarmZone)
admin.site.register(AlarmRule)
admin.site.register(AlarmRequest)
admin.site.register(AlarmOrder)
admin.site.register(AlarmConfirm)

admin.site.register(Key)
admin.site.register(KeyRule)
admin.site.register(KeyRequest)
admin.site.register(KeyOrder)
admin.site.register(KeyConfirm)
