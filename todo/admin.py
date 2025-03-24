from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ("id","title", "created", "completed", "user")
    list_filter = ("completed", "created", "user")
    search_fields = ("title", "memo")
    readonly_fields = ("created",)
    fieldsets = (
        ("Basic Information", {"fields": ("title", "memo", "completed")}),
        ("User Information", {"fields": ("user", "created")}),
    )


admin.site.register(Todo, TodoAdmin)
# Register your models here.
