from flask import Flask, render_template, jsonify
import json
from datetime import datetime, timedelta
import random

app = Flask(__name__)

# Sample data for the dashboard
def generate_sample_data():
    # Financial metrics
    metrics = {
        'total_lucro': 12600,
        'total_perda': -4250,
        'total_operacoes': 350,
        'total_operacoes_dia': 15,
        'total_lucro_dia': 1200,
        'total_perda_dia': -300,
        'operacoes_win': 220,
        'operacoes_loss': 130
    }
    
    # Chart data for years (2020-2025)
    anos_data = {
        'labels': ['2020', '2021', '2022', '2023', '2024', '2025'],
        'data': [1000, 2500, 4200, 6800, 9200, 11500]
    }
    
    # Chart data for months
    meses_data = {
        'labels': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov'],
        'data': [3500, 2800, 4200, 3800, 5200, 4600, 3900, 4100, 4800, 5100, 4900]
    }
    
    # Chart data for days
    dias_data = {
        'labels': ['Seg', 'Ter', 'Qua', 'Qui', 'Sex', 'Sáb', 'Dom'],
        'data': [1000, 600, 1500, 800, 1100, 500, 1200]
    }
    
    # Chart data for last 24h
    horas_data = {
        'labels': ['Seg', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Nov'],
        'data': [250, 180, 220, 190, 160, 300, 200, 500, 180, 120]
    }
    
    # Trading operations table data
    operations = []
    symbols = ['BTCUSDT', 'ETHUSDT', 'ADAUSDT', 'DOTUSDT']
    types = ['Long', 'Short']
    results = ['Win', 'Loss']
    
    for i in range(15):
        op = {
            'data': '22/04/2024',
            'symbol': random.choice(symbols),
            'tipo': random.choice(types),
            'resultado': random.choice(results),
            'entrada': round(random.uniform(100, 2000), 3),
            'fechamento': round(random.uniform(100, 2000), 3),
            'pnl': round(random.uniform(-100, 100), 2),
            'pnl_percent': round(random.uniform(-1, 1), 2),
            'capital': round(random.uniform(1000, 120000), 3),
            'alavancagem': random.choice([20, 50, 100])
        }
        operations.append(op)
    
    return {
        'metrics': metrics,
        'charts': {
            'anos': anos_data,
            'meses': meses_data,
            'dias': dias_data,
            'horas': horas_data
        },
        'operations': operations
    }

@app.route('/')
def dashboard():
    data = generate_sample_data()
    return render_template('dashboard.html', data=data)

@app.route('/api/data')
def api_data():
    data = generate_sample_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
