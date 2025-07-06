"""
Q-Rapid Data Collector
Script para coletar e atualizar métricas de qualidade do AgroMart
"""

import json
import datetime
import random
from pathlib import Path

class QRapidDataCollector:
    def __init__(self, data_file_path="docs/qrapid/data/metrics_data.json"):
        self.data_file = Path(data_file_path)
        self.ensure_data_file_exists()
    
    def ensure_data_file_exists(self):
        """Garante que o arquivo de dados existe"""
        if not self.data_file.exists():
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            initial_data = []
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump(initial_data, f, ensure_ascii=False, indent=2)
    
    def load_existing_data(self):
        """Carrega dados existentes"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def simulate_metrics_collection(self):
        """
        Simula a coleta de métricas - Em produção, substitua por coleta real
        """
        # Simula uma pequena melhoria nas métricas ao longo do tempo
        base_metrics = {
            "M1_completude_funcional": random.uniform(85, 95),
            "M2_sucesso_tarefas": random.uniform(88, 95),
            "M3_autonomia_usuario": random.uniform(80, 90),
            "M4_navegacao_sucesso": random.uniform(85, 95),
            "M5_compreensao_csa": random.uniform(83, 90),
            "M6_consistencia_dispositivos": random.uniform(87, 95),
            "M7_legibilidade_mensagens": random.uniform(35, 45),  # Crítico - da avaliação
            "M8_descoberta_carrossel": random.uniform(25, 35),    # Crítico - da avaliação
            "M9_compreensao_nomenclatura": random.uniform(55, 65), # Crítico - da avaliação
            "M10_reconhecimento_icones": random.uniform(45, 55),   # Crítico - da avaliação
            "M11_prevencao_erros": random.uniform(15, 25),         # Crítico - da avaliação
            "M7_clareza_visual": random.uniform(84, 92),           # Mantido para histórico
            "M8_recuperacao_erros": random.uniform(78, 88),        # Mantido para histórico
            "M9_tempo_aprendizado": random.uniform(12, 18)         # Mantido para histórico
        }
        
        return base_metrics
    
    def collect_real_metrics(self, use_evaluation_data=False):
        """
        Método para coletar métricas reais - implementar conforme necessário
        
        Args:
            use_evaluation_data (bool): Se True, usa valores baseados na avaliação específica
        """
        # TODO: Implementar coleta real de métricas
        # Exemplos de fontes:
        # - Google Analytics
        # - Logs do servidor
        # - Testes automatizados
        # - Feedback de usuários
        
        # Por enquanto, usa simulação ou dados da avaliação
        if use_evaluation_data:
            print("📊 Usando valores baseados na avaliação de usabilidade...")
            return self.define_metrics_based_on_evaluation()
        else:
            print("📊 Usando valores simulados...")
            return self.simulate_metrics_collection()
    
    def add_new_data_point(self, custom_date=None, use_evaluation_data=False):
        """
        Adiciona um novo ponto de dados
        
        Args:
            custom_date: Data customizada (opcional)
            use_evaluation_data (bool): Se True, usa valores baseados na avaliação específica
        """
        existing_data = self.load_existing_data()
        
        # Data atual ou customizada
        date = custom_date or datetime.date.today().isoformat()
        
        # Coleta métricas
        metrics = self.collect_real_metrics(use_evaluation_data)
        
        # Cria novo ponto de dados
        new_data_point = {
            "date": date,
            **metrics
        }
        
        # Adiciona aos dados existentes
        existing_data.append(new_data_point)
        
        # Mantém apenas os últimos 30 pontos de dados
        if len(existing_data) > 30:
            existing_data = existing_data[-30:]
        
        # Salva dados atualizados
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Dados atualizados para {date}")
        return new_data_point
    
    def generate_sample_data(self, days=30):
        """Gera dados de exemplo para demonstração"""
        data = []
        start_date = datetime.date.today() - datetime.timedelta(days=days)
        
        for i in range(days):
            current_date = start_date + datetime.timedelta(days=i)
            
            # Simula melhoria gradual ao longo do tempo
            improvement_factor = 1 + (i / days) * 0.1  # Melhoria de até 10%
            
            metrics = {
                "date": current_date.isoformat(),
                "M1_completude_funcional": min(95, 75 + (i * 0.5)),
                "M2_sucesso_tarefas": min(95, 85 + (i * 0.3)),
                "M3_autonomia_usuario": min(90, 75 + (i * 0.4)),
                "M4_navegacao_sucesso": min(95, 80 + (i * 0.4)),
                "M5_compreensao_csa": min(90, 78 + (i * 0.3)),
                "M6_consistencia_dispositivos": min(95, 82 + (i * 0.4)),
                "M7_clareza_visual": min(92, 79 + (i * 0.35)),
                "M8_recuperacao_erros": min(88, 73 + (i * 0.4)),
                "M9_tempo_aprendizado": max(10, 20 - (i * 0.2))
            }
            data.append(metrics)
        
        # Salva dados
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Gerados {days} dias de dados de exemplo")
        return data
    
    def get_latest_metrics(self):
        """Retorna as métricas mais recentes"""
        data = self.load_existing_data()
        if data:
            return data[-1]
        return None
    
    def generate_report(self):
        """Gera relatório das métricas atuais"""
        latest = self.get_latest_metrics()
        if not latest:
            print("❌ Nenhum dado disponível")
            return
        
        print("\n" + "="*50)
        print("📊 RELATÓRIO Q-RAPID - AGROMART")
        print("="*50)
        print(f"📅 Data: {latest['date']}")
        print("\n🔧 ADEQUAÇÃO FUNCIONAL:")
        print(f"   • Completude Funcional: {latest['M1_completude_funcional']:.1f}% (Meta: ≥85%)")
        print(f"   • Sucesso em Tarefas: {latest['M2_sucesso_tarefas']:.1f}% (Meta: ≥90%)")
        print(f"   • Autonomia do Usuário: {latest['M3_autonomia_usuario']:.1f}% (Meta: ≥80%)")
        
        print("\n👤 USABILIDADE:")
        print(f"   • Navegação Bem-sucedida: {latest['M4_navegacao_sucesso']:.1f}% (Meta: ≥90%)")
        print(f"   • Compreensão CSA: {latest['M5_compreensao_csa']:.1f}% (Meta: ≥85%)")
        print(f"   • Consistência Dispositivos: {latest['M6_consistencia_dispositivos']:.1f}% (Meta: ≥90%)")
        
        print("\n🔴 PROBLEMAS CRÍTICOS DA AVALIAÇÃO:")
        if 'M7_legibilidade_mensagens' in latest:
            print(f"   • Legibilidade Mensagens: {latest['M7_legibilidade_mensagens']:.1f}% (Meta: ≥90%)")
        if 'M8_descoberta_carrossel' in latest:
            print(f"   • Descoberta Carrossel: {latest['M8_descoberta_carrossel']:.1f}% (Meta: ≥85%)")
        if 'M9_compreensao_nomenclatura' in latest:
            print(f"   • Compreensão Nomenclatura: {latest['M9_compreensao_nomenclatura']:.1f}% (Meta: ≥95%)")
        if 'M10_reconhecimento_icones' in latest:
            print(f"   • Reconhecimento Ícones: {latest['M10_reconhecimento_icones']:.1f}% (Meta: ≥85%)")
        if 'M11_prevencao_erros' in latest:
            print(f"   • Prevenção de Erros: {latest['M11_prevencao_erros']:.1f}% (Meta: ≥80%)")
        
        print("\n📈 MÉTRICAS HISTÓRICAS:")
        if 'M7_clareza_visual' in latest:
            print(f"   • Clareza Visual: {latest['M7_clareza_visual']:.1f}% (Meta: ≥85%)")
        if 'M8_recuperacao_erros' in latest:
            print(f"   • Recuperação de Erros: {latest['M8_recuperacao_erros']:.1f}% (Meta: ≥80%)")
        if 'M9_tempo_aprendizado' in latest:
            print(f"   • Tempo de Aprendizado: {latest['M9_tempo_aprendizado']:.1f} min (Meta: ≤15 min)")
        print("="*50)
    
    def define_metrics_based_on_evaluation(self):
        """
        Define valores específicos baseados na avaliação de usabilidade realizada
        """
        # Valores baseados na sua avaliação específica
        evaluation_metrics = {
            "M1_completude_funcional": 78.0,  # Funcionalidades básicas implementadas
            "M2_sucesso_tarefas": 82.0,       # Algumas tarefas com problemas
            "M3_autonomia_usuario": 70.0,     # Problemas de usabilidade afetam autonomia
            "M4_navegacao_sucesso": 75.0,     # Navegação OK, mas com problemas
            "M5_compreensao_csa": 85.0,       # Busca de CSA bem estruturada
            "M6_consistencia_dispositivos": 88.0,  # Boa responsividade mobile
            
            # Métricas específicas baseadas nos problemas identificados:
            "M7_legibilidade_mensagens": 40.0,     # Fonte muito clara - CRÍTICO
            "M8_descoberta_carrossel": 30.0,       # Sem indicadores visuais - CRÍTICO  
            "M9_compreensao_nomenclatura": 60.0,   # Termos em inglês - PROBLEMA
            "M10_reconhecimento_icones": 50.0,     # Ícones ambíguos - PROBLEMA
            "M11_prevencao_erros": 20.0,           # Não identificados - CRÍTICO
            "M12_contraste_visual": 45.0,          # Cores semelhantes - CRÍTICO
            "M13_tempo_aprendizado": 25.0           # Afetado pelos problemas
        }
        
        return evaluation_metrics

def main():
    """Função principal para execução do script"""
    collector = QRapidDataCollector()
    
    print("🚀 Q-Rapid Data Collector - AgroMart")
    print("="*50)
    print("Escolha uma opção:")
    print("1. Gerar dados de exemplo (30 dias)")
    print("2. Adicionar novo ponto com dados simulados")
    print("3. Adicionar novo ponto com dados da AVALIAÇÃO")
    print("4. Visualizar relatório atual")
    print("5. Sair")
    
    choice = input("\nOpção: ")
    
    if choice == "1":
        collector.generate_sample_data()
        print("✅ Dados de exemplo gerados!")
        
    elif choice == "2":
        new_data = collector.add_new_data_point(use_evaluation_data=False)
        print("✅ Novo ponto de dados adicionado com valores simulados!")
        
    elif choice == "3":
        new_data = collector.add_new_data_point(use_evaluation_data=True)
        print("✅ Novo ponto de dados adicionado com valores da avaliação!")
        print("\n🚨 ATENÇÃO: Valores críticos baseados nos problemas identificados!")
        
    elif choice == "4":
        collector.generate_report()
        
    elif choice == "5":
        print("👋 Até logo!")
        return
        
    else:
        print("❌ Opção inválida!")
        return
    
    # Pergunta se quer visualizar o dashboard
    if choice in ["1", "2", "3"]:
        view_dashboard = input("\n🌐 Deseja abrir o dashboard? (s/n): ")
        if view_dashboard.lower() == 's':
            import webbrowser
            import os
            dashboard_path = os.path.abspath("docs/qrapid/dashboard.html")
            webbrowser.open(f"file://{dashboard_path}")
            print("🌐 Dashboard aberto no navegador!")
    
    if choice == "1":
        collector.generate_sample_data(30)
    elif choice == "2":
        collector.add_new_data_point()
    elif choice == "3":
        collector.generate_report()
    elif choice == "4":
        print("👋 Até logo!")
    else:
        print("❌ Opção inválida")

if __name__ == "__main__":
    main()
