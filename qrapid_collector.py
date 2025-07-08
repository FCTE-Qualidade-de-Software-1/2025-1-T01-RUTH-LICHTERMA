"""
Q-Rapid Data Collector
Script para coletar e atualizar métricas de qualidade do AgroMart
"""

import json
import datetime
from pathlib import Path
import webbrowser
import os

class QRapidDataCollector:
    def __init__(self, data_file_path="docs/qrapid/data/metrics_data.json"):
        self.data_file = Path(data_file_path)
        self.ensure_data_file_exists()
    
    def ensure_data_file_exists(self):
        """Garante que o arquivo de dados existe"""
        if not self.data_file.exists():
            self.data_file.parent.mkdir(parents=True, exist_ok=True)
            with open(self.data_file, 'w', encoding='utf-8') as f:
                json.dump([], f, ensure_ascii=False, indent=2)
    
    def load_existing_data(self):
        """Carrega dados existentes"""
        try:
            with open(self.data_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return []
    
    def simulate_metrics_collection(self):
        """
        Simula a coleta de métricas
        """
        import random
        base_metrics = {
            "M1_completude_funcional": random.uniform(60, 85),
            "M2_precisao_computacional": random.uniform(0, 50),
            "M3_apropriacao_funcional": random.uniform(85, 100),
            "M4_clareza_mensagens": random.uniform(9, 40),
            "M5_consistencia_operacional": random.uniform(30, 70),
            "M6_documentacao_usuario": random.uniform(50, 80),
            "M7_prevencao_erros": random.uniform(85, 100),
        }
        return base_metrics
            
    def define_metrics_based_on_evaluation(self):
        """
        Define valores reais da avaliação do laudo fornecido
        """
        evaluation_metrics = {
            "M1_completude_funcional": 60.0,
            "M2_precisao_computacional": 0.0,
            "M3_apropriacao_funcional": 100.0,
            "M4_clareza_mensagens": 9.09,
            "M5_consistencia_operacional": 60.0,
            "M6_documentacao_usuario": 60.0,
            "M7_prevencao_erros": 100.0
        }
        return evaluation_metrics
    
    def collect_real_metrics(self, use_evaluation_data=False):
        """
        Coleta métricas reais ou simuladas
        """
        if use_evaluation_data:
            print("📊 Coletando métricas com base na AVALIAÇÃO REAL...")
            return self.define_metrics_based_on_evaluation()
        else:
            print("📊 Coletando métricas simuladas...")
            return self.simulate_metrics_collection()
    
    def add_new_data_point(self, custom_date=None, use_evaluation_data=False):
        """
        Adiciona um novo ponto de dados
        """
        existing_data = self.load_existing_data()
        date = custom_date or datetime.date.today().isoformat()
        metrics = self.collect_real_metrics(use_evaluation_data)
        new_data_point = {
            "date": date,
            **metrics
        }
        existing_data.append(new_data_point)

        # manter somente últimos 30
        if len(existing_data) > 30:
            existing_data = existing_data[-30:]

        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Dados atualizados para {date}")
        return new_data_point
    
    def get_latest_metrics(self):
        data = self.load_existing_data()
        if data:
            return data[-1]
        return None
    
    def generate_report(self):
        """
        Gera relatório formatado
        """
        latest = self.get_latest_metrics()
        if not latest:
            print("❌ Nenhum dado disponível")
            return
        
        print("\n" + "="*50)
        print("📊 RELATÓRIO Q-RAPID - AGROMART")
        print("="*50)
        print(f"📅 Data: {latest['date']}")
        print("\n🔧 ADEQUAÇÃO FUNCIONAL:")
        print(f"   • Completude Funcional (M1): {latest.get('M1_completude_funcional', 0):.1f}% (Meta: ≥85%)")
        print(f"   • Precisão Computacional (M2): {latest.get('M2_precisao_computacional', 0):.1f}% (Meta: =100%)")
        print(f"   • Apropriação Funcional (M3): {latest.get('M3_apropriacao_funcional', 0):.1f}% (Meta: ≥85%)")

        print("\n👤 USABILIDADE:")
        print(f"   • Clareza das Mensagens (M4): {latest.get('M4_clareza_mensagens', 0):.1f}% (Meta: ≥85%)")
        print(f"   • Consistência Operacional (M5): {latest.get('M5_consistencia_operacional', 0):.1f}% (Meta: ≤10%)")
        print(f"   • Documentação do Usuário (M6): {latest.get('M6_documentacao_usuario', 0):.1f}% (Meta: ≥85%)")
        print(f"   • Prevenção de Erros (M7): {latest.get('M7_prevencao_erros', 0):.1f}% (Meta: ≥85%)")
        
        print("="*50)

    def generate_sample_data(self, days=30):
        """
        Gera dados fictícios
        """
        data = []
        start_date = datetime.date.today() - datetime.timedelta(days=days)

        for i in range(days):
            current_date = start_date + datetime.timedelta(days=i)
            metrics = {
                "date": current_date.isoformat(),
                "M1_completude_funcional": min(85, 60 + i * 0.5),
                "M2_precisao_computacional": min(100, 0 + i * 2.0),
                "M3_apropriacao_funcional": max(85, 100 - i * 0.2),
                "M4_clareza_mensagens": min(85, 9 + i * 1.5),
                "M5_consistencia_operacional": max(10, 60 - i * 1.0),
                "M6_documentacao_usuario": min(85, 60 + i * 0.8),
                "M7_prevencao_erros": max(85, 100 - i * 0.1)
            }
            data.append(metrics)
        
        with open(self.data_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"✅ Gerados {days} dias de dados de exemplo")
        return data
    

def main():
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
    elif choice == "2":
        collector.add_new_data_point(use_evaluation_data=False)
    elif choice == "3":
        collector.add_new_data_point(use_evaluation_data=True)
    elif choice == "4":
        collector.generate_report()
    elif choice == "5":
        print("👋 Até logo!")
        return
    else:
        print("❌ Opção inválida.")
        return
    
    # Pergunta se quer abrir o dashboard
    if choice in ["1", "2", "3"]:
        view_dashboard = input("\n🌐 Deseja abrir o dashboard? (s/n): ")
        if view_dashboard.lower() == 's':
            dashboard_path = os.path.abspath("docs/qrapid/dashboard_fixed.html")
            webbrowser.open(f"file://{dashboard_path}")
            print("🌐 Dashboard aberto no navegador!")

if __name__ == "__main__":
    main()
