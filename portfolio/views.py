from django.shortcuts import render

from core.models import Pessoal

from portfolio.models import Certificado, Projeto


def home (request): #request: objeto da requisição http; render: pega um html e mostra ele no navegador
    pessoal = Pessoal.objects.first()
    certificados = Certificado.objects.all()
    return render(request,'portfolio/home.html', {'pessoal': pessoal, 'certificados': certificados})

def projetos(request):
    projeto = Projeto.objects.all()
    return render(request,'portfolio/projetos.html', {'projeto': projeto})

def contato(request):
    pessoal = Pessoal.objects.first()
    return render(request,'portfolio/contato.html', {'pessoal': pessoal})