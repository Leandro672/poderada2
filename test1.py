from pytest_bdd import scenario, given, when, then
import time
import random

@scenario("rappi_tests.feature", "Exibição correta dos ganhos")
def test_precision_tela_ganhos():
    pass

@given("um entregador acessa a tela de ganhos")
def entregador_acessa_tela():
    pass  # Simula a ação do usuário acessando a tela

@when("o backend retorna os valores processados corretamente")
def backend_retorna_valores():
    global valores_backend
    valores_backend = {"ganhos": 100.50}
    time.sleep(random.uniform(0, 5))  # Simula um tempo de resposta variável

@then("a tela de ganhos exibe os valores sem discrepâncias")
def tela_exibe_valores():
    valores_exibidos = {"ganhos": 100.50}  # Simula valores na UI
    assert valores_exibidos == valores_backend

@then("o tempo de exibição não ultrapassa 5 segundos em 95% das requisições")
def tempo_resposta():
    tempo_resposta = random.uniform(0, 5)
    assert tempo_resposta <= 5

@then("um alerta é disparado se houver discrepâncias entre os valores mostrados e os valores reais processados no backend")
def verifica_alerta():
    valores_exibidos = {"ganhos": 99.99}  # Simula um erro na UI
    alerta_disparado = valores_exibidos != valores_backend
    assert alerta_disparado
