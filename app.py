from flask import Flask, render_template, request
import dal.dalImpl as db
from modele.pingouins import Pingouin

app = Flask(__name__)


@app.route('/')
def accueil():
    pingouins = db.get_all_pingouins()
    return render_template('accueil.html', individus=pingouins)


@app.route('/update', methods=['GET', 'POST'])
def modifier():
    if request.method == 'GET':
        id = request.args['id']
        pingouin = db.get_pingouin(id)
        return render_template('modification.html', pingouin=pingouin)
    else:
        print(request.form.to_dict())
        db.update_pingouin(Pingouin(request.form['idPingouin'], request.form['ile'], request.form['espece'],
                                    request.form['longueur_bec'],
                                    request.form['profondeur_bec'], request.form['longueur_nageoire'],
                                    request.form['poids'],
                                    request.form['sexe'], request.form['annee_naissance']))
        pingouins = db.get_all_pingouins()
        return render_template('accueil.html', individus=pingouins,
                               message='Le pingouin n°={} a été correctement mis à jour.'.format(
                                   request.form['idPingouin']))


@app.route('/delete')
def supprimer():
    id = request.args['id']
    db.delete_pingouin(id)
    pingouins = db.get_all_pingouins()
    return render_template('accueil.html', individus=pingouins,
                           message='Le pingouin n°={} a été correctement supprimé.'.format(id))


app.run()
