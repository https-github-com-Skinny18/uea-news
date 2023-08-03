from django.shortcuts import render
from core.models import AtoNormativ

from core.models import BoletimGerado
# Create your views here.

def geral(request):
    portaria = AtoNormativ.objects.filter(tipo_ato='portaria', status='aprovado')
    resolucao = AtoNormativ.objects.filter(tipo_ato='Resolução', status='aprovado')
    boletim = BoletimGerado.objects.filter(status='aprovado')
    for b in boletim:
        ato_normativ_index = b.conteudo_pdf.find('AtoNormativ:')
        if ato_normativ_index != -1:
            b.conteudo_pdf = b.conteudo_pdf.replace('AtoNormativ:', '')  
        b.conteudo_pdf = b.conteudo_pdf.strip('[<>]')
    return render(request, 'geral.html', {'portaria': portaria, 'boletim': boletim, 'resolucao': resolucao})

