from django.contrib import admin
from .models import *

admin.site.register(Advertiser)
# admin.site.register(Ad)
admin.site.register(Click)
admin.site.register(View)


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    fields = ('title', 'approve')
    list_filter = ('approve',)
    search_fields = ('title',)
