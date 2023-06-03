from django.shortcuts import render
from members.models import CustomUser


def rraffineurs(request):
    raffineurs = CustomUser.objects.all()

    return render(request, 'members/raffineurs.html', {'raffineurs': raffineurs})
