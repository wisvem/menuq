import qrcode
from crum import get_current_request
from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.companies.models.brand import Brand
from io import BytesIO
from django.core.files import File


@receiver(post_save, sender=Brand)
def generate_qr(sender, instance, **kwargs):
    if not instance.qr_code:
        blob = BytesIO()
        # get domain
        request = get_current_request()
        # build image path
        qr_url = f'http://{request.META["HTTP_HOST"]}'
        qr_url += f'/menu/active/{instance.id}'
        # create qr code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=20,
            border=4,
        )
        qr.add_data(qr_url)
        img = qr.make_image()
        # save qr code
        img.save(blob, 'PNG')
        post_save.disconnect(generate_qr, sender=Brand)
        instance.qr_code.save(
            f'qr_{instance.name}{instance.id}.png', File(blob)
        )
        blob.close()
        qr.clear()
        post_save.connect(generate_qr, sender=Brand)
