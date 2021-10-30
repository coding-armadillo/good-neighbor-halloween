import json
from random import randint

import boto3
import folium
import requests
from django.http import HttpResponseNotAllowed
from django.shortcuts import render


from . import forms, models
from good_neighbor_halloween.settings import (
    GCP_KEY,
    MAP_LAT,
    MAP_LNG,
    MAPQUEST_KEY,
    AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACCESS_KEY,
    AWS_REGION_NAME,
)


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


def get_clean_address(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"key": GCP_KEY, "address": address}

    try:
        resp = requests.get(url, params=params).json()
        lat = resp["results"][0]["geometry"]["location"]["lat"]
        lng = resp["results"][0]["geometry"]["location"]["lng"]
        addr = resp["results"][0]["formatted_address"]
    except:
        lat, lng, addr = None, None, address
    return addr, lat, lng


def get_stops(locations):
    url = "http://www.mapquestapi.com/directions/v2/optimizedroute"
    params = {"key": MAPQUEST_KEY}
    resp = requests.post(
        url,
        params=params,
        data=json.dumps({"locations": locations}),
    ).json()

    round_trip_time = resp["route"]["formattedTime"]
    seq = [int(j - 1) for j in resp["route"]["locationSequence"]][1:-1]

    stops = [locations[i] for i in seq]

    return stops, round_trip_time


def index(request):
    return render(request, "trick_or_treating/index.html")


def contact_us(request):
    return render(request, "trick_or_treating/contact_us.html")


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
            popup=location.label,
            icon=custom_icon,
        ).add_to(m)

    if request.method == "GET":
        form = forms.PlayForm()
        return render(
            request,
            "trick_or_treating/map.html",
            {
                "map": m._repr_html_(),
                "form": form,
            },
        )
    elif request.method == "POST":
        form = forms.PlayForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data.get("address")
            address, _, _ = get_clean_address(address)
            locations = (
                [address]
                + [addr.name for addr in locations if addr.name != address]
                + [address]
            )

            stops, round_trip_time = get_stops(locations)
            phone = form.cleaned_data.get("phone")
            if phone:
                client = boto3.client(
                    "sns",
                    aws_access_key_id=AWS_ACCESS_KEY_ID,
                    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                    region_name=AWS_REGION_NAME,
                )

                message = "Welcome to Good Neighbor Trick or Treat!\n\n"
                message += "Here are the stops in order:\n\n"
                message += "\n\n".join(stops)
                client.publish(
                    PhoneNumber=f"+1{phone}",
                    Message=message,
                )
            return render(
                request,
                "trick_or_treating/result.html",
                {
                    "map": m._repr_html_(),
                    "stops": stops,
                    "round_trip_time": round_trip_time,
                },
            )
    else:
        return HttpResponseNotAllowed("Method Not Allowed")


def route(request):
    pass
