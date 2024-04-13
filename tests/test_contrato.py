import pytest
from datetime import datetime
from src.contrato import Vendas
from pydantic import ValidationError

def test_vendas_com_dados_validados():

    dados_validados = {
        'email' : 'comprador@example.com',
        'data' : datetime.now(),
        'valor' : 100.50,
        'produto' : 'Produto X',
        'quantidade' : 3,
        'categoria' : 'categoria3',
    }

    venda = Vendas(**dados_validados)

    assert venda.email == dados_validados['email']
    assert venda.data == dados_validados['data']
    assert venda.valor == dados_validados['valor']
    assert venda.produto == dados_validados['produto']
    assert venda.quantidade == dados_validados['quantidade']
    assert venda.categoria == dados_validados['categoria']

def test_vendas_com_dados_invalidos():

    """
    Testa a criação de uma instância da classe Vendas com dados inválidos.

    Este teste verifica a validação de dados na classe Vendas. Dados inválidos incluem um email incorreto,
    data em formato inválido, valor negativo, nome do produto vazio, quantidade negativa, e uma categoria válida.
    Espera-se que a classe Vendas gere uma exceção ValidationError quando dados inválidos são fornecidos.
    """

    dados_invalidos = {
        'email' : 'comprador',
        'data' : 'não é uma data',
        'valor' : -100,
        'produto' : '',
        'quantidade': -1,
        'categoria': 'categoria3'
    }

    with pytest.raises(ValidationError):
        Vendas(**dados_invalidos)

def test_validacao_categoria():
    
    """"
    Testa a validação da categoria na criação de uma instância da classe Vendas.

    Este teste especificamente verifica se a classe Vendas valida a categoria do produto.
    Ele utiliza dados válidos para todos os campos, exceto pela categoria, que é definida como uma categoria inexistente.
    Espera-se que a classe Vendas gere uma exceção ValidationError devido à categoria inválida.

    args:
        dados = {
        email : comprador@example.com
        data : datetime.now()
        valor  : 100.50
        produto : Produto Y
        quantidade : 1
        categoria : categoria inexistente
        }
    """

    dados = {
        'email' : 'comprador@example.com',
        'data' : datetime.now(),
        'valor' : 100.50,
        'produto' : 'Produto Y',
        'quantidade' : 1,
        'categoria' : 493.50
    }

    with pytest.raises(ValidationError):
        Vendas(**dados)