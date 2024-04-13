from pydantic import BaseModel
from datetime import datetime

class Vendas(BaseModel):
    email : str
    data : datetime
    valor : float
    produto : str
    quantidade : int
    categoria : str