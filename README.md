# Processos_de_dados

### Instalação e Configuração

1. Clone o repositório:
```bash
git clone https://github.com/MateusKasuya/Processos_de_dados.git
cd Processos_de_dados
```

2. Configure a versão correta do Python com `pyenv`:
```bash
pyenv install 3.11.5
pyenv local 3.11.5
```

3. Instale as depedências do projeto:
```bash
python -m venv .venv
# O padrão é utilizar .venv
source .venv/Scripts/activate
# Usuários Linux e Mac
.venv\Scripts\Activate
# Usuários Windows
pip install -r requirements.txt
```