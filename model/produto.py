from sqlalchemy import Column, String, Integer, DateTime, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from  model import Base, Comentario

class Produto(Base):
    __tablename__ = 'produto'

    id = Column("pk_produto", Integer, primary_key=True)
    nome = Column(String(140), unique=True)
    size = Column(String(140), unique=True)
    quantity = Column(Integer)
    data_insercao = Column(DateTime, default=datetime.now())
    # Definição do relacionamento entre o produto e o comentário.
    comentarios = relationship("Comentario")

    def __init__(self, nome:str, size:str, quantity:int,
                 data_insercao:Union[DateTime, None] = None):
        """
        Cria um Produto

        Arguments:
            name: nome do produto.
            quantidade: quantidade que se espera comprar daquele produto
            valor: valor esperado para o produto
            data_insercao: data de quando o produto foi inserido à base
        """
        self.nome = nome
        self.size = size
        self.quantity = quantity

        # se não for informada, será o data exata da inserção no banco
        if data_insercao:
            self.data_insercao = data_insercao

    def adiciona_comentario(self, comentario:Comentario):
        """ Adiciona um novo comentário ao Produto
        """
        self.comentarios.append(comentario)

