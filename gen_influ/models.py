from django.db import models

class influencer(models.Model):
    nome = models.CharField(max_length=100, null=True, blank=True)  # Tornar opcional
    arroba = models.CharField(max_length=25, null=False, blank=False, unique=True)  # Campo obrigatório
    range = models.CharField(max_length=10, null=True, blank=True)  # Tornar opcional
    seguidores = models.BigIntegerField(null=True, blank=True)  # Tornar opcional
    score_medio = models.FloatField(null=True, blank=True)  # Tornar opcional
    foto = models.CharField(max_length=100, null=True, blank=True)  # Tornar opcional
    
    def __str__(self) -> str:
        return f"Influencer [nome={self.nome}]"
