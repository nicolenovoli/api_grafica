from app.models.produto_model import Produto


def criar_produtos_iniciais(db):
    produtos = [
        {
            "nome": "Cartões de Visita",
            "descricao": "Cartões de visita com impressão de alta definição, cores vivas e acabamento profissional.",
            "preco": 89.00,
            "imagem": "cartoes_visita.png"
        },
        {
            "nome": "Panfletos",
            "descricao": "Panfletos coloridos para divulgação de promoções, eventos e serviços.",
            "preco": 120.00,
            "imagem": "panfletos.png"
        },
        {
            "nome": "Pastas Personalizadas",
            "descricao": "Pastas com bolso interno e impressão personalizada.",
            "preco": 320.00,
            "imagem": "pastas.png"
        },
        {
            "nome": "Cartazes",
            "descricao": "Cartazes em diversos tamanhos com cores vibrantes.",
            "preco": 45.00,
            "imagem": "cartazes.png"
        },
        {
            "nome": "Folders",
            "descricao": "Folders com dobras profissionais para apresentar serviços, produtos ou portfólios.",
            "preco": 180.00,
            "imagem": "folders.png"
        },
        {
            "nome": "Etiquetas Adesivas",
            "descricao": "Etiquetas adesivas personalizadas para produtos, embalagens e identificação.",
            "preco": 65.00,
            "imagem": "etiquetas.png"
        },
        {
            "nome": "Receituário Médico",
            "descricao": "Blocos de receituário médico personalizados com dados do profissional, CRM e logotipo.",
            "preco": 75.00,
            "imagem": "receituario.png"
        }
    ]

    for item in produtos:
        produto_existe = db.query(Produto).filter(
            Produto.nome == item["nome"]
        ).first()

        if produto_existe is None:
            novo_produto = Produto(
                nome=item["nome"],
                descricao=item["descricao"],
                preco=item["preco"],
                imagem=item["imagem"]
            )

            db.add(novo_produto)

    db.commit()