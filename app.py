from flask import Flask, render_template, request, redirect, url_for
import pdfkit
import os
from datetime import datetime

app = Flask(__name__)

REPORTS_DIR = 'reports'
os.makedirs(REPORTS_DIR, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create_report/<int:client_id>', methods=['GET', 'POST'])
def create_report(client_id):
    if request.method == 'POST':
        title = request.form.get('title')
        content = request.form.get('content')
        date = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        pdf_path = f"{REPORTS_DIR}/report_{client_id}_{date}.pdf"
        rendered = render_template('report_template.html', title=title, content=content)
        pdfkit.from_string(rendered, pdf_path)
        return redirect(url_for('index'))
    return render_template('create_report.html', client_id=client_id)

if __name__ == '__main__':
    app.run()
