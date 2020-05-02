import flask
import pandas as pd
import pickle

# Importando o modelo e a feature names:
with open('modelo/modelo_simples.pkl', 'rb') as file:
    modelo = pickle.load(file)
with open('modelo/features_simples.names', 'rb') as file:
    features_names = pickle.load(file)

app = flask.Flask(__name__, template_folder='templates')

@app.route('/', methods=["POST", "GET"])
def main():
    if flask.request.method == "GET":
        return flask.render_template('home.html')

    if flask.request.method == "POST":
        user_inputs = {
            'District': flask.request.form.get('District'),
            'Condo': flask.request.form.get('Condo'),
            'Size': flask.request.form.get('Area'),
            'Rooms': flask.request.form.get('Rooms'),
            'Toilets': flask.request.form.get('Toilets'),
            'Suites': flask.request.form.get('Suites'),
            'Parking': flask.request.form.get('Parking'),
            'Elevator': flask.request.form.get('Elevator'),
            'Furnished': flask.request.form.get('Furnished'),
            'Swimming Pool': flask.request.form.get('Swimming Pool'),
            'New': flask.request.form.get('New')
        }
        dados = pd.DataFrame(index=[0], columns=features_names)
        dados = dados.fillna(value=0)

        for i in user_inputs.items():
            if i[1] != None:
                dados[i[0]] = i[1]
            else:
                dados[i[0]] = 0
        df_lat_long = pd.read_csv('dataset\Bairros_LatLong.csv')
        dados.Latitude = df_lat_long[df_lat_long.District == user_inputs.get('District')].Latitude.values[0]
        dados.Longitude = df_lat_long[df_lat_long.District == user_inputs.get('District')].Longitude.values[0]
        dados.drop('District', axis=1, inplace=True)
        dados = dados.astype(float)
        y_pred = modelo.predict(dados)[0][0]

        print(user_inputs)
        return flask.render_template('home.html', valor_venda=y_pred)

if __name__ == '__main__':
    app.run(debug=True)