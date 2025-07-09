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
            <li>Cobertura de Implementação Funcional</li>
            <li>Precisão Computacional</li>
            <li>Apropriação Funcional</li>
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
          <li>Hipótese 1: Pelo menos 85% das funcionalidades nas interfaces principais foram implementadas adequadamente.</li>
          <li>Hipótese 2: 90% das operações de compra e adição de produtos executam sem erros.</li>
          <li>Hipótese 3: 80% dos usuários conseguem executar funcionalidades sem suporte técnico.</li>
        </ul>
    </td>
    <td colspan="2">
        <ul>
            <li>O nível técnico intermediário dos usuários pode impactar a apropriação funcional, por conta da dificuldade do usuário em usar o sistema sem ajuda.</li>
            <li>Os perfis distintos podem impactar na precisão computacional, por conta de usos diferentes de funções gerarem erros.</li>
            <li>A execução em Android/Linux pode impactar a precisão computacional, por conta de comportamentos inconsistentes entre plataformas.</li>
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
            <li>Clareza da Mensagem</li>
            <li>Consistência Operacional</li>
            <li>Completude e Facilidade de Uso da Documentação do Usuário</li>
            <li>Prevenção a Operações Incorretas</li>
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
          <li>Hipótese 4:90% dos usuários navegam entre as interfaces sem abandonar tarefas.</li>
          <li>Hipótese 5:85% dos usuários entendem os termos relacionados à agricultura sustentável sem explicação adicional.</li>
          <li>Hipótese 6: 90% dos usuários percebem consistência visual e processual entre diferentes dispositivos.</li>
          <li>Hipótese 7: 85% dos elementos visuais são interpretados corretamente sem legendas auxiliares.</li>
          <li>Hipótese 8: 80% dos usuários conseguem corrigir erros sem abandonar a tarefa.</li>
        </ul>
    </td>
    <td colspan="2">
        <ul>
            <li>Nível de conhecimento sobre CSA e agricultura</li>
            <li>Diferenças na visualização em diferentes dispotivos, causadas por má implementação da responsividade, pode afetar a consistência operacional.</li>
            <li>A clareza das mensagens é mais efetiva quando há a participação dos usuários no desenvolvimento e quando algum dos envolvidos no projeto, seja os desenvolvedores ou o usuário participante, possuem conhecimento sobre CSA.</li>
            <li>Com um usuário envolvido no desenvolvimento, a completude da documentação de usuário pode ser testada e validada.</li>
            <li>Usuários testando a aplicação em diferentes plataforma ainda durante o desenvolvimento ajuda detectar potenciais funcionalidade que necessitam de mecanismos de prevenção a erros.</li>
        </ul>
    </td>
  </tr>
</table>

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
      <td>25/05/2025</td>
      <td>Revisão</td>
      <td>Raphael Mendes</td>
    </tr>
    <tr>
      <td>1.2</td>
      <td>03/06/2025</td>
      <td>Revisão</td>
      <td>Leonardo Barcellos</td>
    </tr>
    <tr>
      <td>1.3</td>
      <td>07/06/2025</td>
      <td>Implementação dos feedbacks da professora</td>
      <td>Raphael Mendes, Leonardo Barcellos, Breno Lucena, Luis Zarbielli e Dannyeclisson Rodrigo</td>
    </tr>
    <tr>
      <td>1.4</td>
      <td>08/06/2025</td>
      <td>Alinhando com as hipóteses usadas no resto do projeto</td>
      <td>Raphael Mendes</td>
    </tr>
  </tbody>
</table>