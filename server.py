import os
from flask import render_template
from hetzner_dns_tools.zone_list import zone_list
from flask import Flask, redirect, url_for, request
from hetzner_dns_tools.record_create import record_create
from hetzner_dns_tools.zone_get import zone_get
app = Flask(__name__)

@app.route('/success')
def success():
  return 'success!'

@app.route('/index', methods=['POST', 'GET'])
def index():
  def zone_names():
    zones = []
    zone_dict = zone_list()
    for i in zone_dict['zones']:
      zones.append(i['name'])
    return zones
  zones = zone_names()
  if request.method == 'POST':
    hetznerdnstoken = request.args.get('page')
    zone = request.form.get('zone_select')
    handle = request.form.get('handle')
    didvalue = request.form.get('didvalue')
    zone_id = zone_get(hetzner_dns_token=hetznerdnstoken,
                    zone_name=zone,
                    id_only=True)
    record = record_create(hetzner_dns_token=hetznerdnstoken,
                           zone_id=zone_id,
                           record_type='TXT',
                           name='_atproto.%s' % (handle),
                           value=didvalue,
                           ttl=60)
    print(record)
    return redirect(url_for('success'))
  else:
    handle = request.args.get('handle')
    didvalue = request.args.get('didvalue')
    zone = request.args.get('zone_select')
    return render_template('index.html', zones=zones)

@app.route('/login', methods=['POST', 'GET'])
def login():
  if request.method == 'POST':
    hetznerdnstoken = request.form['hetznerdnstoken']
    os.environ["HETZNER_DNS_TOKEN"] = hetznerdnstoken
    return redirect(url_for('index', token=hetznerdnstoken))
  else:
    hetznerdnstoken = request.args.get('hetznerdnstoken')
    return render_template('login.html')

if __name__ == '__main__':
  app.run(debug = True)

