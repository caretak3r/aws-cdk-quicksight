from flask import Flask, render_template
import aws_resources

app = Flask(__name__)

@app.route('/')
def home():
    data = aws_resources.get_aws_resources()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
