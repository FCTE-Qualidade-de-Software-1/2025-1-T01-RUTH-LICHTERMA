## Introdução
O artefato a seguir tem como objetivo planejar a avaliação das 8 telas do AgroMart. Será utilizado prints das telas do AgroMart.

### 1. Objetivo da Avaliação
Avaliar a qualidade do sistema AgroMart quanto à adequação funcional e usabilidade, identificando pontos críticos e oportunidades de melhoria, utilizando métricas baseadas no modelo GQM.

### 2. Escopo
- Funcionalidades principais do aplicativo (Cadastro, Login, Instalação, Uso, Compra)
- Usabilidade (legibilidade, navegação, nomenclatura, prevenção de erros, consistência)

### 3. Métricas a serem avaliadas

- M1: Completude Funcional (Functional implementation coverage)
- M2: Precisão Computacional (Computational Accuracy)
- M3: Apropriação Funcional (Functional appropriateness)
- M4: Clareza das Mensagens (Message clarity)
- M5: Consistência Operacional (Operational Consistency)
- M6: Completude e Facillidade de Uso da Documentação do Usuário (Completeness of user documentation and/or help facility)
- M7: Prevenção a Operações Incorretas (Avoidance of incorrect operation - AIO)


### 5. Metodologia
- **Revisão de documentação:** Análise detalhada dos requisitos funcionais e não funcionais, especificações de fluxo de usuário e wireframes/mockups fornecidos.

    Para a revisão de documentação, utilizamos como base os materiais presentes no repositório do AgroMart, especificamente na seção "docs". A equipe do AgroMart também disponibilizou um link público ([https://agromart.github.io/docs/](https://agromart.github.io/docs/)), onde está centralizada toda a documentação do projeto. 
  
    Nessa documentação, encontramos:
        
      - Elicitação de requisitos, contendo todos os requisitos funcionais e não funcionais do aplicativo;
      - Framework de priorização utilizado ("MoSCoW") para definir a prioridade de cada requisito (não foram detalhadas perguntas técnicas além do uso do MoSCoW);
      - Na seção de "modelagem", estão descritos: Casos de Uso, Cenários e Histórias de Usuário, contemplando dois tipos de usuários principais: "Administrador" e "Co-agricultor";
      - No "Backlog", há uma tabela detalhada com a granularidade do backlog, incluindo: Épicos, Features e User Stories
      - Tutorial de instalação do sistema (especificamente isolado no respositório [Ajuda-Agromart](https://github.com/AgroMart/ajuda-agromart));

 - **Avaliação Heurística da Interface:** Inspeção da interface do usuário com base nas Heurísticas de Usabilidade de Nielsen para identificar potenciais falhas de design e usabilidade, elas são:

  - Heurística 2 – Correspondência entre o sistema e o mundo real 
  - Heurística 4 – Consistência e padrões
  - Heurística 5 – Prevenção de erros 
  - Heurística 6 – Reconhecimento em vez de memorização
  - Heurística 9 – Recuperação de erros

- **Checklist de métricas:** Preencher tabela de métricas com valor atual, meta, status e justificativa.

### 6. Critérios de Aceite
- Todas as métricas críticas (🔴) devem ter plano de ação definido.
- Métricas com status "Atingido" (✅) devem ser documentadas como boas práticas.
- O relatório deve conter evidências (prints e justificativas).

A entrega final e a demonstração do cumprimento de todos estes critérios serão realizadas na Fase 4: Relatório de Análise de Qualidade, que apresentará de forma consolidada os resultados, diagnósticos e ações recomendadas.

### 7. Ferramentas e Recursos
- Plataforma analisada AgroMart Web
- Dispositivos de teste (computador pessoal e celular)


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
      <td>07/07/2025</td>
      <td>Criação do documento</td>
      <td>Luis Zarbielli</td>
    </tr>
    <tr>
      <td>1.1</td>
      <td>07/07/2025</td>
      <td>Expansão das métricas avaliadas (M1-M7), melhoria da metodologia com heurísticas específicas de Nielsen, e refinamento dos critérios de aceite</td>
      <td>Luis Zarbielli</td>
    </tr>
        <tr>
      <td>1.2</td>
      <td>07/07/2025</td>
      <td>Revisãoe</td>
      <td>Breno Lucena</td>
    </tr>
  </tbody>
</table>