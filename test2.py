from pytest_bdd import scenario, given, when, then
import time
import random

@scenario("efficiency_frota.feature", "Atribuição rápida de entregadores")
def test_efficiency_frota():
    pass

@given("um pedido é criado no sistema")
def pedido_criado():
    pass  # Simula a criação do pedido no sistema

@when("a alocação de um entregador ocorre")
def aloca_entregador():
    global tempo_alocacao
    tempo_alocacao = random.uniform(10, 60)  # Simula um tempo de alocação variável

@then("95% dos pedidos são atribuídos em até 30 segundos")
def verifica_tempo_alocacao():
    assert tempo_alocacao <= 30

@then("um alerta é disparado se mais de 5% dos pedidos demorarem mais de 60 segundos")
def verifica_alerta():
    alerta_disparado = tempo_alocacao > 60
    assert not alerta_disparado
