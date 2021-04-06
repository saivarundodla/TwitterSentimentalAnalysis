from flask import Flask, request, render_template

from TwitterClient import TwitterClient

app = Flask(__name__, template_folder="static")


@app.route('/')
def success():
    return render_template("index.html")


@app.route('/search', methods=['POST', 'GET'])
def search():
    print(f"Method called {request.method} {request.form}")
    query = request.form['query']
    # query = "trump"
    count = 200
    print(f"Query {query}")
    twitterclientObj = TwitterClient()
    jsonoutput = twitterclientObj.main(query, count)
    jsonoutput["query"] = query
    return render_template('result.html', title="page", data=jsonoutput)


if __name__ == '__main__':
    app.run(debug=True)
