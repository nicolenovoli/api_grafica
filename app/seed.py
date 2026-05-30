from app.models.produto_model import Produto
from app.models.produto_opcao_model import ProdutoOpcao


def criar_produtos_iniciais(db):

    produtos = [

        {
            "nome": "Cartões de Visita",

            "descricao":
                "Cartões de visita com impressão de alta definição.",

            "preco_base": 89.00,

            "opcoes": [

                {
                    "grupo": "Papel",
                    "nome": "Couchê 250g",
                    "valor_adicional": 0
                },

                {
                    "grupo": "Papel",
                    "nome": "Couchê 300g",
                    "valor_adicional": 20
                },

                {
                    "grupo": "Acabamento",
                    "nome": "Sem verniz",
                    "valor_adicional": 0
                },

                {
                    "grupo": "Acabamento",
                    "nome": "Verniz Total",
                    "valor_adicional": 15
                },
            ],
        },

        {
            "nome": "Panfletos",

            "descricao":
                "Panfletos coloridos para divulgação.",

            "preco_base": 120.00,

            "opcoes": [

                {
                    "grupo": "Quantidade",
                    "nome": "100 unidades",
                    "valor_adicional": 0
                },

                {
                    "grupo": "Quantidade",
                    "nome": "500 unidades",
                    "valor_adicional": 80
                },
            ],
        },

        {
            "nome": "Pastas Personalizadas",

            "descricao":
                "Pastas com bolso interno e impressão personalizada.",

            "preco_base": 320.00,

            "opcoes": [

                {
                    "grupo": "Material",
                    "nome": "Triplex 300g",
                    "valor_adicional": 0
                },

                {
                    "grupo": "Material",
                    "nome": "Supremo 350g",
                    "valor_adicional": 40
                },
            ],
        },

        {
            "nome": "Cartazes",

            "descricao":
                "Cartazes em diversos tamanhos com cores vibrantes.",

            "preco_base": 45.00,

            "opcoes": [

                {
                    "grupo": "Tamanho",
                    "nome": "A4",
                    "valor_adicional": 0
                },

                {
                    "grupo": "Tamanho",
                    "nome": "A3",
                    "valor_adicional": 20
                },
            ],
        },

        {
            "nome": "Folders",

            "descricao":
                "Folders com dobras profissionais.",

            "preco_base": 180.00,

            "opcoes": [

                {
                    "grupo": "Dobras",
                    "nome": "2 dobras",
                    "valor_adicional": 0
                },

                {
                    "grupo": "Dobras",
                    "nome": "3 dobras",
                    "valor_adicional": 25
                },
            ],
        },

        {
            "nome": "Etiquetas Adesivas",

            "descricao":
                "Etiquetas adesivas personalizadas.",

            "preco_base": 65.00,

            "opcoes": [

                {
                    "grupo": "Formato",
                    "nome": "Redonda",
                    "valor_adicional": 0
                },

                {
                    "grupo": "Formato",
                    "nome": "Quadrada",
                    "valor_adicional": 10
                },
            ],
        },

        {
            "nome": "Receituário Médico",

            "descricao":
                "Blocos personalizados para clínicas.",

            "preco_base": 75.00,

            "opcoes": [

                {
                    "grupo": "Quantidade",
                    "nome": "50 folhas",
                    "valor_adicional": 0
                },

                {
                    "grupo": "Quantidade",
                    "nome": "100 folhas",
                    "valor_adicional": 30
                },
            ],
        },
    ]

    for item in produtos:

        produto_existe = db.query(Produto).filter(
            Produto.nome == item["nome"]
        ).first()

        if produto_existe is None:

            novo_produto = Produto(

                nome=item["nome"],

                descricao=item["descricao"],

                preco_base=item["preco_base"],
            )

            db.add(novo_produto)

            db.flush()

            for opcao in item["opcoes"]:

                nova_opcao = ProdutoOpcao(

                    grupo=opcao["grupo"],

                    nome=opcao["nome"],

                    valor_adicional=
                        opcao["valor_adicional"],

                    produto_id=novo_produto.id,
                )

                db.add(nova_opcao)

    db.commit()