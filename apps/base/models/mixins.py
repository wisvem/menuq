from django.contrib.auth.mixins import UserPassesTestMixin
from django.db import models
from django.conf import settings
from django.contrib import admin
from crum import get_current_user
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin


class TimeStampMixin(models.Model):
    """
    Abstract class for time stamp
    """
    created = models.DateTimeField(
        auto_now_add=True
    )
    updated = models.DateTimeField(
        auto_now=True
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='%(class)s_created_by',
        blank=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
        related_name='%(class)s_updated_by',
        blank=True
    )

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super(TimeStampMixin, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class BasicInfoMixin(models.Model):
    """Abstract class for basic info
    """
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    description = models.TextField(
        max_length=10000,
        null=True,
        blank=True
    )

    class Meta:
        abstract = True


class SaveAdminMixin(admin.ModelAdmin):
    readonly_fields = [
        'created_by',
        'updated_by'
    ]

    def save_model(self, request, obj, form, change):
        if not change:
            obj.created_by = request.user
        obj.updated_by = request.user
        obj.save()

    class Meta:
        abstract = True

class OwnerMixin(LoginRequiredMixin, UserPassesTestMixin):
    
    def test_func(self):
        self.owner = self.get_object().created_by
        return self.request.user == self.owner

    # def handle_no_permission(self):
    #     return JsonResponse(
    #         {'message': 'You don\'t have access to edit this'}
    #     )
