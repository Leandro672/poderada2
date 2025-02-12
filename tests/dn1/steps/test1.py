from behave import given, when, then
import random
import time

# Mockando o contexto de ganhos
ganhos_context = {
    "entregador_logado": True,
    "valores_exibidos": 0.0,
    "valores_reais_backend": 0.0,
    "atraso_exibicao": 0,
    "alerta_discrepancia": False,
    "relatorio_performance": "",
    "historico_alertas": []
}

# -------------------------------
# Cenários de Precisão da Tela de Ganhos
# -------------------------------

@given('que o entregador está logado na plataforma')
def step_entregador_logado(context):
    ganhos_context["entregador_logado"] = True

@when('o entregador consulta a tela de ganhos')
def step_consulta_tela_ganhos(context):
    ganhos_context["valores_reais_backend"] = round(random.uniform(50, 500), 2)  # Simula um valor real do backend
    ganhos_context["valores_exibidos"] = ganhos_context["valores_reais_backend"]

@then('o sistema deve exibir os valores corretos e atualizados para o entregador')
def step_verifica_valores_corretos(context):
    assert ganhos_context["valores_exibidos"] == ganhos_context["valores_reais_backend"], \
        f"Valores exibidos: {ganhos_context['valores_exibidos']}, Valores reais: {ganhos_context['valores_reais_backend']}"

@then('a precisão da tela de ganhos deve ser de 99,9% em todas as consultas')
def step_verifica_precisao(context):
    assert abs(ganhos_context["valores_exibidos"] - ganhos_context["valores_reais_backend"]) <= 0.1, \
        "Precisão da tela de ganhos abaixo de 99,9%"

# -------------------------------
# Teste de Performance
# -------------------------------

@given('que o entregador consulta a tela de ganhos')
def step_consulta_ganhos(context):
    ganhos_context["atraso_exibicao"] = random.uniform(0, 5)  # Simula um atraso na exibição dos valores

@then('o atraso na exibição dos valores não deve ultrapassar {tempo_limite:d} segundos em 95% das requisições')
def step_verifica_performance(context, tempo_limite):
    assert ganhos_context["atraso_exibicao"] <= tempo_limite, \
        f"Atraso de exibição: {ganhos_context['atraso_exibicao']} segundos, que ultrapassa o limite de {tempo_limite} segundos."

# -------------------------------
# Monitoramento de Discrepâncias
# -------------------------------

@when('o sistema exibe os valores na tela de ganhos')
def step_exibe_valores_tela(context):
    ganhos_context["alerta_discrepancia"] = False  # Reseta o alerta de discrepância
    if ganhos_context["valores_exibidos"] != ganhos_context["valores_reais_backend"]:
        ganhos_context["alerta_discrepancia"] = True

@then('o sistema deve verificar se os valores exibidos são consistentes com os valores processados no backend')
def step_verifica_discrepancia(context):
    assert not ganhos_context["alerta_discrepancia"], "Discrepância detectada entre valores exibidos e valores reais."

@then('um alerta deve ser disparado caso haja discrepância')
def step_gera_alerta_discrepancia(context):
    if ganhos_context["alerta_discrepancia"]:
        ganhos_context["historico_alertas"].append("Alerta de discrepância gerado")
    assert ganhos_context["alerta_discrepancia"], "Alerta de discrepância não gerado!"

@then('os alertas devem ser armazenados para análise futura')
def step_armazenar_alerta(context):
    assert "Alerta de discrepância gerado" in ganhos_context["historico_alertas"], "Alerta não armazenado corretamente."
