from django.contrib import admin

# from django.contrib.auth.admin import UserAdmin

from django.utils.html import format_html
# from django.utils.safestring import mark_safe

from rest_framework.authtoken.admin import TokenAdmin

from . models import VcfFile


class VcfFileAdmin(admin.ModelAdmin):

    save_on_top = True
    list_display = ('__str__', 'created_at', 'updated_at',
                    'is_active', 'admin_inspect_file')
    list_filter = ('is_active',)
    ordering = ('-created_at',)
    search_fields = ('name',)
    date_hierarchy = 'created_at'

    def admin_inspect_file(self, obj):
        return format_html(
            '<a target="_blank" href="/file/{0}/records/">Open url</a>&nbsp;',
            obj.id
            )

    admin_inspect_file.allow_tags = True
    admin_inspect_file.short_description = 'Inspect this file'


admin.site.register(VcfFile, VcfFileAdmin)


TokenAdmin.raw_id_fields = ['user']
