import os

from flask import Flask, render_template

from investing_parse import REPORT_DIR_PATH
from investing_parse.core.help_function import get_data_json
from investing_parse.core.parse_behave_json import parse_behave_json_report

app = Flask(__name__)


@app.route('/')
def main_page():
    try:
        behave_report = parse_behave_json_report(
            os.path.join(REPORT_DIR_PATH, 'behave.json'))
    except:
        behave_report = None
    try:
        pairs_company_divident = get_data_json(
            os.path.join(REPORT_DIR_PATH, 'dividend.json')).items()
    except:
        pairs_company_divident = None
    return render_template('main.html',
                           pairs=pairs_company_divident,
                           scenario=behave_report)


def run():
    app.run(debug=True)
