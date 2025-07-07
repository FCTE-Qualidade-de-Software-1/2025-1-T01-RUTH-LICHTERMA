# Avaliação

## Planejamento da Avaliação

### 1. Objetivo da Avaliação
Avaliar a qualidade do sistema AgroMart quanto à adequação funcional e usabilidade, identificando pontos críticos e oportunidades de melhoria, utilizando métricas baseadas no modelo GQM.

### 2. Escopo
- Funcionalidades principais do aplicativo (Cadastro, Login, Instalação, Uso, Compra)
- Usabilidade (legibilidade, navegação, nomenclatura, prevenção de erros, consistência, etc.)

### 3. Métricas a serem avaliadas
- M1: Completude Funcional
- M4: Navegação
- M5: Consistência entre Dispositivos
- M7: Legibilidade das Mensagens
- M8: Descoberta de Carrossel
- M9: Compreensão de Nomenclatura
- M10: Clareza dos Ícones
- M11: Prevenção de Erros
- M12: Compreensão CSA

### 4. Metodologia
- **Revisão de documentação:** Analisar requisitos, fluxos e telas fornecidas.
- **Testes exploratórios:** Navegar pelo sistema (quando possível) para identificar problemas de usabilidade e funcionalidade.
- **Análise de capturas de tela:** Avaliar funcionalidades e usabilidade a partir das imagens fornecidas.
- **Checklist de métricas:** Preencher tabela de métricas com valor atual, meta, status e justificativa.

### 5. Critérios de Aceite
- Todas as métricas críticas (🔴) devem ter plano de ação definido.
- Métricas com status "Atingido" (✅) devem ser documentadas como boas práticas.
- O relatório deve conter evidências (prints, tabelas, justificativas).



## Avaliação de Adequação Funcional - Observações

### M1 - Cobertura de Implementação Funcional
**Valor Atual: 75% | Meta: ≥85% | Status: 🔴 Crítico**

- **(F1) Cadastro**: não foi possível verificar, pois não há ambiente de testes funcional disponível.  
- **(F2) Login**: não foi possível verificar o fluxo completo, considerando apenas as capturas de tela.  
- **(F3) Instalação**:
  - Não há aplicativo publicado em lojas oficiais (Google Play, App Store).  
  - Não existe um APK pronto para download direto.  
  - O tutorial de parte do deploy encontra-se armazenado em um repositório separado das aplicações ([Ajuda AgroMart](https://github.com/AgroMart/ajuda-agromart)).  
- **(F4) Uso**: não pôde ser avaliado de forma completa devido à ausência de ambiente interativo funcional.  
- **(F5) Compra**: não foi possível verificar as operações de compra em funcionamento, considerando que apenas as telas estáticas foram fornecidas.

#### Proposta de melhoria para M1:
- **Criar ambiente de teste funcional** para validar todas as funcionalidades
- **Publicar aplicativo nas lojas oficiais** (Google Play e App Store)
- **Gerar APK de demonstração** para testes diretos  


## Avaliação de Usabilidade - Observações

### M7 - Legibilidade das Mensagens
**Valor Atual: 35% | Meta: ≥90% | Status: 🔴 Crítico**

- As descrições dos menus apresentam uma fonte com cor muito clara, dificultando a leitura em alguns dispositivos.

<center>
<img src="../../assets/tela-com-texto-ruim.jpeg" alt="Fonte clara" width="300"/>
</center>
<center>
**Figura 1**: Tela de Inicial
</center>

#### Proposta de melhoria para M7:
- **Aplicar alto contraste** seguindo WCAG 2.1 (mínimo 4.5:1)
- **Aumentar peso da fonte** (bold/semi-bold) para melhor legibilidade
- **Implementar modo escuro/claro** para usuários

### M8 - Descoberta de Carrossel
**Valor Atual: 25% | Meta: ≥85% | Status: 🔴 Crítico**

- Na tela inicial há um carrossel de imagens, porém os indicadores visuais que evidenciam tratar-se de um carrossel são difíceis de perceber, pois as três bolinhas estão quase imperceptíveis devido à sua cor. O usuário precisa arrastar manualmente para descobrir outras imagens, o que pode gerar confusão.

<center>
<img src="../../assets/carrossel.jpeg" alt="Carrossel" width="300"/>
</center>
<center>
**Figura 2**: Tela inicial do aplicativo mostrando o carrossel 
</center>

#### Proposta de melhoria para M8:
- **Redesenhar indicadores** com cores contrastantes e tamanho maior
- **Adicionar setas de navegação** laterais para indicar swipe
- **Incluir números nos indicadores** (1/3, 2/3, 3/3)

### M12 - Compreensão CSA
**Valor Atual: 85% | Meta: ≥80% | Status: ✅ Atingido**

- A tela de busca de CSA está bem estruturada, apresentando imagens de pontos específicos de cada região administrativa, acompanhadas do respectivo nome, o que facilita a compreensão.

<center>
<img src="../../assets/csa.jpeg" alt="Tela de CSA" width="300"/>
</center>
<center>
**Figura 3**: Tela de csa 
</center>

#### Proposta de melhoria para M12:
- **Manter padrão visual** como referência para outras telas
- **Adicionar filtros de busca** por região ou tipo de produto

### M9 - Compreensão de Nomenclatura
**Valor Atual: 55% | Meta: ≥95% | Status: 🔴 Crítico**

- Alguns termos do aplicativo estão apresentados em inglês (por exemplo, *History*), o que pode dificultar o entendimento do público-alvo, formado majoritariamente por usuários sem familiaridade com outros idiomas.

<center>
<img src="../../assets/home.jpeg" alt="Home" width="300"/>
</center>

<center>
<img src="../../assets/search.jpeg" alt="Search" width="300"/>
</center>

- O ícone da tela de histórico é representado por três linhas (menu tipo hambúrguer), o que pode gerar dúvidas, pois não está claramente identificado como "Histórico".

<center>
<img src="../../assets/historico.jpeg" alt="Historico" width="300"/>
</center>

#### Proposta de melhoria para M9:
- **Traduzir todos os termos** para português (History → Histórico, Search → Buscar)
- **Substituir ícone hambúrguer** por ícone de relógio para histórico
- **Padronizar nomenclatura** com glossário específico do domínio agrícola


### M10 - Clareza dos Ícones
**Valor Atual: 45% | Meta: ≥85% | Status: 🔴 Crítico**

- Alguns ícones do aplicativo não são intuitivos ou podem gerar interpretações ambíguas, como o ícone de menu hambúrguer sendo usado para representar "Histórico".

#### Proposta de melhoria para M10:
- **Substituir ícones ambíguos** por símbolos universalmente reconhecidos
- **Adicionar labels descritivos** acompanhando ícones críticos
- **Padronizar biblioteca de ícones** (Material Design ou iOS Guidelines)

### M5 - Consistência entre Dispositivos
**Valor Atual: 82% | Meta: ≥80% | Status: ✅ Atingido**

- O aplicativo apresenta boa responsividade e funcionamento consistente no ambiente mobile, o que é positivo.

#### Proposta de melhoria para M5:
- **Documentar guidelines** de design responsivo para a equipe
- **Expandir testes** para diferentes tamanhos de tela

### M4 - Navegação Bem-sucedida  
**Valor Atual: 75% | Meta: ≥90% | Status: 🔴 Crítico**

- De forma geral, o usuário consegue acessar e navegar pelas telas, compreendendo os textos e imagens apresentados.  
- Contudo, a utilização de termos estrangeiros pode ser um obstáculo para alguns usuários, prejudicando a completude e a facilidade de uso.
- O uso de cores muito semelhantes em determinadas telas pode gerar confusão visual, principalmente para usuários com limitações cognitivas ou baixa visão.

#### Proposta de melhoria para M4:
- **Traduzir termos estrangeiros** para português
- **Aumentar contraste** entre elementos interativos
- **Adicionar breadcrumbs** para orientação de navegação

### M11 - Prevenção de Erros
**Valor Atual: 15% | Meta: ≥80% | Status: 🔴 Crítico**

- Ainda não foram identificados mecanismos claros de prevenção a operações incorretas, tampouco feedbacks de erro visíveis no sistema. Recomenda-se mapear esses pontos futuramente para aumentar a segurança operacional e evitar falhas de uso.

#### Proposta de melhoria para M11:
- **Implementar validação em tempo real** em formulários críticos
- **Criar confirmações** para ações irreversíveis (compras, exclusões)
- **Desenvolver mensagens de erro claras** em português

## 📊 Resumo das Métricas Avaliadas

| Métrica | Valor Atual | Meta | Status | Justificativa Principal |
|---------|-------------|------|--------|------------------------|
| M1 - Completude Funcional | 75% | ≥85% | 🔴 Crítico | Funcionalidades não testáveis |
| M4 - Navegação | 75% | ≥90% | 🔴 Crítico | Problemas de nomenclatura |
| M5 - Consistência | 82% | ≥80% | ✅ Atingido | Boa responsividade mobile |
| M7 - Legibilidade | 35% | ≥90% | 🔴 Crítico | Fontes com baixo contraste |
| M8 - Carrossel | 25% | ≥85% | 🔴 Crítico | Indicadores imperceptíveis |
| M9 - Nomenclatura | 55% | ≥95% | 🔴 Crítico | Termos em inglês |
| M10 - Ícones | 45% | ≥85% | 🔴 Crítico | Ícones ambíguos |
| M11 - Prevenção | 15% | ≥80% | 🔴 Crítico | Ausência de validações |
| M12 - CSA | 85% | ≥80% | ✅ Atingido | Interface bem estruturada |


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
  </tbody>
</table>