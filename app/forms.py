from django import forms
from app.models import Package

#class PostFormUpgradeHost(slug, forms.Form):
#    packages = forms.CheckboxSelectMultiple(required=True, choices=Package.objects.filter(slug=slug))
#    created_at = forms.DateTimeField()

class PostFormUpgradeHost(forms.Form):
    packages = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="Notify and subscribe package to this post: ")

