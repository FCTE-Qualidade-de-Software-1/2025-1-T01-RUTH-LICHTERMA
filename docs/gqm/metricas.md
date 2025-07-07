# Métricas
Definidas através da análise das perguntas e hipóteses e da consulta às ISOs de família SQUARE.

## Adequação Funcional

|ID|Nome|Objetivo|Cálculo (segundo a SQUARE)|
|-|-|-|-|
|M1|Cobertura de Implementação Funcional (Functional implementation coverage)| Como completar a implementação de acordo com as especificações de requisito?|(Nº de funcionalidades nos requisitos) ÷ (Nº funcionalidades incorretas ou faltando)|
|M2|Precisão Computacional (Computational Accuracy)| O quão frequentes são resultados errados das funções implementadas?| (Nº de operações erradas) ÷ (tempo gasto nelas)|
|M3|Apropriação Funcional (Functional appropriateness)| Quantas funcionalidades realizam seus objetivos sem problemas?| (Nº de funções que realizam tarefas específicas) ÷ (Nº de funções com problemas)|

## Usabilidade

|ID|Nome|Objetivo|Cálculo (segundo a SQUARE)|
|-|-|-|-|
|M4|Clareza da Mensagem (Message clarity)|O quão clara mensagens operacionais do sistema podem ser entendidas?| (Nº de mensagens claras) ÷ (Total de mensagens) |
|M5|Consistência Operacional (Operational Consistency)|O quão consistentes são operações similares| (Nº de operações inconsistentes) ÷ (Nº de operações de comportamento similar) |
|M6|Completude e Facillidade de Uso da Documentação do Usuário (Completeness of user documentation and/or help facility)|Qual a proporção da funcionalidades descritas na documentação?|(Nº de funcionalidades descritas corretamente) ÷ (Nº total de funcionalidades) |
|M7|Prevenção a Operações Incorretas (Avoidance of incorrect operation - AIO)|Quantas funcionalidades têm prevenção a operações incorretas?| (Nº de funcionalidades que implementaram AIO) ÷ (Nº total de padrões de operações incorretas) |

<!-- |ID|Nome|Objetivo|Valor Atual|Meta|Status|
|-|-|-|-|-|-|
|M1|Cobertura de Implementação Funcional| Completude da implementação conforme especificações|75%|≥85%|🔴 Crítico|
|M2|Sucesso em Tarefas Centrais| Frequência de operações corretas em compra/adição|70%|≥90%|🔴 Crítico|
|M3|Autonomia do Usuário| Funcionalidades executadas sem suporte técnico|65%|≥80%|🔴 Crítico|

## Usabilidade

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
-->

## Relação entre Objetivos de Medição - Questões e Métricas - Objetivo de Medição 1: Adequação Funcional

<center><p>Figura 2 - Questões e Métricas - Adequação Funcional</p></center>

![Questões e Métricas - Adequação Funcional](../assets/functional.jpeg)

## Relação entre Objetivos de Medição - Questões e Métricas - Objetivo de Medição 2: Usabilidade

<center><p>Figura 3 - Questões e Métricas - Usabilidade</p></center>

![Questões e Métricas - Usabilidade](../assets/usability.jpeg)



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
      <td>02/07/2025</td>
      <td>Exposição de métricas</td>
      <td>Raphael Mendes da Silva</td>
    </tr>
    <tr>
      <td>1.3</td>
      <td>06/07/2025</td>
      <td>Separação em arquivo e paǵina dedicados</td>
      <td>Raphael Mendes da Silva e Breno Lucena</td>
    </tr>
  </tbody>
</table>