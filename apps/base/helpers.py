import os
from django.db.utils import IntegrityError


def custom_path(instance, filename):
    """
    Function to create a string that would be used as a path
    to upload an image or file and mantain only one file
    """
    cls_name = instance.__class__.__name__
    filename = f'{instance.id}-{instance.name}{filename[filename.rfind("."):]}'
    try:
        obj = instance.__class__.objects.get(pk=instance.id)
        if obj.photo:
            obj.photo.delete()
    except:
        print('tu tranquilo')
    if cls_name == 'Product':
        path = f'brands/{instance.brand_id}/products'
    else:
        path = f'brands/{instance.id}-{instance.name}'
    return f'{path}/{filename}'


def clone_object(obj, attrs={}):
    """
    Function to clone any existing object
    """

    # we start by building a "flat" clone
    clone = obj._meta.model.objects.get(pk=obj.pk)
    clone.pk = None

    # if caller specified some attributes to be overridden, use them
    for key, value in attrs.items():
        setattr(clone, key, value)

    # save the partial clone to have a valid ID assigned
    clone.save()

    # Scan field to further investigate relations
    fields = clone._meta.get_fields()
    for field in fields:

        # Manage M2M fields by replicating all related records found on parent "obj" into "clone"
        if not field.auto_created and field.many_to_many:
            for row in getattr(obj, field.name).all():
                getattr(clone, field.name).add(row)

        # Manage 1-N and 1-1 relations by cloning child objects
        if field.auto_created and field.is_relation:
            if field.many_to_many:
                # do nothing
                pass
            else:
                # provide "clone" object to replace "obj" on remote field
                attrs = {field.remote_field.name: clone}
                children = field.related_model.objects.filter(
                    **{field.remote_field.name: obj})
                for child in children:
                    clone_object(child, attrs)

    return clone
