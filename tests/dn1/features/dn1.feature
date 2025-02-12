Feature: Precisão da Tela de Ganhos

Background:
  Given que o entregador está logado na plataforma


  # Teste para garantir que a tela de ganhos exibe valores corretos e atualizados
  Scenario: Exibir informações corretas e atualizadas na tela de ganhos
    When o entregador consulta a tela de ganhos
    Then o sistema deve exibir os valores corretos e atualizados para o entregador
    And a precisão da tela de ganhos deve ser de 99,9% em todas as consultas

  # Teste de performance: garantir que o atraso na exibição dos valores não ultrapasse 5 segundos
  Scenario: Atraso na exibição dos valores
    Given que o entregador consulta a tela de ganhos


  # Teste de monitoramento de discrepâncias entre os valores exibidos e os valores reais
  Scenario: Detectar discrepâncias entre os valores exibidos e os valores reais
    When o sistema exibe os valores na tela de ganhos
    Then o sistema deve verificar se os valores exibidos são consistentes com os valores processados no backend

