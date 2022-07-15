import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from PIL import Image


st.title("Painel de Saúde da População")
st.header("Hipertensão")
st.sidebar.title("Menu")
selecionada = st.sidebar.selectbox("Escolha uma pesquisa:",
                               ("Vigitel, 2021", "IBGE, 2020"))

if  selecionada == "Vigitel, 2021":
    st.subheader("Análise de dados do Ministério da Saúde")
    st.markdown(" O Vigitel - Sistema de Vigilância de Fatores de Risco de Doenças Crônicas \
Não Transmissíveis (DCNT) do Ministério da Saúde, conjuntamente a outros inquéritos, como os \
domiciliares, vem ampliando o conhecimento sobre as DCNT no país. \
Com ele é possível monitorar os principais determinantes das DCNT no Brasil e, \
assim, apoiar a formulação de políticas públicas que promovam a melhoria da qualidade de \
vida da população brasileira.\
\n\n A coleta de dados do Vigitel é realizada por entrevista telefônica, por telefone fixo, \
conduzida por uma empresa contratada especialmente para esse fim, e esta, realizada no ano de 2021. \
Esta edição foi recém publicada e está disponivel na URL http://plataforma.saude.gov.br/vigitel/ \
(acesso em julho/2022). \
\n\n Os resultados dessa pesquisa subsidiam o monitoramento das metas propostas no Plano de Ações \
Estratégicas para o Enfrentamento das Doenças Crônicas Não Transmissíveis no Brasil 2011-2022, \
assim como embasam as metas do Plano de Ações Estratégicas para o Enfrentamento \
das Doenças Crônicas e Agravos não Transmissíveis no Brasil 2021-2030, o Plano \
Regional (ORGANIZAÇÃO PAN-AMERICANA DA SAÚDE, 2014), o Plano de Ação Global para a Prevenção \
e Controle das DCNT, da Organização Mundial da Saúde (WORLD HEALTH ORGANIZATION, 2013), \
bem como das metas de DCNT referentes à agenda 2030 dos Objetivos de Desenvolvimento Sustentável \
(UNITED NATIONS, 2015).\
\n\n Separei somente os dados relacionados à **hipertensão** e trago as visualizações a seguir, \
que mostram maiores valores nas capitais do RJ, PE e MG, observando ainda, \
por região, que as **mulheres** são maioria entre os acometidos pela doença." )
    
    vigitel = pd.read_csv("vigitel_hipertensao.csv", delimiter=",")
    dados = vigitel[["Capitais", "total", "masculino", "feminino"]]

    sul = dados[dados.index.isin([6,7,16])]
    sudeste = dados[dados.index.isin([2,20,23,25])]
    norte = dados[dados.index.isin([1,3,11,13,15,17,19])]
    nordeste = dados[dados.index.isin([0,8,10,12,14,18,21,22,24])]
    centro_oeste = dados[dados.index.isin([4,5,9,26])]
    
    dados.plot(kind='bar', x= 'Capitais', y='total', title='Total Geral', color='darkblue')
    plt.ylabel('Valor percentual')
    st.pyplot(plt)
    st.caption('Secretaria de Vigilância em Saúde, MS, Vigitel, 2021')

    st.subheader("Subdivisão por região")
    st.markdown("Percentual de adultos (≥18 anos) que referiram diagnóstico\
    médico de hipertensão arterial, por sexo")

    regiao = st.radio(
     "Selecione uma região:",
     ('Norte', 'Nordeste', 'Sul', 'Sudeste'))

    if regiao == 'Norte':
        norte.plot(kind='barh', x= 'Capitais', y= ['feminino','masculino'], 
    title= "Região Norte", color=['blue', 'lightsteelblue'])
        plt.xlabel('Valor percentual')
        st.pyplot(plt)
        st.caption('Secretaria de Vigilância em Saúde, MS, Vigitel, 2021')
        
    elif regiao == 'Nordeste':
        nordeste.plot(kind='barh', x= 'Capitais', y= ['feminino','masculino'], 
    title= "Região Nordeste", color=['green', 'lightgreen'])
        plt.xlabel('Valor percentual')
        st.pyplot(plt)
        st.caption('Secretaria de Vigilância em Saúde, MS, Vigitel, 2021')
        
    elif regiao == 'Sul':
        sul.plot(kind='barh', x= 'Capitais', y= ['feminino','masculino'], 
    title= "Região Sul", color=['purple', 'violet'])
        plt.xlabel('Valor percentual')
        st.pyplot(plt)
        st.caption('Secretaria de Vigilância em Saúde, MS, Vigitel, 2021')
        
    elif regiao == 'Sudeste':
        sudeste.plot(kind='barh', x= 'Capitais', y= ['feminino','masculino'], 
    title= "Região Sudeste", color=['crimson', 'salmon'])
        st.caption('Secretaria de Vigilância em Saúde, MS, Vigitel, 2021')
        st.pyplot(plt)
        plt.xlabel('Valor percentual')
        
elif selecionada == "IBGE, 2020":
    st.subheader("Análise de dados do IBGE")
    st.markdown("A Pesquisa Nacional de Saúde - PNS alerta sobre as condições de saúde \
        da população brasileira em relação à doenças crônicas \
        não transmissíveis (DCNT) e acesso a planos de saúde médicos. Os dados apresentados\
        são de pessoas de 18 anos ou mais de idade com pelo menos um diagnóstico médico de DCNT,\
        com período de referência de 01/01/2019 a 31/12/2019 e foi publicada em 2020 (disponível\
        em URL https://sidra.ibge.gov.br/pesquisa/pns, acesso em jun/2022).\
        \n\n   Este relatório abaixo foi feito no PowerBI desktop e nele mostro, em porcentagem, gráficos relacionados \
        à **hipertensão** ou pressão alta, a principal doença autorreferida pela população pesquisada. Assim,\
        é possível visualizar o perfil de pessoas mais acometidas pela doença (**mulheres, pessoas sem instrução\
        ou com ensino fundamental incompleto, sem plano de saúde, em situação domiciliar urbana e de cor \
        ou raça pretas ou pardas**) e contribui para a compreensão dos perfis demográfico e social \
        da população, possibilitando o monitoramento de políticas públicas e o planejamento de ações \
        para redução dos impactos que a doença causa.")
    image = Image.open('report_pns.png')
    st.image(image, caption= 'Fonte: IBGE, Diretoria de Pesquisas, Coordenação de Trabalho e Rendimento, \
        Pesquisa Nacional de Saúde, 2019.')
