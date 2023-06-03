from django.shortcuts import render


def tab_budgets(request):
    return render(request, 'budget/tableaux_budgetaires.html',{})


def plan_tresorie(request):
    return render(request,'budget/plan_tresorie.html', {})


def suivi_subvention(request):
    return render(request, 'budget/suivi_subvention.html', {})

