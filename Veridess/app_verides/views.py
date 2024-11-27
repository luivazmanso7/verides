from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def contribuir(request):
    return render(request,'contribuir.html')

def inscricao(request):
    return render(request,'inscricao.html')

def doacoes(request):
    return render(request,'doacoes.html')

def catalogo(request):
    return render(request,'catalogo.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def sobrenos(request):
    return render(request, 'sobrenos.html')

def inscricao(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        sexo = request.POST['sexo']
        idade = request.POST['idade']
        telefone = request.POST['telefone']
        email = request.POST['email']
        sobre_voce = request.POST['sobre_voce']
        disponibilidade = request.POST['disponibilidade']

        assunto = f"Nova Inscrição de Voluntário: {nome}"
        mensagem = (
            f"Nome Completo: {nome}\n"
            f"Sexo: {sexo}\n"
            f"Idade: {idade}\n"
            f"Telefone: {telefone}\n"
            f"E-mail: {email}\n"
            f"Fale sobre você: {sobre_voce}\n"
            f"Disponibilidade: {disponibilidade}"
        )
        destinatario = 'rblt@cesar.school'
        send_mail(assunto, mensagem, 'rblt@cesar.school', [destinatario])

        return redirect('pagina_de_confirmacao')

    return render(request, 'inscricao.html')

def confirmacao(request):
    return render(request, 'confirmacao.html')

def faq_page(request):
    faqs = [
        {"question": "Como faço para virar um colaborador?", "answer": "Acesse a pagina Inscrição e clique no botão para se voluntariar."},
        {"question": "Como faço para entrar em contato?", "answer": "Use a opção Contato no Menu Inicial."},
        {"question": "Quais métodos de pagamento são aceitos nas doaçoes?", "answer": "Aceitamos Paypal, ou Pix para Danielle."},
    ]
    return render(request, 'faq.html', {'faqs': faqs})
