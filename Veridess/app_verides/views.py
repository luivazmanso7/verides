from django.shortcuts import render, redirect
from django.core.mail import send_mail

def home(request):
    return render(request, 'index.html')

def contribuir(request):
    return render(request, 'contribuir.html')

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
        remetente = 'rblt@cesar.school'
        send_mail(assunto, mensagem, remetente, [destinatario])

        return redirect('pagina_de_confirmacao')

    return render(request, 'inscricao.html')

def doacoes(request):
    return render(request, 'doacoes.html')

def catalogo(request):
    produtos = [
        {'id': 1, 'nome': 'Boneco Aventureiro', 'preco': 59.90, 'descricao': 'Boneco divertido e educativo.', 'data': '2024-11-01', 'imagem': 'fotos/boneco1.jpg'},
        {'id': 2, 'nome': 'Boneco Felpudo', 'preco': 79.90, 'descricao': 'Boneco felpudo e macio.', 'data': '2024-11-02', 'imagem': 'fotos/boneco2.jpg'},
        {'id': 3, 'nome': 'Boneco Aventureiro', 'preco': 65.00, 'descricao': 'Boneco ideal para aventuras.', 'data': '2024-11-03', 'imagem': 'fotos/boneco3.jpg'},
        {'id': 4, 'nome': 'Boneco Criativo', 'preco': 45.99, 'descricao': 'Boneco criativo e inspirador.', 'data': '2024-11-04', 'imagem': 'fotos/boneco4.jpg'},
        {'id': 5, 'nome': 'Boneco Clássico', 'preco': 60.00, 'descricao': 'Boneco de design clássico.', 'data': '2024-11-05', 'imagem': 'fotos/boneco5.jpg'},
        {'id': 6, 'nome': 'Boneco Colorido', 'preco': 64.00, 'descricao': 'Boneco com cores vibrantes.', 'data': '2024-11-06', 'imagem': 'fotos/boneco6.jpg'},
        {'id': 7, 'nome': 'Boneco Divertido', 'preco': 69.99, 'descricao': 'Boneco para horas de diversão.', 'data': '2024-11-07', 'imagem': 'fotos/boneco7.jpg'},
        {'id': 8, 'nome': 'Boneco Fofinho', 'preco': 55.90, 'descricao': 'Boneco macio e fofinho.', 'data': '2024-11-08', 'imagem': 'fotos/boneco8.jpg'},
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

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        assunto = f"Mensagem de Contato: {subject}"
        mensagem = (
            f"Nome: {name}\n"
            f"E-mail: {email}\n"
            f"Mensagem:\n{message}"
        )
        destinatario = 'rblt@cesar.school'
        remetente = 'rblt@cesar.school'
        send_mail(assunto, mensagem, remetente, [destinatario])

        return redirect('pagina_de_confirmacao')

    return render(request, 'contato.html')

def sobrenos(request):
    return render(request, 'sobrenos.html')

def material(request):
    return render(request, 'material.html')

def formulariodoacao(request):
    return render(request, 'formulariodoacao.html')

def pergmaterial(request):
    return render(request, 'pergmaterial.html')

def processar_doacao(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        item = request.POST.get('item')
        cidade = request.POST.get('cidade')
        cep = request.POST.get('cep')
        endereco = request.POST.get('endereco')
        outro_item = request.POST.get('outro_item', 'N/A')
        mensagem_texto = request.POST.get('mensagem')

        assunto = f"Nova Doação de Material de {nome}"
        mensagem = (
            f"Nome: {nome}\n"
            f"E-mail: {email}\n"
            f"Telefone: {telefone}\n"
            f"Item para doação: {item}\n"
            f"Cidade/Estado: {cidade}\n"
            f"CEP: {cep}\n"
            f"Endereço: {endereco}\n"
            f"Outro item para doação: {outro_item}\n"
            f"Mensagem:\n{mensagem_texto}"
        )
        destinatario = 'rblt@cesar.school'
        remetente = 'rblt@cesar.school'
        send_mail(assunto, mensagem, remetente, [destinatario])

        return redirect('pagina_de_confirmacao')

    else:
        return redirect('pergmaterial')

def confirmacao(request):
    return render(request, 'confirmacao.html')

def faq_page(request):
    faqs = [
        {"question": "Como faço para virar um colaborador?", "answer": "Acesse a página Inscrição e clique no botão para se voluntariar."},
        {"question": "Como faço para entrar em contato?", "answer": "Use a opção Contato no Menu Inicial."},
        {"question": "Quais métodos de pagamento são aceitos nas doações?", "answer": "Aceitamos Paypal ou Pix para Danielle."},
    ]
    second_faqs = [
        {"question": "Quais materiais são usados na confecção dos bonecos?", "answer": "Materiais 100% reciclados."},
        {"question": "Que tipo de mão de obra é utilizada?", "answer": "Nossos colaboradores são apenas mulheres em situação de vulnerabilidade que necessitam de ajuda."},
        {"question": "Qual o nome das redes sociais da marca?", "answer": "fabricas_de_ideias"},
    ]
    return render(request, 'faq.html', {'faqs': faqs, 'second_faqs': second_faqs})
