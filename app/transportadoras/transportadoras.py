from flask import Blueprint, render_template#, request, flash, redirect, url_for
#from app import db
#from app.model.tables import Transportadoras


transportadora_blueprint = Blueprint('transportadoras', __name__, template_folder='templates')


# CADASTRO DE TRANSPORTADORA
@transportadora_blueprint.route('/transportadoras', methods=['GET', 'POST'])
def transportadora():
    #my_data = db.session.query(Transportadoras).all()
    return render_template('transportadoras.html')

'''
    my_data = db.session.query(Transportadoras).all()
    if request.method == "POST":
        transportadora = request.form['transportadora']
        cidade = request.form['cidade']
        estado = request.form['estado']
        telefone = request.form['telefone']
        my_data = transportadora(Transportadora=transportadora, Cidade=cidade, Estado=estado, Telefone=telefone)
        db.session.add(my_data)
        db.session.commit()
        flash("Dados inseridos com sucesso!")
        return redirect(url_for('transportadoras.transportadoras'))
'''


'''
# ATUALIZAÇÃO DO CADASTRO DA TRANSPORTADORA
@transportadora_blueprint.route('/updatetransp', methods=['POST', 'GET'])
def updatetransp():
    if request.method == "POST":
        my_data = Transportadoras.query.get(request.form.get('idtransportadora'))
        my_data.idtransportadora = request.form['idtransportadora']
        my_data.Transportadora = request.form['transportadora']
        my_data.Cidade = request.form['cidade']
        my_data.Estado = request.form['estado']
        my_data.Telefone = request.form['telefone']
        db.session.commit()
        flash("Dados alterados com sucesso!")
        return redirect(url_for('transportadoras.transportadoras', listatransportadoras=my_data))
    return render_template('transportadoras.html')


# DELETAR A TRANSPORTADORA
@transportadora_blueprint.route('/deletetransp/<string:idtransportadora>', methods=['GET'])
def deletetransp(idtransportadora):
    my_data = Transportadoras.query.get(idtransportadora)
    db.session.delete(my_data)
    db.session.commit()
    flash("Item deletado com sucesso!")
    return redirect(url_for('transportadoras.transportadora'))





'''