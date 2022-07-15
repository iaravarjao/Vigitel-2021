# Vigitel-2021
:bar_chart: Análise de dados públicos do Ministério da Saúde

O Vigitel - Sistema de Vigilância de Fatores de Risco de Doenças Crônicas Não Transmissíveis (DCNT) do Ministério da Saúde, conjuntamente a outros inquéritos, como os domiciliares, vem ampliando o conhecimento sobre as DCNT no país. Com ele é possível monitorar os principais determinantes das DCNT no Brasil e, assim, apoiar a formulação de políticas públicas que promovam a melhoria da qualidade de vida da população brasileira.

A coleta de dados do Vigitel é realizada por entrevista telefônica, por telefone fixo, conduzida por uma empresa contratada especialmente para esse fim, e esta, realizada no ano de 2021. Esta edição foi recém publicada e está disponivel na URL http://plataforma.saude.gov.br/vigitel/ (acesso em julho/2022).

Os resultados dessa pesquisa subsidiam o monitoramento das metas propostas no Plano de Ações Estratégicas para o Enfrentamento das Doenças Crônicas Não Transmissíveis no Brasil 2011-2022, assim como embasam as metas do Plano de Ações Estratégicas para o Enfrentamento das Doenças Crônicas e Agravos não Transmissíveis no Brasil 2021-2030, o Plano Regional (ORGANIZAÇÃO PAN-AMERICANA DA SAÚDE, 2014), o Plano de Ação Global para a Prevenção e Controle das DCNT, da Organização Mundial da Saúde (WORLD HEALTH ORGANIZATION, 2013), bem como das metas de DCNT referentes à agenda 2030 dos Objetivos de Desenvolvimento Sustentável (UNITED NATIONS, 2015).

Separei somente os dados relacionados à ***hipertensão*** e trago as visualizações a seguir, que mostram maiores valores nas capitais do ***RJ***, ***PE*** e ***MG***, observando ainda, por região, que as ***mulheres*** são maioria entre os acometidos pela doença.

Apresento uma visualização desses dados com uso da biblioteca Streamlit, um framework de código aberto, onde é possível construir dashboards interativos de maneira simples. Para o desenvolvimento deste projeto, utilizei o editor de código Visual Studio Code.

- Criação de ambiente virtual e Instalação dos pacotes necessários
```
python -m venv venv
venv\Scripts\activate
```
```
pip install pandas
pip install streamlit
```
- Rodar o arquivo para visualização do painel
```
streamlit run main.py
```
