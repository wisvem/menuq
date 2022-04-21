import os

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
