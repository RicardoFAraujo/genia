# gen_influ/views.py
from django.shortcuts import render, redirect, get_object_or_404
from gen_influ.models import influencer
from django.urls import reverse
from forms.influencer_form import InfluencerForm
from .instagram_utils import get_instagram_profile_info, download_profile_pic
import os

def index(request):
    influencers = influencer.objects.all()
    return render(request, 'gen_influ/index.html', {"tabela": influencers})

def add_influencer(request):
    if request.method == 'POST':
        form = InfluencerForm(request.POST)
        if form.is_valid():
            arroba = form.cleaned_data['arroba']
            nome, seguidores, profile_pic_url = get_instagram_profile_info(arroba)
            if seguidores is not None:
                foto_path = download_profile_pic(profile_pic_url, arroba)
                relative_foto_path = foto_path.replace('static/', '') if foto_path else ""
                influencer_obj = influencer(
                    arroba=arroba,
                    nome=nome,
                    seguidores=seguidores,
                    foto=relative_foto_path
                )
                influencer_obj.save()
                return redirect(reverse('index'))
            else:
                # Tratar o caso de perfil não encontrado ou erro na API
                form.add_error('arroba', 'Erro ao buscar o perfil no Instagram: ' + nome)
    else:
        form = InfluencerForm()
    return render(request, 'gen_influ/index.html', {'form': form})

def edit_influencer(request):
    if request.method == 'POST':
        influencer_id = request.POST['id']
        influencer_obj = get_object_or_404(influencer, id=influencer_id)
        form = InfluencerForm(request.POST, instance=influencer_obj)
        if form.is_valid():
            form.save()
            return redirect(reverse('index'))
    return redirect(reverse('index'))

def delete_influencer(request, id):
    influencer_obj = get_object_or_404(influencer, id=id)
    influencer_obj.delete()
    return redirect(reverse('index'))
