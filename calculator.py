from flask import Flask, render_template, request
from functions import Calc

app = Flask(__name__)
calc = Calc()

@app.route('/', methods=['GET', 'POST'])
@app.route('/calc', methods=['GET', 'POST'])
def Calculator():
    button_value = request.values.get('button')

    if (button_value == '=' or button_value == 'del' or button_value == 'clear'):
        calc.edit_operation(button_value)
    else:
        calc.get_operation(button_value)

    return render_template("calc.html", operation=calc.inputCurrent, last_operation=calc.get_last_of_list())

if __name__ == '__main__':
    app.run(debug=True)