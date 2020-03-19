from flask import Flask,render_template
app = Flask (__name__)


@app.route("/")
def home():

    return  render_template("index.html")

@app.route("/archviz")
def archviz():

    return  render_template("archviz.html")

@app.route("/dynamo")
def dynamo():

    return  render_template("dynamo.html")

@app.route("/revitplugin")
def revitplugin():

    return  render_template("revitplugin.html")


@app.route("/web3d")
def web3d():

    return  render_template("web3d.html")


if __name__ == '__main__':

    app.run(debug=True)

