# Goal-Question-Metric (GQM)

## Propósito Empresarial do AgroMart
<div align="justify">

A finalidade comercial do AGROMART consiste em criar uma solução tecnológica revolucionária que promova a ligação direta entre produtores agrícolas e compradores finais, particularmente considerando as dificuldades geradas pelo distanciamento social durante a crise sanitária da COVID-19. A plataforma concentra seus esforços em simplificar e potencializar a venda de produtos sustentáveis, garantindo acesso imediato ao mercado para pequenos agricultores, apoiando a criação e gestão de Comunidades que Sustentam a Agricultura (CSAs).

</div>

## Objetivos de Medição

### Objetivo 1: Adequação Funcional
|||
|---|---|
| Analisar | AgroMart |
| Para o propósito de | Entender |
| Com Respeito a | Adequação Funcional |
| Ponto de Vista | Dono do Produto e Agricultor CSA |
| Contexto | Sistema com 8 interfaces principais e usuários com conhecimento tecnológico intermediário |

### Objetivo 2: Usabilidade e Aprendizado
|||
|---|---|
| Analisar | AgroMart |
| Para o propósito de | Entender |
| Com Respeito a | Usabilidade |
| Ponto de Vista | Consumidores CSA e Agricultores CSA |
| No contexto de | Sistema com componentes textuais/visuais e usuários com conhecimento médio em CSA |

## Questões e Métricas - Objetivo 1: Adequação Funcional

> **Q1:** As interfaces principais do sistema atendem completamente aos requisitos funcionais?  
> **Hipótese 1:** Pelo menos 85% das funcionalidades nas interfaces principais foram implementadas adequadamente.  

> **Q2:** As tarefas centrais (Comprar e Adicionar produtos) operam corretamente?  
> **Hipótese 2:** 90% das operações de compra e adição de produtos executam sem erros.  

> **Q3:** O sistema é funcionalmente adequado para usuários com conhecimento tecnológico intermediário?  
> **Hipótese 3:** 80% dos usuários conseguem executar funcionalidades sem suporte técnico.  

## Questões e Métricas - Objetivo 2: Usabilidade

> **Q4:** O usuário consegue navegar pelas 8 interfaces principais sem dificuldades?  
> **Hipótese 4:** 90% dos usuários navegam entre as interfaces sem abandonar tarefas.  

> **Q5:** A terminologia utilizada é compreensível para usuários com conhecimento médio em CSA?  
> **Hipótese 5:** 85% dos usuários entendem os termos relacionados à agricultura sustentável sem explicação adicional.  

> **Q6:** As interfaces apresentam consistência considerando os diferentes ambientes (Android/Linux)?  
> **Hipótese 6:** 90% dos usuários percebem consistência visual e processual entre diferentes dispositivos.  

> **Q7:** Os componentes principais (textos e imagens) são facilmente compreendidos?  
> **Hipótese 7:** 85% dos elementos visuais são interpretados corretamente sem legendas auxiliares.  

> **Q8:** O usuário consegue se recuperar facilmente de erros durante as tarefas principais?        
> **Hipótese 8:** 80% dos usuários conseguem corrigir erros sem abandonar a tarefa.  

> **Q9:** O tempo de aprendizado é adequado considerando o conhecimento médio dos usuários em CSA?            
> **Hipótese 9:** Tempo médio de aprendizado das funcionalidades ≤ 15 minutos.

## Métricas
Definidas através da análise das perguntas e hipóteses e da consulta às ISOs de família SQUARE.

### Adequação Funcional

|ID|Nome|Objetivo|Valor Atual|Meta|Status|
|-|-|-|-|-|-|
|M1|Cobertura de Implementação Funcional| Completude da implementação conforme especificações|75%|≥85%|🔴 Crítico|
|M2|Sucesso em Tarefas Centrais| Frequência de operações corretas em compra/adição|70%|≥90%|🔴 Crítico|
|M3|Autonomia do Usuário| Funcionalidades executadas sem suporte técnico|65%|≥80%|🔴 Crítico|

### Usabilidade

|ID|Nome|Objetivo|Valor Atual|Meta|Status|
|-|-|-|-|-|-|
|M4|Navegação Bem-sucedida|Usuários que navegam entre interfaces sem abandonar|75%|≥90%|🔴 Crítico|
|M5|Consistência entre Dispositivos|Consistência visual/processual entre Android/Linux|82%|≥80%|✅ Atingido|
|M7|Legibilidade das Mensagens|Mensagens operacionais compreendidas claramente|35%|≥90%|🔴 Crítico|
|M8|Descoberta de Carrossel|Usuários que identificam funcionalidade do carrossel|25%|≥85%|🔴 Crítico|
|M9|Compreensão de Nomenclatura|Termos compreendidos por usuários CSA|55%|≥95%|🔴 Crítico|
|M10|Reconhecimento de Ícones|Ícones interpretados corretamente|45%|≥85%|🔴 Crítico|
|M11|Prevenção de Erros|Funcionalidades com mecanismos de prevenção|15%|≥80%|🔴 Crítico|
|M12|Compreensão CSA|Elementos relacionados a CSA compreendidos|85%|≥80%|✅ Atingido|

## Relação entre Objetivos de Medição - Questões e Métricas - Objetivo de Medição 1: Adequação Funcional

<center><p>Figura 2 - Questões e Métricas - Adequação Funcional</p></center>

![Questões e Métricas - Adequação Funcional](../assets/functional.jpeg)

## Relação entre Objetivos de Medição - Questões e Métricas - Objetivo de Medição 2: Usabilidade

<center><p>Figura 3 - Questões e Métricas - Confiabilidade</p></center>

![Questões e Métricas - Confiabilidade](../assets/usability.jpeg)


## Fontes e Heurísticas para as Questões

| Questão | Fonte / Heurística ou Norma |
|:---|:---|
| **Q1-Q3** | **ISO/IEC 25010:2011 – Functional Suitability**. Completude, correção e adequação funcional. |
| **Q4** | **Heurística 6 – Reconhecimento em vez de memorização** (Nielsen, 1995). Facilitar navegação e reduzir carga cognitiva. |
| **Q5** | **Heurística 2 – Correspondência entre o sistema e o mundo real** (Nielsen, 1995). Usar linguagem familiar ao domínio CSA. |
| **Q6** | **Heurística 4 – Consistência e padrões** (Nielsen, 1995). Manter padrões entre diferentes ambientes. |
| **Q7** | **Affordances e Signifiers** (Norman, 1988). Elementos visuais devem comunicar sua função naturalmente. |
| **Q8** | **Heurística 5 – Prevenção de erros** e **Heurística 9 – Recuperação de erros** (Nielsen, 1995). |
| **Q9** | **ISO 9241-110:2020 – Suitability for learning**. Facilidade de aprendizado para usuários do domínio. |

## Referências Bibliográficas
> NIELSEN, Jakob. Usability Engineering. Academic Press, 1995.  
> NORMAN, Donald A. The Design of Everyday Things. Basic Books, 1988.  
> ISO/IEC 25010:2011 - Systems and software engineering - Systems and software Quality Requirements and Evaluation (SQuaRE)  
> ISO 9241-110:2020 - Ergonomics of human-system interaction

## Histórico de Versões
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
      <td>21/05/2025</td>
      <td>Criação do documento</td>
      <td>Leonardo Barcellos</td>
    </tr>
    <tr>
      <td>1.1</td>
      <td>22/05/2025</td>
      <td>Revisão</td>
      <td>Raphael Mendes</td>
    </tr>
    <tr>
      <td>1.2</td>
      <td>02/06/2025</td>
      <td>Expansão das questões</td>
      <td>Breno Lucena, Luis Zarbielli e Dannyeclisson Rodrigo</td>
    </tr>
    <tr>
      <td>1.3</td>
      <td>03/06/2025</td>
      <td>Revisão</td>
      <td>Leonardo Barcellos, Raphael Mendes da Silva e Breno Lucena</td>
    </tr>
  </tbody>
</table>

