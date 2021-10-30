from .views import get_clean_address


def prepare_address(sender, instance, created, **kwargs):
    if created:
        addr, lat, lng = get_clean_address(instance.name)

        instance.latitude = lat
        instance.longitude = lng
        instance.name = addr
        instance.save()
