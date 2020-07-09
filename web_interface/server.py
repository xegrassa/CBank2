from flask import Flask, render_template
import json


def get_data_json(path: str):
    with open(path) as f:
        data = json.load(f)
    return data


pairs_company_divident = get_data_json('report\dividend.json')

app = Flask(__name__)


@app.route('/')
def hello_world():
    print(pairs_company_divident, type(pairs_company_divident))
    print(pairs_company_divident.items())
    return render_template('main.html', pairs=pairs_company_divident.items())


if __name__ == '__main__':
    app.run(debug=True)
