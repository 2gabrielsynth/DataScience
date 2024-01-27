import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import locale
from datetime import datetime, timedelta
from PIL import Image

def default_moeda_brasil():

    locale.setlocale(locale.LC_ALL, 'pt_BR')

def main_page():

    imagem1 = Image.open("logo3.png")
    largura_desejada = 800
    altura_desejada = 449
    imagem1_redimensionada = imagem1.resize((largura_desejada, altura_desejada))

    data_hoje = datetime.now()
    data_ontem = data_hoje - timedelta(days=1)
    data_ontem = data_ontem.strftime("%d/%m")


    #def verificar_login():


    def Perdas_Mercadeli():
            qtde_dias = st.selectbox("Maior - Menor", ["97D"])
            num_dias = int(qtde_dias.replace("D", ""))
            path = 'dezPerdas23.csv'
            dados = pd.read_csv(path, encoding='latin1', delimiter=';')
            dados['Valor'] = dados['Valor'].str.replace(',', '.').astype(float)
            num_linhas = len(dados['Cliente'])
            #print(num_linhas)
            dados_reunidos = dados.groupby('Cliente')['Valor'].sum().reset_index()
            dados_reunidos[-num_dias:]
            st.bar_chart(dados_reunidos, x="Cliente", y="Valor", color = "#bd2f3c")

            soma = dados_reunidos['Valor'].sum()
            print(soma)
            
            default_moeda_brasil()
            st.write(locale.currency(soma, grouping=True))

            
    
    
    def Vendas_Mercadeli_Varejo():
            qtde_dias = st.selectbox("Maior - Menor", ["97D"])
            num_dias = int(qtde_dias.replace("D", ""))
            path = 'dezVendasVar23.csv'
            dados = pd.read_csv(path, encoding='latin1', delimiter=';')
            dados['Valor'] = dados['Valor'].str.replace(',', '.').astype(float)
            num_linhas = len(dados['Cliente'])
            #print(num_linhas)
            dados_reunidos = dados.groupby('Cliente')['Valor'].sum().reset_index()
            dados_reunidos[-num_dias:]
            st.bar_chart(dados_reunidos, x="Cliente", y="Valor", color = "#bd2f3c")

            soma = dados_reunidos['Valor'].sum()
            print(soma)
            
            default_moeda_brasil()
            st.write(locale.currency(soma, grouping=True))
    
    def Vendas_Mercadeli_Caixa():
            qtde_dias = st.selectbox("Maior - Menor", ["97D"])
            num_dias = int(qtde_dias.replace("D", ""))
            path = 'dezCupom23.csv'
            dados = pd.read_csv(path, encoding='latin1', delimiter=';')
            dados['Valor Bruto'] = dados['Valor Bruto'].str.replace(',', '.').astype(float)
            num_linhas = len(dados['Operador'])
            #print(num_linhas)
            dados_reunidos = dados.groupby('Operador')['Valor Bruto'].sum().reset_index()
            dados_reunidos[-num_dias:]
            st.bar_chart(dados_reunidos, x="Operador", y="Valor Bruto", color = "#bd2f3c")

            soma = dados_reunidos['Valor Bruto'].sum()
            print(soma)
            
            default_moeda_brasil()
            st.write(locale.currency(soma, grouping=True))
    
    
    

    def valor_fornecedores():
        qtde_dias = st.selectbox("Maior - Menor", ["97D"])
        num_dias = int(qtde_dias.replace("D", ""))
        path = 'dezTotais23.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)
        num_linhas = len(dados['Nome do Fornecedor'])
        #print(num_linhas)
        dados_reunidos = dados.groupby('Nome do Fornecedor')['Valor Total'].sum().reset_index()
        dados_reunidos[-num_dias:]
        st.bar_chart(dados_reunidos, x="Nome do Fornecedor", y="Valor Total", color = "#bd2f3c")

        soma = dados_reunidos['Valor Total'].sum()
        print(soma)
        
        default_moeda_brasil()
        st.write(locale.currency(soma, grouping=True))
    
    
   
    
    def Compras_Açougue():
        qtde_dias = st.selectbox("Maior - Menor", ["15 Fornecedores"])
        num_dias = int(qtde_dias.replace("Fornecedores", ""))
        path = 'dezAçouge23.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)
        num_linhas = len(dados['Nome do Fornecedor'])
        #print(num_linhas)
        dados_reunidos = dados.groupby('Nome do Fornecedor')['Valor Total'].sum().reset_index()
        dados_reunidos[-num_dias:]
        st.bar_chart(dados_reunidos, x="Nome do Fornecedor", y="Valor Total", color = "#bd2f3c")

        soma = dados_reunidos['Valor Total'].sum()
        print(soma)
        
        default_moeda_brasil()
        st.write(locale.currency(soma, grouping=True))

    
    
    
    def Compras_Adega():
        qtde_dias = st.selectbox("Maior - Menor", ["15 Fornecedores"])
        num_dias = int(qtde_dias.replace("Fornecedores", ""))
        path = 'dezAdega23.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)
        num_linhas = len(dados['Nome do Fornecedor'])
        #print(num_linhas)
        dados_reunidos = dados.groupby('Nome do Fornecedor')['Valor Total'].sum().reset_index()
        dados_reunidos[-num_dias:]
        st.bar_chart(dados_reunidos, x="Nome do Fornecedor", y="Valor Total", color = "#bd2f3c")

        soma = dados_reunidos['Valor Total'].sum()
        print(soma)
        
        default_moeda_brasil()
        st.write(locale.currency(soma, grouping=True))

    
    
    def Compras_Congelados():
        qtde_dias = st.selectbox("Maior - Menor", ["15 Fornecedores"])
        num_dias = int(qtde_dias.replace("Fornecedores", ""))
        path = 'dezCongelados23.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)
        num_linhas = len(dados['Nome do Fornecedor'])
        #print(num_linhas)
        dados_reunidos = dados.groupby('Nome do Fornecedor')['Valor Total'].sum().reset_index()
        dados_reunidos[-num_dias:]
        st.bar_chart(dados_reunidos, x="Nome do Fornecedor", y="Valor Total", color = "#bd2f3c")

        soma = dados_reunidos['Valor Total'].sum()
        print(soma)
        
        default_moeda_brasil()
        st.write(locale.currency(soma, grouping=True))

    
    
    
    
    
    def Compras_Frios():
        qtde_dias = st.selectbox("Maior - Menor", ["15 Fornecedores"])
        num_dias = int(qtde_dias.replace("Fornecedores", ""))
        path = 'dezFrios23.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)
        num_linhas = len(dados['Nome do Fornecedor'])
        #print(num_linhas)
        dados_reunidos = dados.groupby('Nome do Fornecedor')['Valor Total'].sum().reset_index()
        dados_reunidos[-num_dias:]
        st.bar_chart(dados_reunidos, x="Nome do Fornecedor", y="Valor Total", color = "#bd2f3c")

        soma = dados_reunidos['Valor Total'].sum()
        print(soma)
        
        default_moeda_brasil()
        st.write(locale.currency(soma, grouping=True))

    
    
    
    
    def Compras_Mercearia():
        qtde_dias = st.selectbox("Maior - Menor", ["15 Fornecedores"])
        num_dias = int(qtde_dias.replace("Fornecedores", ""))
        path = 'dezMercearia23.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)
        num_linhas = len(dados['Nome do Fornecedor'])
        #print(num_linhas)
        dados_reunidos = dados.groupby('Nome do Fornecedor')['Valor Total'].sum().reset_index()
        dados_reunidos[-num_dias:]
        st.bar_chart(dados_reunidos, x="Nome do Fornecedor", y="Valor Total", color = "#bd2f3c")

        soma = dados_reunidos['Valor Total'].sum()
        print(soma)
        
        default_moeda_brasil()
        st.write(locale.currency(soma, grouping=True))

    
    def Compras_Bebidas():
        qtde_dias = st.selectbox("Maior - Menor", ["15 Fornecedores"])
        num_dias = int(qtde_dias.replace("Fornecedores", ""))
        path = 'dezBebidas23.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)
        num_linhas = len(dados['Nome do Fornecedor'])
        #print(num_linhas)
        dados_reunidos = dados.groupby('Nome do Fornecedor')['Valor Total'].sum().reset_index()
        dados_reunidos[-num_dias:]
        st.bar_chart(dados_reunidos, x="Nome do Fornecedor", y="Valor Total", color = "#bd2f3c")

        soma = dados_reunidos['Valor Total'].sum()
        print(soma)
        
        default_moeda_brasil()
        st.write(locale.currency(soma, grouping=True))

    
    def Compras_Padaria():
        qtde_dias = st.selectbox("Maior - Menor", ["15 Fornecedores"])
        num_dias = int(qtde_dias.replace("Fornecedores", ""))
        path = 'dezPadaria23.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)
        num_linhas = len(dados['Nome do Fornecedor'])
        #print(num_linhas)
        dados_reunidos = dados.groupby('Nome do Fornecedor')['Valor Total'].sum().reset_index()
        dados_reunidos[-num_dias:]
        st.bar_chart(dados_reunidos, x="Nome do Fornecedor", y="Valor Total", color = "#bd2f3c")

        soma = dados_reunidos['Valor Total'].sum()
        print(soma)
        
        default_moeda_brasil()
        st.write(locale.currency(soma, grouping=True))

    
    def Compras_Interno():
        qtde_dias = st.selectbox("Maior - Menor", ["15 Fornecedores"])
        num_dias = int(qtde_dias.replace("Fornecedores", ""))
        path = 'dezInterno23.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Valor Total'] = dados['Valor Total'].str.replace(',', '.').astype(float)
        num_linhas = len(dados['Nome do Fornecedor'])
        #print(num_linhas)
        dados_reunidos = dados.groupby('Nome do Fornecedor')['Valor Total'].sum().reset_index()
        dados_reunidos[-num_dias:]
        st.bar_chart(dados_reunidos, x="Nome do Fornecedor", y="Valor Total", color = "#bd2f3c")

        soma = dados_reunidos['Valor Total'].sum()
        print(soma)
        
        default_moeda_brasil()
        st.write(locale.currency(soma, grouping=True))

    
    
    
    
    def Faturamento_dia():
        path = 'teste_fatura.xls'
        dados = pd.read_excel(path)
        #print(dados)

    def operadoras_sacola():
        path = 'sacola.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Qtd. Itens'] = dados['Qtd. Itens'].astype(str)
        dados['Qtd. Itens'] = dados['Qtd. Itens'].str.replace(',', '.').astype(float)
        
        dados_reunidos = dados.groupby('Operador')['Qtd. Itens'].sum().reset_index()

        fig, ax = plt.subplots()
        ax.bar(dados_reunidos['Operador'], dados_reunidos['Qtd. Itens'])
        plt.xticks(rotation=45, ha='right')
        fig.patch.set_facecolor('#0F1117')
        ax.patch.set_visible(False)
        ax.tick_params(axis='y', colors='tomato')
        ax.tick_params(axis='x', colors='tomato')

        fig.patch.set_edgecolor('yellow')
        st.pyplot(fig)

        st.write(dados_reunidos)

    def venda_hortifruti():
        path = 'adega_vendas_jan.csv'
        dados = pd.read_csv(path, encoding='latin1', delimiter=';')
        dados['Faturamento'] = dados['Faturamento'].str.replace(',', '.').astype(float)
        dados_reunidos = dados.groupby('Descrição')['Faturamento'].sum().reset_index()
        st.bar_chart(dados_reunidos, x="Descrição", y="Faturamento", color = "#bd2f3c")

        soma = dados_reunidos['Faturamento'].sum()
        default_moeda_brasil()
        st.write(locale.currency(soma, grouping=True))
        
        soma = round(soma, 2)
        st.write(f"O valor de venda do Hortifruti é {locale.currency(soma, grouping=True)}")

    # Título do aplicativo
    with st.container():
        #st.subheader("""Primeiro site com Streamlit""")
        st.markdown("<h1 style='text-align: center; color: #b42e53;'>Resultados Mercadeli:</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: #b42e53;'>Controle T.I</h1>", unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: 'black';'>Gabriel Machado</h1>", unsafe_allow_html=True)

        st.image(imagem1_redimensionada, caption='', use_column_width=True)
        
        #st.title("Resultados Mercadeli")
        st.write("Informações sobre movimentos ao longo do mês de Dezembro")
        st.write("Link da Nuvem: [Clique aqui](https://grupojrd.varejofacil.com/app/#/login)")

    

    with st.container():
         st.write("____________________________")
         imagem2 = Image.open("vrj.png")
         largura_desejada = 800
         altura_desejada = 600
         imagem2_redimensionada = imagem2.resize((largura_desejada, altura_desejada))
         st.image(imagem2_redimensionada, caption="", use_column_width=True)

    st.markdown("<h1 style='text-align: center; color: #b42e53;'>Perdas:</h1>", unsafe_allow_html=True)

    with st.container():
            st.write("---")
            Perdas_Mercado = st.button("Perdas Mercadeli")
            if Perdas_Mercado:
                Perdas_Mercadeli()
    
    st.markdown("<h1 style='text-align: center; color: #b42e53;'>Vendas:</h1>", unsafe_allow_html=True)

    with st.container():
            st.write("---")
            Vendas_Varejo = st.button("Vendas_Varejo")
            if Vendas_Varejo:
                Vendas_Mercadeli_Varejo()

    with st.container():
            st.write("---")
            Vendas_PDV = st.button("Vendas PDV")
            if Vendas_PDV:
                Vendas_Mercadeli_Caixa()
    
   
    st.markdown("<h1 style='text-align: center; color: #b42e53;'>Compras:</h1>", unsafe_allow_html=True)

    
    with st.container():
        st.write("---")
        button_compras_açougue = st.button("Compras Açougue")
        if button_compras_açougue:
            Compras_Açougue()


    with st.container():
        st.write("---")
        button_compras_adega = st.button("Compras Adega")
        if button_compras_adega:
            Compras_Adega()


    with st.container():
        st.write("---")
        button_compras_congelados = st.button("Compras Congelados")
        if button_compras_congelados:
            Compras_Congelados()


    with st.container():
        st.write("---")
        button_compras_frios = st.button("Compras Frios")
        if button_compras_frios:
            Compras_Frios()


    with st.container():
        st.write("---")
        button_compras_mercearia = st.button("Compras Mercearia")
        if button_compras_mercearia:
            Compras_Mercearia()

    with st.container():
        st.write("---")
        button_compras_bebidas = st.button("Compras Bebidas")
        if button_compras_bebidas:
            Compras_Bebidas()

    with st.container():
        st.write("---")
        button_compras_padaria = st.button("Compras Padaria")
        if button_compras_padaria:
            Compras_Padaria()

    with st.container():
        st.write("---")
        button_compras_interno = st.button("Compras Interno")
        if button_compras_interno:
            Compras_Interno()




            
                
        
    
    
    
    
    
    with st.container():
        st.write("---")
        Compra_geral_button = st.button("""Totais 
                            Fornecedores""")
        if Compra_geral_button:
            valor_fornecedores()


    st.markdown("<h1 style='text-align: center; color: #b42e53;'>Falhas de Procedimento:</h1>", unsafe_allow_html=True)

    with st.container():
        st.write("---")
        Infração_button = st.button('Infração')
        if Infração_button:
            operadoras_sacola()

    st.markdown("<h1 style='text-align: center; color: #b42e53;'>Vendas por Seção::</h1>", unsafe_allow_html=True)


    with st.container():
        st.write("---")
        button_hort = st.button('Venda Hortifruti')
        if button_hort:
            venda_hortifruti()

main_page()
