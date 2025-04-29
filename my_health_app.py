from flask import Flask, render_template, request, redirect, url_for, flash
from models import db, HealthMetricReading
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///vitallog.db'
app.secret_key = 'your_secret_key'

db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create', methods=['GET', 'POST'])
def create_metric():
    if request.method == 'POST':
        metric_type = request.form.get('metric_type')
        value = request.form.get('value')
        unit = request.form.get('unit')
        recorded_at = datetime.now()

        # Validation: Allow numeric or special formats like "120/80"
        if metric_type.lower() == "blood pressure" and "/" not in value:
            flash('Blood pressure must be in the format "120/80".')
            return redirect(url_for('create_metric'))
        elif metric_type.lower() != "blood pressure" and not value.replace('.', '', 1).isdigit():
            flash('The value must be a number.')
            return redirect(url_for('create_metric'))

        metric = HealthMetricReading(
            user_id=1,
            metric_type=metric_type,
            value=value,  # Store as a string
            unit=unit,
            recorded_at=recorded_at
        )
        db.session.add(metric)
        db.session.commit()
        flash('Metric added successfully!')
        return redirect(url_for('index'))
    return render_template('create.html')
@app.route('/metrics')
def view_metrics():
    from datetime import datetime

    start_date = request.args.get('start_date')
    end_date = request.args.get('end_date')

    metrics = HealthMetricReading.query
    if start_date:
        metrics = metrics.filter(HealthMetricReading.recorded_at >= datetime.strptime(start_date, '%Y-%m-%d'))
    if end_date:
        metrics = metrics.filter(HealthMetricReading.recorded_at <= datetime.strptime(end_date, '%Y-%m-%d'))

    metrics = metrics.all()
    metrics = HealthMetricReading.query.all()
    assert isinstance(metrics, object)
    return render_template('metrics.html', metrics=metrics)


@app.route('/update/<int:metric_id>', methods=['GET', 'POST'])
def update_metric(metric_id):
    metric = HealthMetricReading.query.get(metric_id)
    if request.method == 'POST':
        metric.value = float(request.form.get('value'))
        metric.unit = request.form.get('unit')
        db.session.commit()
        flash('Metric updated successfully!')
        return redirect(url_for('view_metrics'))
    return render_template('update.html', metric=metric)

@app.route('/delete/<int:metric_id>')
def delete_metric(metric_id):
    metric = HealthMetricReading.query.get(metric_id)
    db.session.delete(metric)
    db.session.commit()
    flash('Metric deleted successfully!')
    return redirect(url_for('view_metrics'))
import matplotlib.pyplot as plt
from io import BytesIO
import base64

@app.route('/metrics_chart')
def metrics_chart():
    # Fetch metrics data from the database
    metrics = HealthMetricReading.query.order_by(HealthMetricReading.recorded_at).all()

    # Extract dates and values
    dates = [metric.recorded_at for metric in metrics]
    values = [float(metric.value) for metric in metrics if metric.value.replace('.', '', 1).isdigit()]

    # Plot the graph
    plt.figure(figsize=(10, 5))
    plt.plot(dates, values, marker='o', color='blue')
    plt.title('Metrics Over Time')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.grid(True)
    plt.tight_layout()
    print(dates)
    print(values)
    # Save the graph to a BytesIO object
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    with open('output_graph.png', 'wb') as f:
        f.write(img.getvalue())  # Save the graph locally to verify it
        metrics = HealthMetricReading.query.order_by(HealthMetricReading.recorded_at).all()
        for metric in metrics:
            print(metric.recorded_at, metric.value)
    # Encode the graph image as a Base64 string
    graph_url = base64.b64encode(img.getvalue()).decode()

    return render_template('metrics_chart.html', graph_url=graph_url)

import csv
from flask import Response

@app.route('/export_metrics')
def export_metrics():
    metrics = HealthMetricReading.query.all()
    output = []
    output.append(['Metric Type', 'Value', 'Unit', 'Date'])

    for m in metrics:
        output.append([m.metric_type, m.value, m.unit, m.recorded_at])

    # Create CSV response
    csv_output = "\n".join([",".join(map(str, row)) for row in output])
    return Response(csv_output, mimetype='text/csv',
                    headers={'Content-Disposition': 'attachment;filename=metrics.csv'})
if __name__ == '__main__':
    app.run(debug=True)