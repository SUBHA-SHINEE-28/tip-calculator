from flask import Flask, request, render_template
from waitress import serve

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    amt = int(request.form['amt'])
    tip_per = int(request.form['tip_per'])
    no_of_per = int(request.form['no_of_per'])
    tip_amt = round(amt*(tip_per/100))
    tip_per_person = round(tip_amt/no_of_per)
    tot_amt = round(amt+tip_amt)
    amt_per_person = round(tot_amt/no_of_per)
    if (no_of_per > 1):
        return render_template(
            "tip_for_many_person.html",
            amount=amt,
            tip_percentage=tip_per,
            no_of_per=no_of_per,
            tip_amount=tip_amt,
            total_amount=tot_amt,
            per_person=tip_per_person,
            total_per_person=amt_per_person
        )
    else:
        return render_template(
            "tip_for_one_person.html",
            amount=amt,
            tip_percentage=tip_per,
            no_of_per=no_of_per,
            tip_amount=tip_amt,
            total_amount=tot_amt,
        )


if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)
