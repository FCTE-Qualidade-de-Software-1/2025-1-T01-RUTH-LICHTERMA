# Q-Rapid Implementation Guide

## Resumo Executivo

Este guia fornece **todos os passos necessários** para implementar e usar o Q-Rapid.

### Estrutura de Arquivos
```
docs/qrapid/
├── dashboard.html              #  Dashboard interativo principal
├── qrapid.md                   #  Documentação da metodologia
├── metricas.md                 #  Definições das métricas
└── data/
    └── metrics_data.json       #  Dados das métricas

qrapid_collector.py             #  Script para coletar dados
```

###  Dashboard Criado
- **9 métricas** de qualidade monitoradas
- **3 gráficos interativos** (Adequação Funcional, Usabilidade, Evolução Temporal)
- **Cards de status** com alertas visuais
- **Design responsivo** para mobile e desktop

##  Sequência de Passos para Usar

### Passo 1: Visualizar o Dashboard
```bash
# Método 1: Abrir no navegador
# Navegue até: docs/qrapid/dashboard.html e abra no navegador

# Método 2: Via VS Code
# Clique com botão direito em dashboard.html > Open with Live Server
```

### Passo 2: Gerar Dados de Exemplo
```bash
# Execute o script Python
python qrapid_collector.py

# Escolha opção 1: "Gerar dados de exemplo (30 dias)"
```

### Passo 3: Visualizar no MkDocs
```bash
# Servir a documentação localmente
mkdocs serve

# Acesse: http://localhost:8000
# Navegue para: Q-Rapid > Dashboard
```

### Passo 4: Personalizar as Métricas
1. **Edite as metas** em `docs/qrapid/metricas.md`
2. **Ajuste os dados** em `docs/qrapid/data/metrics_data.json`
3. **Customize o visual** no `docs/qrapid/dashboard.html`

##  Métricas Implementadas

###  Adequação Funcional (3 métricas)
| Métrica | Descrição | Meta | Status Atual |
|---------|-----------|------|--------------|
| M1 | Completude Funcional | ≥85% | 🟢 87.5% |
| M2 | Sucesso em Tarefas | ≥90% | 🟢 92.0% |
| M3 | Autonomia do Usuário | ≥80% | 🟢 83.0% |

###  Usabilidade (6 métricas)
| Métrica | Descrição | Meta | Status Atual |
|---------|-----------|------|--------------|
| M4 | Navegação Bem-sucedida | ≥90% | 🟡 89.5% |
| M5 | Compreensão CSA | ≥85% | 🟢 86.0% |
| M6 | Consistência Dispositivos | ≥90% | 🟢 91.0% |
| M7 | Clareza Visual | ≥85% | 🟢 88.0% |
| M8 | Recuperação de Erros | ≥80% | 🟢 82.5% |
| M9 | Tempo de Aprendizado | ≤15 min | 🟢 14.2 min |

##  Como Coletar Dados Reais

### Para substituir dados simulados:

1. **Edite o arquivo** `qrapid_collector.py`
2. **Substitua a função** `collect_real_metrics()`:

```python
def collect_real_metrics(self):
    """Coleta métricas reais do sistema"""
    
    # Exemplo: Google Analytics
    analytics_data = get_analytics_data()
    
    # Exemplo: Logs do servidor
    server_logs = parse_server_logs()
    
    # Exemplo: Testes automatizados
    test_results = run_automated_tests()
    
    return {
        "M1_completude_funcional": calculate_functional_completeness(),
        "M2_sucesso_tarefas": analytics_data.success_rate,
        # ... outras métricas
    }
```

##  Automação

### Script Automático de Coleta
```bash
# Adicionar novo ponto de dados diariamente
python qrapid_collector.py
# Escolha opção 2: "Adicionar novo ponto de dados"

# Ou automatize via cron/task scheduler:
# Diário às 9h: python qrapid_collector.py --auto-collect
```

### Integração com CI/CD
```yaml
# .github/workflows/qrapid.yml
name: Q-Rapid Data Collection
on:
  schedule:
    - cron: '0 9 * * *'  # Diário às 9h
jobs:
  collect-metrics:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Collect Q-Rapid metrics
        run: python qrapid_collector.py --auto-collect
```

##  Próximos Passos

### Nível Básico (Já implementado)
- ✅ Dashboard funcional
- ✅ 9 métricas definidas
- ✅ Visualizações interativas
- ✅ Dados simulados

### Nível Intermediário
- [ ] Conectar com dados reais do AgroMart
- [ ] Implementar alertas automáticos
- [ ] Adicionar histórico de 6 meses
- [ ] Criar relatórios PDF automáticos

### Nível Avançado
- [ ] Machine Learning para previsões
- [ ] Integração com Slack/Teams
- [ ] API REST para métricas
- [ ] Dashboard em tempo real (WebSockets)

## Solução de Problemas

### Dashboard não carrega
```bash
# Verificar se os arquivos existem
ls docs/qrapid/
ls docs/qrapid/data/

# Verificar JSON válido
python -m json.tool docs/qrapid/data/metrics_data.json
```

### MkDocs não encontra os arquivos
```bash
# Verificar navegação no mkdocs.yml
cat mkdocs.yml | grep -A 10 "Q-Rapid"

# Reconstruir site
mkdocs build --clean
```

### Script Python com erro
```bash
# Instalar dependências se necessário
pip install json datetime pathlib

# Executar com debug
python -v qrapid_collector.py
```

##  Comandos Rápidos

```bash
# Visualizar dashboard
start docs/qrapid/dashboard.html  # Windows
open docs/qrapid/dashboard.html   # Mac
xdg-open docs/qrapid/dashboard.html # Linux

# Servir MkDocs
mkdocs serve

# Coletar dados
python qrapid_collector.py

# Ver relatório atual
python qrapid_collector.py
# Escolha opção 3
```


