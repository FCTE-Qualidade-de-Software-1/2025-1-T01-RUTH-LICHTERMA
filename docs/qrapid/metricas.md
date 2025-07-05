# Q-Rapid: Métricas e Dados para Dashboard

## Visão Geral
Este documento define as métricas coletadas através da metodologia Q-Rapid para o projeto AgroMart, que serão utilizadas para gerar dashboards de qualidade de software.

## Métricas de Adequação Funcional

### M1: Taxa de Completude Funcional
- **Descrição:** Percentual de funcionalidades implementadas corretamente nas 8 interfaces principais
- **Fórmula:** (Funcionalidades Implementadas / Total de Funcionalidades) × 100
- **Meta:** ≥ 85%
- **Fonte:** Análise das interfaces do sistema
- **Frequência de Coleta:** Semanal

### M2: Taxa de Sucesso em Tarefas Críticas
- **Descrição:** Percentual de operações de compra e adição de produtos executadas sem erros
- **Fórmula:** (Operações Bem-sucedidas / Total de Operações) × 100
- **Meta:** ≥ 90%
- **Fonte:** Logs do sistema e testes funcionais
- **Frequência de Coleta:** Diária

### M3: Autonomia do Usuário
- **Descrição:** Percentual de usuários que conseguem executar funcionalidades sem suporte técnico
- **Fórmula:** (Usuários Autônomos / Total de Usuários Testados) × 100
- **Meta:** ≥ 80%
- **Fonte:** Testes de usabilidade
- **Frequência de Coleta:** Mensal

## Métricas de Usabilidade

### M4: Taxa de Navegação Bem-sucedida
- **Descrição:** Percentual de usuários que navegam entre interfaces sem abandonar tarefas
- **Fórmula:** (Navegações Completas / Total de Tentativas) × 100
- **Meta:** ≥ 90%
- **Fonte:** Analytics de navegação
- **Frequência de Coleta:** Diária

### M5: Consistência entre Dispositivos
- **Descrição:** Percentual de usuários que percebem consistência visual entre dispositivos
- **Fórmula:** (Percepção Positiva / Total de Avaliações) × 100
- **Meta:** ≥ 90%
- **Fonte:** Testes multi-dispositivo
- **Frequência de Coleta:** Mensal

### M6: Clareza dos Elementos Visuais
- **Descrição:** Percentual de elementos visuais interpretados corretamente
- **Fórmula:** (Interpretações Corretas / Total de Elementos Testados) × 100
- **Meta:** ≥ 85%
- **Fonte:** Testes de compreensão visual
- **Frequência de Coleta:** Quinzenal

### M7: Taxa de Recuperação de Erros
- **Descrição:** Percentual de usuários que conseguem corrigir erros sem abandonar tarefas
- **Fórmula:** (Recuperações Bem-sucedidas / Total de Erros Encontrados) × 100
- **Meta:** ≥ 80%
- **Fonte:** Observação de sessões de uso
- **Frequência de Coleta:** Semanal

### M8: Tempo de Aprendizado
- **Descrição:** Tempo médio para usuários aprenderem as funcionalidades principais
- **Unidade:** Minutos
- **Meta:** ≤ 15 minutos
- **Fonte:** Testes de primeira utilização
- **Frequência de Coleta:** Mensal

## Dados Simulados para Demonstração

```json
{
  "timestamp": "2025-07-03T10:00:00Z",
  "metrics": {
    "M1_completude_funcional": 87.5,
    "M2_sucesso_tarefas": 92.0,
    "M3_autonomia_usuario": 83.0,
    "M4_navegacao_sucesso": 89.5,
    "M5_compreensao_csa": 86.0,
    "M6_consistencia_dispositivos": 91.0,
    "M7_clareza_visual": 88.0,
    "M8_recuperacao_erros": 82.5,
    "M9_tempo_aprendizado": 14.2
  }
}
```

## Histórico de Versões

| Versão | Data | Descrição | Autor |
|:----:|----|---------|----|
|`1.0`|03/07/2025|Criação do documento de métricas Q-Rapid|Sistema Q-Rapid|
