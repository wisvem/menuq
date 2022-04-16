from django.dispatch import receiver
from apps.companies.models import Brand
from apps.menus.models import Product
from django.db.models.signals import post_delete, pre_save
import os


@receiver(post_delete, sender=Brand)
@receiver(post_delete, sender=Product)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding object is deleted.
    """
    if instance.photo:
        if os.path.isfile(instance.photo.path):
            os.remove(instance.photo.path)


@receiver(pre_save, sender=Brand)
@receiver(pre_save, sender=Product)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding object is updated
    with new file or without file.
    """
    cls_name = instance.__class__.__name__
    if not instance.pk:
        return False
    try:
        old_file = instance.__class__.objects.get(pk=instance.pk).photo
    except instance.__class__.DoesNotExist:
        return False

    new_file = instance.photo

    if old_file and not (old_file == new_file):
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
