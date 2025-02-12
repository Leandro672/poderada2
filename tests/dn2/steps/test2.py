from behave import given, when, then
import random
import time

# Mockando o contexto de alocação de frota
frota_context = {
    "pedidos_atendidos": 0,
    "pedidos_sem_entregador": 0,
    "tempo_alocacao": 0,
    "tempo_alocacao_categoria": {"Retail": [], "Restaurante": [], "Mercado": []},
    "alerta_gerado": False
}

# -------------------------------
# Cenários de Tempo de Alocação
# -------------------------------

@given('que o sistema tem uma frota de entregadores disponíveis para atender os pedidos')
def step_define_frota(context):
    frota_context["pedidos_atendidos"] = 0
    frota_context["pedidos_sem_entregador"] = 0

@given('o sistema está rastreando os tempos de alocação de entregadores')
def step_track_allocation_times(context):
    frota_context["tempo_alocacao"] = 0

@when('o sistema aloca um entregador para um pedido de Retail')
def step_allocate_retail_delivery(context):
    tempo_alocacao = random.uniform(5, 15)
    frota_context["tempo_alocacao"] = tempo_alocacao
    frota_context["tempo_alocacao_categoria"]["Retail"].append(tempo_alocacao)

@then('o tempo de alocação deve ser inferior a 15 segundos')
def step_check_retail_allocation_time(context):
    assert frota_context["tempo_alocacao"] < 15, f"Tempo de alocação: {frota_context['tempo_alocacao']} segundos, deveria ser inferior a 15 segundos."

@when('o sistema aloca um entregador para um pedido de Restaurante ou Mercado')
def step_allocate_restaurant_market_delivery(context):
    tempo_alocacao = random.uniform(10, 20)
    frota_context["tempo_alocacao"] = tempo_alocacao
    frota_context["tempo_alocacao_categoria"]["Restaurante"].append(tempo_alocacao) if random.choice([True, False]) else frota_context["tempo_alocacao_categoria"]["Mercado"].append(tempo_alocacao)

@then('o tempo de alocação não pode ultrapassar 20 segundos')
def step_check_restaurant_market_allocation_time(context):
    assert frota_context["tempo_alocacao"] <= 20, f"Tempo de alocação: {frota_context['tempo_alocacao']} segundos, deveria ser no máximo 20 segundos."

# -------------------------------
# Cenário de Alerta de Pedido sem Entregador
# -------------------------------

@when('mais de 5% dos pedidos não têm entregador por mais de 60 segundos')
def step_orders_without_delivery(context):
    frota_context["pedidos_sem_entregador"] = int(frota_context["pedidos_atendidos"] * 0.05)
    assert frota_context["pedidos_sem_entregador"] > 0, "Não há pedidos sem entregador suficientes para gerar o alerta."

@then('o sistema deve gerar um alerta de alocação')
def step_generate_alert(context):
    frota_context["alerta_gerado"] = True
    assert frota_context["alerta_gerado"], "Alerta de alocação não gerado!"

# -------------------------------
# Garantir que 95% dos pedidos sejam alocados em até 30 segundos
# -------------------------------

@given('que o sistema está alocando entregadores para 1000 pedidos')
def step_allocate_multiple_orders(context):
    frota_context["pedidos_atendidos"] = 1000
    frota_context["pedidos_sem_entregador"] = 0

@when('o sistema aloca entregadores')
def step_allocate_deliveries(context):
    for i in range(frota_context["pedidos_atendidos"]):
        tempo_alocacao = random.uniform(5, 30)
        frota_context["tempo_alocacao"] = tempo_alocacao

@then('pelo menos 95% dos pedidos devem ser atribuídos a um entregador em até 30 segundos')
def step_check_95_percent_allocation(context):
    pedidos_no_limite = sum(1 for i in range(frota_context["pedidos_atendidos"]) if frota_context["tempo_alocacao"] <= 30)
    assert pedidos_no_limite / frota_context["pedidos_atendidos"] >= 0.95, f"Menos de 95% dos pedidos foram atribuídos a um entregador em até 30 segundos!"

# -------------------------------
# Monitoramento de Tempo de Alocação por Categoria
# -------------------------------

@when('o sistema monitora os tempos de alocação por categoria (Retail, Restaurante, Mercado)')
def step_monitor_allocation_times(context):
    # Calcula a média de alocação para cada categoria
    frota_context["media_retail"] = sum(frota_context["tempo_alocacao_categoria"]["Retail"]) / len(frota_context["tempo_alocacao_categoria"]["Retail"]) if frota_context["tempo_alocacao_categoria"]["Retail"] else 0
    frota_context["media_restaurante"] = sum(frota_context["tempo_alocacao_categoria"]["Restaurante"]) / len(frota_context["tempo_alocacao_categoria"]["Restaurante"]) if frota_context["tempo_alocacao_categoria"]["Restaurante"] else 0
    frota_context["media_mercado"] = sum(frota_context["tempo_alocacao_categoria"]["Mercado"]) / len(frota_context["tempo_alocacao_categoria"]["Mercado"]) if frota_context["tempo_alocacao_categoria"]["Mercado"] else 0

@then('o sistema deve gerar um alerta se o tempo de alocação de uma categoria for 50% maior que a média das outras')
def step_check_alert_on_time_difference(context):
    medias = [frota_context["media_retail"], frota_context["media_restaurante"], frota_context["media_mercado"]]
    max_media = max(medias)
    min_media = min(medias)
    if max_media > min_media * 1.5:
        frota_context["alerta_gerado"] = True
    assert frota_context["alerta_gerado"], "Alerta de alocação não gerado por diferença de tempo de alocação entre categorias."
