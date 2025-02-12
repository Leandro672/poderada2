Feature: Eficiência e Distribuição da Frota do Turbo 10
  Background: 
    Given que o sistema tem uma frota de entregadores disponíveis para atender os pedidos
    And o sistema está rastreando os tempos de alocação de entregadores

  # Validação de tempo de alocação para Retail
  Scenario: Tempo médio de alocação de entregador para pedidos de Retail
    When o sistema aloca um entregador para um pedido de Retail
    Then o tempo de alocação deve ser inferior a 15 segundos

  # Validação de tempo de alocação para Restaurantes e Mercados
  Scenario: Tempo médio de alocação de entregador para pedidos de Restaurantes e Mercados
    When o sistema aloca um entregador para um pedido de Restaurante ou Mercado
    Then o tempo de alocação não pode ultrapassar 20 segundos

  # Caso onde mais de 5% dos pedidos ficam sem entregador por mais de 60 segundos
  Scenario: Alerta para pedidos sem entregador por mais de 60 segundos
    When mais de 5% dos pedidos não têm entregador por mais de 60 segundos
    Then o sistema deve gerar um alerta de alocação

  # Teste para garantir que 95% dos pedidos são atribuídos a um entregador em até 30 segundos
  Scenario: Garantir que 95% dos pedidos sejam alocados em até 30 segundos
    Given que o sistema está alocando entregadores para 1000 pedidos
    When o sistema aloca entregadores
    Then pelo menos 95% dos pedidos devem ser atribuídos a um entregador em até 30 segundos

  # Monitoramento de tempo de alocação por categoria
  Scenario: Monitorar tempo de alocação por categoria de pedido
    Then o sistema deve gerar um alerta se o tempo de alocação de uma categoria for 50% maior que a média das outras
