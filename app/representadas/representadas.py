from flask import Blueprint, render_template

representadas_blueprint = Blueprint('representadas', __name__, template_folder='templates')


@representadas_blueprint.route('/representadas', methods=['GET','POST'])
def reresentadas():
    return render_template('representadas.html')
