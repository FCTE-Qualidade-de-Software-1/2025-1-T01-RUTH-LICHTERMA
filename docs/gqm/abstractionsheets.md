# Abstraction Sheets

## Folha de Abstração 1: Adequação Funcional do AgroMart

<table>
  <tr>
    <th>Objeto</th>
    <th>Propósito</th>
    <th>Foco de Qualidade</th>
    <th>Ponto de Vista</th>
  </tr>
  <tr>
    <td>AgroMart</td>
    <td>Entender</td>
    <td>Adequação Funcional</td>
    <td>Dono do Produto e Agricultor CSA</td>
  </tr>
  <tr>
    <th colspan="2">Foco de Qualidade:</th>
    <th colspan="2">Fatores de Variação:</th>
  </tr>
  <tr>
    <td colspan="2">
        <ul>
            <li>Completude funcional das 8 interfaces principais</li>
            <li>Correção funcional das tarefas centrais (Comprar e Adicionar produtos)</li>
            <li>Adequação funcional para usuários com conhecimento tecnológico intermediário</li>
        </ul>
    </td>
    <td colspan="2">
        <ul>
            <li>Nível de conhecimento tecnológico dos usuários (intermediário)</li>
            <li>Diferentes perfis de usuários (Consumidores CSA vs Agricultores CSA)</li>
            <li>Ambiente de execução (Android/Linux)</li>
        </ul>
    </td>
  </tr>
    <tr>
    <th colspan="2">Hipótese Base (estimado):</th>
    <th colspan="2">Impacto dos Fatores de Variação:</th>
  </tr>
  <tr>
    <td colspan="2">
        <ul>
          <li>85% das funcionalidades nas 8 interfaces principais foram implementadas adequadamente</li>
          <li>90% das tarefas centrais (Comprar e Adicionar produtos) operam corretamente</li>
          <li>Tempo médio para completar tarefas críticas ≤ 5 minutos considerando nível intermediário dos usuários</li>
          <li>80% dos usuários conseguem executar funcionalidades sem suporte técnico</li>
        </ul>
    </td>
    <td colspan="2">
        <ul>
            <li>Usuários com conhecimento tecnológico intermediário reduzem problemas de adequação funcional</li>
            <li>Consumidores CSA e Agricultores CSA podem requerer fluxos funcionais específicos</li>
            <li>Diferentes ambientes (Android/Linux) podem impactar a correção funcional</li>
            <li>Ausência de dados-exemplo pode aumentar tempo de execução das tarefas</li>
        </ul>
    </td>
  </tr>
</table>

## Folha de Abstração 2: Usabilidade do Produto

<table>
  <tr>
    <th>Objeto</th>
    <th>Propósito</th>
    <th>Foco de Qualidade</th>
    <th>Ponto de Vista</th>
  </tr>
  <tr>
    <td>AgroMart</td>
    <td>Entender</td>
    <td>Usabilidade</td>
    <td>Consumidores CSA e Agricultores CSA</td>
  </tr>
  <tr>
    <th colspan="2">Foco de Qualidade:</th>
    <th colspan="2">Fatores de Variação:</th>
  </tr>
  <tr>
    <td colspan="2">
        <ul>
            <li>Usabilidade das 8 interfaces principais obrigatórias</li>
            <li>Acessibilidade de textos e imagens (componentes principais)</li>
            <li>Facilidade de aprendizado para conhecimento médio em CSA</li>
        </ul>
    </td>
    <td colspan="2">
        <ul>
            <li>Nível de conhecimento sobre CSA e agricultura sustentável</li>
            <li>Participação dos usuários durante o desenvolvimento</li>
            <li>Diferentes dispositivos (Android/computador Linux)</li>
        </ul>
    </td>
  </tr>
    <tr>
    <th colspan="2">Hipótese Base (estimado):</th>
    <th colspan="2">Impacto dos Fatores de Variação:</th>
  </tr>
  <tr>
    <td colspan="2">
        <ul>
          <li>90% dos usuários navegam pelas 8 interfaces sem dificuldades</li>
          <li>85% dos textos e imagens são compreensíveis sem suporte</li>
          <li>Tempo médio de aprendizado ≤ 15 minutos considerando conhecimento médio em CSA</li>
          <li>80% dos usuários completam tarefas principais sem abandonar o sistema</li>
        </ul>
    </td>
    <td colspan="2">
        <ul>
            <li>Usuários com conhecimento médio em CSA reduzem tempo de aprendizado</li>
            <li>Maior participação dos usuários no desenvolvimento melhora a usabilidade</li>
            <li>Diferentes dispositivos podem requerer adaptações de interface</li>
            <li>Componentes visuais (textos/imagens) impactam diretamente a compreensibilidade</li>
        </ul>
    </td>
  </tr>
</table>

## Histórico de Versões

|Versão|Data|Descrição|Autor|
|:----:|----|---------|-----|
|`1.0`|22/05/2025|Criação do documento|Leonardo Barcellos|
|`1.1`|25/05/2025|Revisão|Raphael Mendes|
|`1.2`|03/06/2025|Revisão|Leonardo Barcellos|