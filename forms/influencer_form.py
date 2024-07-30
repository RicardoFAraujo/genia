# my_app/forms/influencer_form.py
from django import forms
from gen_influ.models import influencer

class InfluencerForm(forms.ModelForm):
    class Meta:
        model = influencer
        fields = ['nome', 'arroba', 'seguidores', 'range', 'score_medio']
       


