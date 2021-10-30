from random import randint

import folium
from django.shortcuts import render

from . import models
from good_neighbor_halloween.settings import MAP_LAT, MAP_LNG


def index(request):
    return render(request, "trick_or_treating/index.html")


def contact_us(request):
    return render(request, "trick_or_treating/contact_us.html")


def get_random_icon():
    mapping = [
        "https://cdn4.iconfinder.com/data/icons/halloween-freebie/130/_vampire-512.png",
        "https://cdn4.iconfinder.com/data/icons/halloween-freebie/130/_Zombie_skull-512.png",
        "https://cdn4.iconfinder.com/data/icons/halloween-freebie/130/_ghost-512.png",
        "https://cdn4.iconfinder.com/data/icons/halloween-freebie/130/_owl-512.png",
        "https://cdn4.iconfinder.com/data/icons/halloween-freebie/130/_cat-512.png",
        "https://cdn4.iconfinder.com/data/icons/halloween-freebie/130/_zombie_rising-512.png",
        "https://cdn4.iconfinder.com/data/icons/halloween-freebie/130/_frankenstein-512.png",
        "https://cdn4.iconfinder.com/data/icons/halloween-freebie/130/_stabbed_head-512.png",
    ]
    return mapping[randint(0, len(mapping) - 1)]


def map(request):
    locations = models.Address.objects.all()
    m = folium.Map(location=(MAP_LAT, MAP_LNG), zoom_start=14)
    for location in locations:
        custom_icon = folium.CustomIcon(
            get_random_icon(),
            icon_size=(48, 48),
        )
        folium.Marker(
            location=[location.latitude, location.longitude],
            popup=location.name,
            icon=custom_icon,
        ).add_to(m)
    return render(request, "trick_or_treating/map.html", {"map": m._repr_html_()})
