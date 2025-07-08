## Avaliação de Adequação Funcional - Observações

### M1 - Cobertura de Implementação Funcional
**Valor Atual: 60% | Meta: ≥85% | Status: ⚠️ Abaixo da meta**

- **(F1) Cadastro**: não há opção de cadastro na plataforma web.

<center>
<img src="../../assets/sem_cadastro.png" alt="Tela de login inicial | Web" width="800"/>
</center>
<center>
<b>Figura 1</b>: Tela de Inicial
</center>
<br>

- **(F2) Login**: há várias formas de login, seja no aplicativo ou na CSA.
<center>
<img src="../../assets/profile.jpeg" alt="Tela de Perfil | Sem CSA" width="300"/>
</center>
<center>
<b>Figura 2</b>: Tela de Perfil | Sem CSA
</center>
<br>
<center>
<img src="../../assets/login_csa.jpeg" alt="Tela de Login em CSA" width="300"/>
</center>
<center>
<b>Figura 3</b>: Tela de Login em CSA
</center>
<br>

- **(F3) Instalação**:
    - Não há aplicativo publicado em lojas oficiais (Google Play, App Store).  
    - Não existe um APK pronto para download direto.
    - No docs do Agromar, a [página de instalação](https://agromart.github.io/docs/docs/instalacao/instalacao) está vazia.
    - O tutorial de parte do deploy encontra-se armazenado em um repositório separado das aplicações ([Ajuda AgroMart](https://github.com/AgroMart/ajuda-agromart)).
    - O tutorial pede que o usuário insira o cartão de crédito na plataforma Heroku, o que tem potencial de afastar futuros contribuídores de realizar deploy na aplicação.

- **(F4) Uso**:

<center>
<img src="../../assets/profile_home.jpeg" alt="Tela de Perfil | Principal" width="300"/>
</center>
<center>
<b>Figura 4</b>: Tela de Perfil | Principal
</center>
<br>
<center>
<img src="../../assets/profile_configs.jpeg" alt="Tela de Perfil | Configurações" width="300"/>
</center>
<center>
<b>Figura 5</b>: Tela de Perfil | Configurações
</center>
<br>
<center>
<img src="../../assets/csa.jpeg" alt="Tela de Busca" width="300"/>
</center>
<center>
<b>Figura 6</b>: Tela de Busca
</center>
<br>
<center>
<img src="../../assets/historico.jpeg" alt="Historico" width="300"/>
</center>
<center>
<b>Figura 7</b>: Historico
</center>
<br>
<center>
<img src="../../assets/pedidos.jpeg" alt="Tela de Pedido" width="300"/>
</center>
<center>
<b>Figura 8</b>: Tela de Pedido
</center>
<br>

- **(F5) Compra**: não foi possível verificar as operações de compra em funcionamento, considerando que apenas as telas estáticas foram fornecidas.  

<center>
<img src="../../assets/compra.jpeg" alt="Tela de Compra" width="300"/>
</center>
<center>
<b>Figura 9</b>: Tela de Compra
</center>

Das 5 funcionalidades, 3 foram encontradas, resultando em **60% para a M1**.

#### Proposta de melhoria para M1:
- **Criar ambiente de teste funcional** para validar todas as funcionalidades
- **Publicar aplicativo nas lojas oficiais** (Google Play e App Store)
- **Gerar APK de demonstração** para testes diretos

### M2 - Precisão Computacional
**Valor Atual: 0% | Meta: =100% | Status: 🔴 Crítico**

A integração entre frontend e backend está com problemas. A cada instante em que tentávamos usar o produto (com a integração), o erro ocorria.

Logo a precisão computacional é de 1 erro a cada instante.

O que é claramente equivalente a 0% do esperado.

### M3 - Apropriação Funcional
**Valor Atual: 100% | Meta: ≥85% | Status: ✅ Atingido**

Durante a instalação, erros foram encontrados na integração do frontend web e mobile e backend.

Mesmo lendo a documentação e pedindo ajuda externa, no final, não foi possível executar o produto com exatidão.

Olhando para esses elementos como conjuntos de funções, temos:

* Frontend web preciso.
* Frontend mobile preciso.
* Backend preciso.
* Integração imprecisa

A precisão computacional portanto chega a um 4/1, o que pode ser considerado 100%.


## Avaliação de Usabilidade

### M4 - Clareza das Mensagens
**Valor Atual: 9,09% | Meta: ≥85% | Status: 🔴 Crítico**

* 1) As descrições dos menus apresentam uma fonte com cor muito clara, dificultando a leitura em alguns dispositivos.

<center><p>Fonte clara</p></center>
<center>
<img src="../../assets/tela-com-texto-ruim.jpeg" alt="Fonte clara" width="300"/>
</center>
<center>
<b>Figura 10</b>: Tela sem login
</center>



<!-- ### M8 - Descoberta de Carrossel
**Valor Atual: 25% | Meta: ≥85% | Status: 🔴 Crítico**-->
<br>

* 2) Na tela inicial há um carrossel de imagens, porém os indicadores visuais que evidenciam tratar-se de um carrossel são difíceis de perceber, pois as três bolinhas estão quase imperceptíveis devido à sua cor. O usuário precisa arrastar manualmente para descobrir outras imagens, o que pode gerar confusão.

<center><p>Carrosel</p></center>
<center>
<img src="../../assets/carrossel.jpeg" alt="Carrossel" width="300"/>
</center>
<center>
<b>Figura 11</b>: Tela inicial do aplicativo mostrando o carrossel.
</center>

<!-- ### M12 - Compreensão CSA
**Valor Atual: 85% | Meta: ≥80% | Status: ✅ Atingido**
 -->
 <br>

* 3) A tela de busca de CSA (Figura 6) está bem estruturada, apresentando imagens de pontos específicos de cada região administrativa, acompanhadas do respectivo nome, o que facilita a compreensão.

<!-- ### M9 - Compreensão de Nomenclatura
**Valor Atual: 55% | Meta: ≥95% | Status: 🔴 Crítico** -->

* 4) Alguns termos do aplicativo estão apresentados em inglês (por exemplo, *History*), o que pode dificultar o entendimento do público-alvo, que é composto por pessoas que podem ter nível de escolaridade variada. O termo:

- _Login_ pode ser visto na figura 1 e 2; 
- _Home_ na figura 4;
- _Profile_ na figura 5;
- _Search_ na figura 6; e
- _History_ na figura 7.


<br>

<!-- ### M10 - Clareza dos Ícones
**Valor Atual: 45% | Meta: ≥85% | Status: 🔴 Crítico** -->

* 5) Alguns ícones do aplicativo não são intuitivos ou podem gerar interpretações ambíguas, como o ícone de menu hambúrguer sendo usado para representar "Histórico" (figura 7).

* 6) O histórico, representado pela figura 7, apresenta uma lista de compras. Essa lista não dá clareza ao usuário sobre o que exatamente ele comprou, visto que falta o campo "nome do produto". Atualmente, só existem os campos "vendedor", "data de compra" e "valor"

Logo, das 11 mensagens avaliadas somente 1 apresentou-se com clareza, totalizando **9,09% na métrica M4**.

#### Propostas de melhoria para M4:
- **Aumentar peso da fonte** (bold/semi-bold) para melhor legibilidade
- **Redesenhar indicadores do carrossel** com cores contrastantes e tamanho maior
- **Traduzir todos os termos** para português (History → Histórico, Search → Buscar)
- **Substituir ícone hambúrguer** por ícone de relógio para histórico
- **Adicionar campo "nome do produto"** no histórico de compras


### M5 - Consistência Operacional
**Valor Atual: 60% | Meta: ≤10% | Status: 🔴 Crítico**

- A versão web apresenta diferenças quanto a responsividade dependendo do dispositivo utilizado:

<center>
<img src="../../assets/ipad_air.png" alt="Problema de responsividade no Ipad Air" width="300"/>
</center>
<center>
<b>Figura 12</b>: Problema de responsividade no Ipad Air.
</center>

<center>
<img src="../../assets/iphone_pro_max.png" alt="Responsividade no Iphone 14 Pro Max praticamente adequadal" width="300"/>
</center>
<center>
<b>Figura 13</b>: Responsividade no Iphone 14 Pro Max praticamente adequada.
</center>

<center>
<img src="../../assets/iphone_xr.png" alt="Problema de responsividade no Iphone XR" width="300"/>
</center>
<center>
<b>Figura 14</b>: Problema de responsividade no Iphone XR.
</center>

<center>
<img src="../../assets/s20.png" alt="Responsividade no Galaxy S20 Ultra praticamente adequadal" width="300"/>
</center>
<center>
<b>Figura 16</b>: Problema de responsividade no Galaxy S20 Ultra.
</center>


- Já no aplicativo, como visto na figura 10, não houveram problemas.

Dadas as 5 mesmas telas em dispotivos diferentes, 3 possuem problemas de implementação responsividade, totalizando **60% na métrica M5**.

#### Proposta de melhoria para M5:
- **Documentar guidelines** de design responsivo para a equipe.
- **Expandir testes** para diferentes tamanhos de tela

<!-- ### M4 - Navegação Bem-sucedida  
**Valor Atual: 75% | Meta: ≥90% | Status: 🔴 Crítico**

- De forma geral, o usuário consegue acessar e navegar pelas telas, compreendendo os textos e imagens apresentados.  
- Contudo, a utilização de termos estrangeiros pode ser um obstáculo para alguns usuários, prejudicando a completude e a facilidade de uso.
- O uso de cores muito semelhantes em determinadas telas pode gerar confusão visual, principalmente para usuários com limitações cognitivas ou baixa visão. -->

### M6  Completude e Facilidade de Uso da Documentação do Usuário
**Valor Atual Estimado: 60% | Meta: ≥85% | Status: ⚠️ Abaixo da meta**

- Os manuais explicam as funcionalidades do aplicativo, fluxo de uso e integrações, ajudando o usuário a entender o propósito e operação do sistema.
- Não há instruções claras para baixar o app mobile, clonar o projeto ou configurar o ambiente local.


#### Proposta de melhoria para M6:
- **Documentação** documentos atualizados de com instalar
- **Aplicativo** funcionando em lojas oficiais


<!--
- Ausência de links diretos para APK 
- versões desatualizadas de dependências, que pode gerar confusão técnica.
-->

### M7 - Prevenção de Erros
**Valor Atual: 100% | Meta: ≥85% | Status: ✅ Atingido**

Em qualquer software, é capaz do usuário se encontrar preso em uma tela sem volta, sendo obrigado a fechar o aplicativo. Para evitar esse tipo de erro, perceba que as 8 telas mobile disponibilizam formas de sair da tela, seja através de:

* uma seta para voltar a página anterior; ou
* o menu inferior com ícones clicáveis com acesso direto a páginas chave do aplicativo.



A figura 9, relacionada a funcionalidade "Compras", mostra mais um padrão de erro:
* **Padrão de erro**: adicionar quantidades além do desejado de um mesmo item.
* **Prevenção a operação incorreta**: opção de diminuir as quantidades selecionadas de um mesmo item.


Já na figura 8:
* **Padrão de erro**: adicionar itens indesejados no pedido.
* **Prevenção a operação incorreta**: opção de remover um item dos pedidos

Dessa forma, totaliza-se:
- Nº de funcionalidades que implementam prevenção de erros: 3
- Nº total de padrões de operações incorretas: 3

Resultando em **100% na métrica M7**.

## Resumo das Métricas Avaliadas

| Métrica | Valor Atual | Meta | Status |
|---------|-------------|------|--------|
| M1 - Completude Funcional | 60% | ≥85% | ⚠️ Abaixo da meta |
| M2 - Precisão Computacional | 0% | =100% | 🔴 Crítico |
| M3 - Apropriação Funcional | 100% | ≥85% | ✅ Atingido |
| M4 - Clareza das Mensagens | 9,09% | ≥85% | 🔴 Crítico |
| M5 - Consistência Operacional | 60% | ≤10% | 🔴 Crítico |
| M6 - M6  Completude e Facilidade de Uso da Documentação do Usuário | 60% | ≥85% | ⚠️ Abaixo da meta |
| M7 - Prevenção a erros | 100% | ≥85% | ✅ Atingido |


## Histórico de Versão

<table border="1" style="width:100%; border-collapse: collapse; text-align: left;">
  <thead>
    <tr>
      <th>Versão</th>
      <th>Data</th>
      <th>Descrição</th>
      <th>Autor(a)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>1.0</td>
      <td>31/05/2025</td>
      <td>Commit inicial, incluindo Objetivos, ODS e questões de análise</td>
      <td>Raphael Mendes da Silva, Leonardo Barcellos, Breno Lucena, Luis Zarbielli</td>
    </tr>
    <tr>
      <td>1.1</td>
      <td>02/07/2025</td>
      <td>Revisão</td>
      <td>Leonardo Barcellos, Breno Lucena, Luis Zarbielli</td>
    </tr>
    <tr>
      <td>1.2</td>
      <td>06/07/2025</td>
      <td>Alinhamento com métricas Q-Rapid e organização por métricas</td>
      <td>Breno Lucena</td>
    </tr>    <tr>
      <td>1.3</td>
      <td>06/07/2025</td>
      <td>Adição do planejamento de avaliação</td>
      <td>Dannyeclisson, Luis Zarbielli</td>
    </tr>
    <tr>
      <td>1.4</td>
      <td>06/07/2025</td>
      <td>Adição de propostas de melhoria para todas as métricas e correção de caminhos das imagens</td>
      <td>Luis Zarbielli, Dannyeclisson</td>
    </tr>
    <tr>
      <td>1.5</td>
      <td>06/07/2025</td>
      <td>Alinhamento com as métricas SQUARE escolhidas, exclusão de métricas redundantes, combinação de justificativas das medidas, adição de novas jusitifativas e provas, ajuste das metas de todas as métricas, cálculo das medidas de todas as métricas</td>
      <td>Raphael Mendes da Silva e Breno Lucena</td>
    </tr>
    <tr>
      <td>1.6</td>
      <td>07/07/2025</td>
      <td>M2 e M3</td>
      <td>Raphael Mendes da Silva, Breno Lucena, Luis Zarbielli e Dannyeclisson</td>
    </tr>
  </tbody>
</table>