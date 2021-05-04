from django.contrib import admin
from case.models import Case, CaseResult

# Register your models here.

class CaseResultInline(admin.TabularInline):
    model = CaseResult

@admin.register(Case)
class CaseAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "message"
    ]
    inlines = [
        CaseResultInline,
    ]
