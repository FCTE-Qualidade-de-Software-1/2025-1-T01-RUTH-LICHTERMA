# Avaliação Q-Rapid - AgroMart

## Visão Geral

Este documento consolida as métricas do Q-Rapid aplicadas ao projeto **AgroMart**, integrando a avaliação de usabilidade realizada com as metas do modelo GQM e evidências coletadas na avaliação do sistema.  



**Métrica M1 (Taxa de Completude Funcional):**  
- Valor atual estimado: **60%**  
- Meta: ≥ 85%   
- Status: ⚠️ **Abaixo da meta**  
- **Justificativa**: Cadastro, Login e Compra não puderam ser verificados completamente. Instalação sem APK disponível.  


**Métrica M4 ( Clareza das Mensagens):**  
- Valor atual estimado: **9,09%**  
- Meta: ≥ 85%  
- Status: 🔴 **Crítico**  
- **Justificativa**: As descrições dos menus apresentam uma fonte com cor muito clara, dificultando a leitura em alguns dispositivos.


**Métrica M5 (Consistência Operacional):**  
- Valor atual estimado: **60%**  
- Meta: ≤10% 
- Status: 🔴 **Crítico**  
- **Justificativa**:A versão web apresenta diferenças quanto a responsividade dependendo do dispositivo utilizado:



**Métrica M7 (Prevenção de Erros):**  
- Valor atual estimado: **100%**  
- Meta: ≥ 85%  
- Status: ✅ **Atingido**  
- **Justificativa**: Em qualquer software, é capaz do usuário se encontrar preso em uma tela sem volta, sendo obrigado a fechar o aplicativo. Para evitar esse tipo de erro, perceba que as 8 telas mobile disponibilizam formas de sair da tela, seja através de:

* uma seta para voltar a página anterior; ou
* o menu inferior com ícones clicáveis com acesso direto a páginas chave do aplicativo.



##  Resumo Consolidado

| Métrica | Problema | Severidade | Valor Atual |
|---------|-------------------------------------------|------------|--------------|
| **M1**  | Completude Funcional| 🔴 Crítico | 60% |
| **M4**  | Clareza das Mensagens| 🔴 Crítico| 9,09% |
| **M5**  | Consistência Operacional | 🔴 Crítico | 60%  |
| **M7**  | Prevenção a erros | ✅ Atingido | 100% |



##  Plano de Ação

### 🔴 Prioridade Máxima

1. **M11 - Completude Funcional** (60%)  
      - Criar ambiente de teste funcional para validar todas as funcionalidades.
      - Publicar aplicativo nas lojas oficiais (Google Play e App Store).
      - Gerar APK de demonstração para testes diretos.

2. **M4 -  Clareza das Mensagens** (9,09%)  
      - Aumentar peso da fonte (bold/semi-bold) para melhor legibilidade
      - Redesenhar indicadores do carrossel com cores contrastantes e tamanho maior
      - Traduzir todos os termos para português (History → Histórico, Search → Buscar)
      - Substituir ícone hambúrguer por ícone de relógio para histórico
      - Adicionar campo "nome do produto" no histórico de compras

3. **M5 - Consistência Operacional** (60%)  
      - Documentar guidelines de design responsivo para a equipe.
      - Expandir testes para diferentes tamanhos de tela.


### 🟢 Manter/Melhorar

1. **M7 - Prevenção a erros** (100%) 
      - Manter qualidade da interface de busca CSA.





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
      <td>07/07/2025</td>
      <td>Revisão</td>
      <td>Breno Lucena</td>
    </tr>
  </tbody>
</table>

