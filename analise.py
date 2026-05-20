import os
import time
import json
from random import random
from datetime import datetime
from sys import argv

import requests
import pandas as pd
import seaborn as sns


URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'


# Extração dos dados
try:
    response = requests.get(url=URL)
    response.raise_for_status()
except requests.HTTPError:
    print('Dado não encontrado, continuando.')
    cdi = None
except Exception as exc:
    print('Erro, parando a execução.')
    raise exc
else:
    dado = json.loads(response.text)[-1]['valor']


for _ in range(10):
    data_e_hora = datetime.now()

    data = datetime.strftime(data_e_hora, '%Y/%m/%d')
    hora = datetime.strftime(data_e_hora, '%H:%M:%S')
    cdi = float(dado) + (random() - 0.5)

    if not os.path.exists('./taxa-cdi.csv'):
        with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
            fp.write('data,hora,taxa\n')

    with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
        fp.write(f'{data},{hora},{cdi}\n')

    time.sleep(1)


# Visualização dos dados
df = pd.read_csv('./taxa-cdi.csv')

grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
grafico.set_xticklabels(labels=df['hora'], rotation=90)

grafico.get_figure().savefig(f'{argv[1]}.png')

print('Sucesso')