from django import forms
from .models import *

CATEGORY = (("1", "Bệnh thường gặp"), ("2", "Bệnh tim - huyết áp"), ("3", "Bệnh gan - thận"), ("4", "Bệnh tiêu hóa"),
            ("5", "Bệnh xương khớp"), ("6", "Bệnh mất ngủ"), ("7", "Bệnh tiểu đường"), ("8", "Bệnh truyền nhiễm"),
            ("9", "Chăm sóc sức khỏe"), ("10", "Khác"),

)


class CreatePostForm(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": "form-control"}), required=True)
    post_image = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control", "onchange": "preview()"}),
                                 required=True)
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "style": "height: 300px"}),
                              required=True)
    category = forms.ChoiceField(choices=CATEGORY, widget=forms.Select(attrs={"class": "form-control"}), required=True)


class EditUserForm(forms.Form):
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    username = forms.CharField(max_length=50,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    phone = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    address = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"class": "form-control"}))
    user_image = forms.FileField(widget=forms.FileInput(attrs={"class": "form-control",  "onchange": "preview()"}), required=False)
