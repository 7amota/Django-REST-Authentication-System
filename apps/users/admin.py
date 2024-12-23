from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.http import HttpRequest

from .models import User, ResetPassword

from rest_framework.authtoken.models import Token
from unfold.contrib.forms.widgets import WysiwygWidget
from unfold.admin import ModelAdmin, TabularInline
from unfold.decorators import action, display
from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm





@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    change_password_form = AdminPasswordChangeForm
    list_display = [
        "display_header",
        "is_active",
        "display_staff",
        "display_superuser",
        "display_created",
    ]
    fieldsets = (
        (None, {"fields": ("username", "password",'email','phoneNumber','image')}),
        (
            ("Personal info"),
            {"fields": (("first_name", "last_name",),)},
        ),
        (
            ("Activation"),
            {"fields": (("is_activated"),)},
        ),
        (
            ("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                    
                ),
            },
        ),
        (("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    filter_horizontal = (
        "groups",
        "user_permissions",
    )

    readonly_fields = ["last_login", "date_joined"]

    @display(description=("User"), header=True)
    def display_header(self, instance: User):
        return instance.first_name, instance.email

    @display(description=("Staff"), boolean=True)
    def display_staff(self, instance: User):
        return instance.is_staff

    @display(description=("Superuser"), boolean=True)
    def display_superuser(self, instance: User):
        return instance.is_superuser

    @display(description=("Created"))
    def display_created(self, instance: User):
        return instance.date_joined
    
    def has_add_permission(self, request: HttpRequest) -> bool:
        return False

@admin.register(ResetPassword)
class ResetAdmin(ModelAdmin):
    fields= ['user','token',"is_checked"]
    list_display = ['user',"is_checked"]