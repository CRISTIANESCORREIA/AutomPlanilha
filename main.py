import pandas as pd
from twilio.rest import Client

account_sid ="ACc04170f0665159bec3e04499f9b64838"
auth_token ="a690bd1d1674aae7429c8ba325749a19"
client = Client(account_sid, auth_token)

lista_mesesDeVendas = ['janeiro', 'fevereiro', 'março', 'abril', 'maio']
#para ler um arquivo em excell
for mes in lista_mesesDeVendas:
    # print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #print(tabela_vendas)
    if (tabela_vendas['Vendas'] > 55000).any():
        Vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        Vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês {mes} alguém bateu a meta. Vendedor: {Vendedor}, Vendas:{Vendas}')
        message = client.messages.create(
            to='+5551982613359',  # meu numero de celular cadastrado
            from_='+12542563503',  # numero do telefone twilio
            body=f'No mês {mes} alguém bateu a meta. Vendedor: {Vendedor}, Vendas:{Vendas}')
        print(message.sid)











