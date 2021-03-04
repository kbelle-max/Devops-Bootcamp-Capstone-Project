from flask import Flask, render_template
from elasticapm.contrib.flask import ElasticAPM
app = Flask(__name__)
 
@app.route("/")
def main():
    return render_template('index.html')
# initialize using environment variables

apm = ElasticAPM(app)
app.config['ELASTIC_APM'] = {
  # Set the required service name. Allowed characters:
  # a-z, A-Z, 0-9, -, _, and space
  'SERVICE_NAME': 'brown-fox-deployment',
  # Set the service environment
  'ENVIRONMENT': 'production',
} 
if __name__ == "__main__":
    apm = ElasticAPM(app)
    app.run(host="0.0.0.0", port=5050, debug=True)

    