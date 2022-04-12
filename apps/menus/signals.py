from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.menus.models.menu import Menu


@receiver(post_save, sender=Menu)
def desactivate_menus(sender, instance, **kwargs):
    if instance.is_active:
        all_menus = Menu.objects.filter(brand=instance.brand)
        for menu in all_menus:
            if menu.id is not instance.id:
                post_save.disconnect(desactivate_menus, sender=Menu)
                menu.is_active = False
                menu.save()
                post_save.connect(desactivate_menus, sender=Menu)
