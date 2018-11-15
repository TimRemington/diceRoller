import matplotlib.pyplot as plt, mpld3

from flask import render_template, url_for, flash, redirect
from diceRoller import app, db, bcrypt
from diceRoller.forms import DiceRoller
from diceRoller.diceSim import Roll, RunStats

@app.route('/')
@app.route('/home')
def homepage():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/dice', methods=['GET', 'POST'])
def dice():
    form = DiceRoller()
    if form.validate_on_submit():
        num = int(form.rules.data)
        results = RunStats(form.trials.data, num, form.amount.data)
        flash('Dice Number: ' + str(results['Dice Number']), 'success')
        flash('Average: ' + str(results['Average']), 'success')
        flash('Standard Deviation: ' + str(results['Standard Deviation']), 'success')
        #plt.boxplot(results['Successes'])
        #mpld3.show()
    return render_template('dice.html', title='Dice Simulator', form=form)
