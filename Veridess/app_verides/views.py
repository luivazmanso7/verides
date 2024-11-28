
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

from django.shortcuts import render, redirect

def home(request):
    return render(request, 'index.html')

def contribuir(request):
    return render(request, 'contribuir.html')

def catalogo(request):
    produtos = [
        {'id': 1, 'nome': 'Boneco Aventureiro', 'preco': 59.90, 'descricao': 'Boneco divertido e educativo.', 'data': '2024-11-01'},
        {'id': 2, 'nome': 'Boneco Felpudo', 'preco': 79.90, 'descricao': 'Boneco felpudo e macio.', 'data': '2024-11-02'},
        {'id': 3, 'nome': 'Boneco Aventureiro', 'preco': 65.00, 'descricao': 'Boneco ideal para aventuras.', 'data': '2024-11-03'},
        {'id': 4, 'nome': 'Boneco Criativo', 'preco': 45.99, 'descricao': 'Boneco criativo e inspirador.', 'data': '2024-11-04'},
        {'id': 5, 'nome': 'Boneco Clássico', 'preco': 60.00, 'descricao': 'Boneco de design clássico.', 'data': '2024-11-05'},
        {'id': 6, 'nome': 'Boneco Colorido', 'preco': 64.00, 'descricao': 'Boneco com cores vibrantes.', 'data': '2024-11-06'},
        {'id': 7, 'nome': 'Boneco Divertido', 'preco': 69.99, 'descricao': 'Boneco para horas de diversão.', 'data': '2024-11-07'},
        {'id': 8, 'nome': 'Boneco Fofinho', 'preco': 55.90, 'descricao': 'Boneco macio e fofinho.', 'data': '2024-11-08'},
    ]

    nome = request.GET.get('nome', '').strip().lower()
    ordenacao = request.GET.get('ordenacao', '')

    if nome:
        produtos = [p for p in produtos if nome in p['nome'].lower()]

    if ordenacao == 'preco':
        produtos = sorted(produtos, key=lambda x: x['preco'])
    elif ordenacao == 'recentes':
        produtos = sorted(produtos, key=lambda x: x['data'], reverse=True)

    return render(request, 'catalogo.html', {'produtos': produtos})

def produto_detalhes(request, id):
    return render(request, f'produto{id}.html')



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

