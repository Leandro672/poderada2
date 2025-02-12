# poderada 2

## DN1 - Precisão da Tela de Ganhos
- Requisito: A tela de ganhos do entregador deve exibir informações corretas e atualizadas em 99,9% das consultas.
- Métrica: O atraso na exibição dos valores não pode ultrapassar 5 segundos em 95% das requisições.
- Monitoramento:
Se houver discrepâncias entre os valores mostrados e os valores reais processados no backend, um alerta deve ser disparado.
Logs automáticos das consultas de ganhos devem ser registrados para auditoria.

## DN2 - Eficiência e Distribuição da Frota do Turbo 10
- Requisito: A distribuição da frota do Turbo 10 deve garantir que 95% dos pedidos sejam atribuídos a um entregador em até 30 segundos.
- Métrica:
O tempo médio de alocação de entregador deve ser inferior a 15 segundos para pedidos de Retail.
Para Restaurantes e Mercados, o tempo médio de alocação não pode ultrapassar 20 segundos.
Se mais de 5% dos pedidos permanecerem sem entregador por mais de 60 segundos, um alerta deve ser disparado.
- Monitoramento:
O sistema deve rastrear e ajustar automaticamente a frota com base na demanda por segmento (Retail, Restaurante, Mercado).
Se uma categoria específica tiver tempo de alocação 50% maior que a média das outras, um alerta é gerado.

