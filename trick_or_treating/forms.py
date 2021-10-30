from django import forms


class PlayForm(forms.Form):
    address = forms.CharField(
        label="Address",
        max_length=200,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-3 py-2 placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-indigo-100 focus:border-indigo-300",
                "placeholder": "Your address",
            }
        ),
    )
    phone = forms.CharField(
        label="Phone number",
        max_length=20,
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-3 py-2 placeholder-gray-300 border border-gray-300 rounded-md focus:outline-none focus:ring focus:ring-indigo-100 focus:border-indigo-300",
                "placeholder": "Your phone number",
            }
        ),
        required=False,
    )
