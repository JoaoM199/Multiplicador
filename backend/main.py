from flask import Flask

app = Flask(__name__)

# Variáveis
multiplicador = 1
nrep = 10

@app.route("/")
def calcular():
    repetir = 0
    colect = []
    while repetir <= nrep:
        resultado = multiplicador * repetir

        colect.append("{} * {} = {}".format(multiplicador, repetir, resultado))
        repetir = repetir + 1
    return colect
calcular()

if __name__ == "__main__":
    app.run()