# Fome Zero — Análise Estratégica de Restaurantes

## 1. Problema de Negócio

A empresa Fome Zero é uma marketplace de restaurantes. Ou seja, seu core
business é facilitar o encontro e negociações de clientes e restaurantes. Os
restaurantes fazem o cadastro dentro da plataforma da Fome Zero, que disponibiliza
informações como endereço, tipo de culinária servida, se possui reservas, se faz
entregas e também uma nota de avaliação dos serviços e produtos do restaurante, dentre outras informações.
O CEO Guerra também foi recém contratado e precisa entender melhor o negócio
para conseguir tomar as melhores decisões estratégicas e alavancar ainda mais a
Fome Zero, e para isso, ele precisa que seja feita uma análise nos dados da
empresa e que sejam gerados dashboards, a partir dessas análises, para responder
às seguintes perguntas:

---

## 2. Premissas do Negócio

### Geral
1. Quantos restaurantes únicos estão registrados?
2. Quantos países únicos estão registrados?
3. Quantas cidades únicas estão registradas?
4. Qual o total de avaliações feitas?
5. Qual o total de tipos de culinária registrados?
---
### Pais
1. Qual o nome do país que possui mais cidades registradas?
2. Qual o nome do país que possui mais restaurantes registrados?
3. Qual o nome do país que possui mais restaurantes com o nível de preço igual a 4 registrados?
4. Qual o nome do país que possui a maior quantidade de tipos de culinária distintos?
5. Qual o nome do país que possui a maior quantidade de avaliações feitas?
6. Qual o nome do país que possui a maior quantidade de restaurantes que fazem entrega?
7. Qual o nome do país que possui a maior quantidade de restaurantes que aceitam reservas?
8. Qual o nome do país que possui, na média, a maior quantidade de avaliações registrada?
9. Qual o nome do país que possui, na média, a maior nota média registrada?
10. Qual o nome do país que possui, na média, a menor nota média registrada?
11. Qual a média de preço de um prato para dois por país?
---
### Cidade
1. Qual o nome da cidade que possui mais restaurantes registrados?
2. Qual o nome da cidade que possui mais restaurantes com nota média acima de 4?
3. Qual o nome da cidade que possui mais restaurantes com nota média abaixo de 2.5?
4. Qual o nome da cidade que possui o maior valor médio de um prato para dois?
5. Qual o nome da cidade que possui a maior quantidade de tipos de culinária distintas?
6. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem reservas?
7. Qual o nome da cidade que possui a maior quantidade de restaurantes que fazem entregas?
8. Qual o nome da cidade que possui a maior quantidade de restaurantes que aceitam pedidos online?
---
### Restaurantes
1. Qual o nome do restaurante que possui a maior quantidade de avaliações?
2. Qual o nome do restaurante com a maior nota média?
3. Qual o nome do restaurante que possui o maior valor de uma prato para duas pessoas?
4. Qual o nome do restaurante de tipo de culinária brasileira que possui a menor média de avaliação?
5. Qual o nome do restaurante de tipo de culinária brasileira, e que é do Brasil, que possui a maior média de avaliação?
6. Os restaurantes que aceitam pedido online são também, na média, os restaurantes que mais possuem avaliações registradas?
7. Os restaurantes que fazem reservas são também, na média, os restaurantes que possuem o maior valor médio de um prato para duas pessoas?
8. Os restaurantes do tipo de culinária japonesa dos Estados Unidos da América possuem um valor médio de prato para duas pessoas maior que as churrascarias americanas (BBQ)?
---
### Tipos de Culinária
1. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a maior média de avaliação?
2. Dos restaurantes que possuem o tipo de culinária italiana, qual o nome do restaurante com a menor média de avaliação?
3. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a maior média de avaliação?
4. Dos restaurantes que possuem o tipo de culinária americana, qual o nome do restaurante com a menor média de avaliação?
5. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a maior média de avaliação?
6. Dos restaurantes que possuem o tipo de culinária árabe, qual o nome do restaurante com a menor média de avaliação?
7. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a maior média de avaliação?
8. Dos restaurantes que possuem o tipo de culinária japonesa, qual o nome do restaurante com a menor média de avaliação?
9. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a maior média de avaliação?
10. Dos restaurantes que possuem o tipo de culinária caseira, qual o nome do restaurante com a menor média de avaliação?
11. Qual o tipo de culinária que possui o maior valor médio de um prato para duas pessoas?
12. Qual o tipo de culinária que possui a maior nota média?
13. Qual o tipo de culinária que possui mais restaurantes que aceitam pedidos online e fazem entregas?


---

## 3. Estratégia da Solução

### Coleta e tratamento

- Renomeação e padronização de colunas;
- Tratamento de valores nulos;
- Conversão de tipos de dados;
- Tradução de informações auxiliares;
- Criação de colunas derivadas;
- Padronização de nomes e categorias.

### Exploração e análise

- Agrupamentos com Pandas;
- Métricas estatísticas;
- Filtros e segmentações;
- Comparações entre categorias;
- Identificação de padrões e tendências.

### Construção do dashboard

- Filtrar por país e culinária;
- Navegar entre diferentes perspectivas do negócio;
- Visualizar indicadores estratégicos;
- Explorar gráficos dinâmicos.

---

## 4. Principais Insights de Dados

### Insight 1

A Indonésia apresentou a maior média de avaliações por restaurante entre todos os países analisados, mesmo possuindo uma das menores quantidades de restaurantes cadastrados e estando presente em apenas três cidades.
Esse resultado pode indicar um alto nível de engajamento dos clientes e uma forte concentração de demanda nos restaurantes da região.

---

### Insight 2

O Brasil aparece entre os países com maior presença de restaurantes com avaliações baixas no dataset, com destaque para:

- São Paulo: 16 restaurantes
- Brasília: 15 restaurantes
- Rio de Janeiro: 12 restaurantes

Ao mesmo tempo, São Paulo também aparece entre as 10 cidades com maior diversidade de culinárias, e o Brasil conta com 3 das 10 culinárias mais bem avaliadas da base.

  
O mercado brasileiro demonstra grande diversidade gastronômica e potencial competitivo, mas também apresenta oportunidades claras de melhoria na experiência dos clientes.

---

### Insight 3

A Índia lidera o dataset em volume de restaurantes cadastrados e cidades presentes, além de concentrar alguns dos restaurantes mais antigos e com melhores avaliações da plataforma.
O país representa o mercado mais relevante da base analisada e pode ser considerado estratégico para decisões de crescimento e priorização comercial.

---

### Insight 4

Restaurantes que aceitam pedidos online apresentam, em média, quase o dobro de avaliações quando comparados aos que não utilizam esse canal.

- Pedidos online: média de **838,8** avaliações
- Sem pedidos online: média de **478,3** avaliações

Isso demonstra que existe um maior engajamento dos clientes e a geração de mais interações dentro da plataforma.
  
---

## 5. Produto Final do Projeto

O resultado do projeto foi a construção de um dashboard analítico interativo com Streamlit.
Acesse no link: 

https://fome-zero-dashboard.streamlit.app/

---

## 6. Conclusão

A análise dos dados da Fome Zero permitiu transformar informações operacionais em indicadores estratégicos capazes de apoiar a tomada de decisão do negócio.

Com o desenvolvimento do dashboard foi possível identificar padrões relevantes entre países, cidades, restaurantes e tipos de culinária, além de entender melhor o comportamento dos usuários dentro da plataforma, como a relação entre pedidos online e engajamento nas avaliações.
