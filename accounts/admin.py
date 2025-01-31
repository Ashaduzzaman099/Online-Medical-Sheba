from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    # Fields to display in the user list view
    list_display = [
        'email',
        'full_name',
        'user_name',
        'phone_number',
        'date_of_birth',
        'role',
        'is_active',
        'is_doctor',
        'is_admin',
        'updated_at',
    ]
    
    # Filters to apply in the user list view
    list_filter = ["is_admin", "role", "is_active", "is_doctor"]
    
    # Fieldsets to organize fields on the user detail edit page
    fieldsets = [
        ("Personal Info", {"fields": ["full_name", "user_name", "phone_number", "date_of_birth", "blood_group", "wants_to_donate_blood", "profile_pic"]}),
        ("User Credentials", {"fields": ["email", "password"]}),
        ("Permissions", {"fields": ["is_active", "is_doctor", "is_admin"]}),
        # Exclude 'created_at' and 'updated_at' from the form fields
        ("Timestamps", {"fields": [], "classes": ["collapse"]}),
    ]

    # Make the password field editable in the admin
    def save_model(self, request, obj, form, change):
        if form.cleaned_data['password']:
            obj.set_password(form.cleaned_data['password'])
        super().save_model(request, obj, form, change)

    # Allow search by email and full name
    search_fields = ['email', 'full_name', 'user_name']
    
    # Pagination settings (if needed)
    list_per_page = 10

    # Make 'created_at' and 'updated_at' read-only in the admin
    def get_readonly_fields(self, request, obj=None):
        return ['created_at', 'updated_at']  # Make both fields read-only

    # Optional: Change the default ordering
    ordering = ['created_at']

    # Add custom actions if necessary
    actions = ['make_active', 'make_inactive']

    def make_active(self, request, queryset):
        queryset.update(is_active=True)
        self.message_user(request, "Selected users have been activated.")

    make_active.short_description = "Activate selected users"

    def make_inactive(self, request, queryset):
        queryset.update(is_active=False)
        self.message_user(request, "Selected users have been deactivated.")

    make_inactive.short_description = "Deactivate selected users"
