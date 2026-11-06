from django.contrib import admin
from history.models import History

@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    list_display = ['type', 'origin_user', 'target_user', 'amount', 'message', 'created_at']
    fieldsets = (
        ('Informacion Basica', {'fields': ['type', 'amount', 'origin_user', 'target_user', 'message', 'created_at']}),
    )
    readonly_fields = ['created_at']