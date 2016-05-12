from django.contrib import admin

from apps.commands.models import Command


class CommandAdmin(admin.ModelAdmin):
    pass


admin.site.register(Command, CommandAdmin)
