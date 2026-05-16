from flask import Flask, request, redirect

app = Flask(__name__)

@app.before_request
def routing():
    return redirect("https://www.bashie.dev/", code=301)

if __name__ == '__main__':
    # This is used when running locally only. 
    app.run(host='127.0.0.1', port=8080, debug=True)