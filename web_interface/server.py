from flask import Flask, render_template
from core.help_function import get_data_json
from core.parse_behave_json import parse_behave_json_report
import os

try:
    behave_report = parse_behave_json_report(os.path.join(os.getcwd(), 'report', 'behave.json'))
except:
    behave_report = None
try:
    pairs_company_divident = get_data_json(os.path.join(os.getcwd(), 'report', 'dividend.json')).items()
except:
    pairs_company_divident = None
app = Flask(__name__)
print(os.getcwd())


@app.route('/')
def main_page():
    return render_template('main.html', pairs=pairs_company_divident, scenario=behave_report)


def run():
    app.run(debug=True)
