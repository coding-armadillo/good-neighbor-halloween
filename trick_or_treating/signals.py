import requests

from good_neighbor_halloween.settings import GCP_KEY


def prepare_address(sender, instance, created, **kwargs):
    if created:
        url = "https://maps.googleapis.com/maps/api/geocode/json"
        params = {"key": GCP_KEY, "address": instance.name}
        try:
            resp = requests.get(url, params=params).json()
            lat = resp["results"][0]["geometry"]["location"]["lat"]
            lng = resp["results"][0]["geometry"]["location"]["lng"]
            addr = resp["results"][0]["formatted_address"]
        except:
            lat, lng, addr = None, None, instance.name

        instance.latitude = lat
        instance.longitude = lng
        instance.name = addr
        instance.save()
