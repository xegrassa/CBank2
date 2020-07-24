from flask import Flask, render_template
from core.help_function import get_data_json

pairs_company_divident = get_data_json(r'C:\Users\Admin\PycharmProjects\BANK_zadanie_2\report\dividend.json')
app = Flask(__name__)


@app.route('/')
def main_page():
    print(pairs_company_divident, type(pairs_company_divident))
    print(pairs_company_divident.items())
    return render_template('main.html', pairs=pairs_company_divident.items())


def run():
    app.run(debug=True)
