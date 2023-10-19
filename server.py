import json
import os
from flask import Flask, redirect, url_for, request
from hetzner_dns_tools.zone_list import zone_list
from hetzner_dns_tools.record_create import record_create
from hetzner_dns_tools.zone_get import zone_get

@app.route('/success')
def success(hetznertoken):
    
@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        hetznerdnstoken = request.form['hetznertoken']
        return redirect(url_for('success', hetznertoken=hetznerdnstoken))
    else: 
        hetznerdnstoken = request.form.get('hetznertoken')
        return redirect(url_for('success', hetznertoken=hetznerdnstoken))
   
@app.route('/add_handle')
def add_handle(hetznertoken, zone_name, handle, did):
    zoneid = zone_get(hetzner_dns_token=hetznerkey,
                    zone_name=zone,
                    id_only=True)
    record = record_create(hetzner_dns_token=hetznerkey,
                    zone_id=zoneid,
                    record_type='TXT',
                    name='_atproto.%s' % (handle),
                    value=didthing,
                    ttl=60)
    return record 

def listzones():
    zones = zone_list()
    print(zones)
    return()
def addname():
    print('what zone do you want to add the handle to?')
    zone = input()
    print('what handle would you like to add to the zone?')
    handle = input()
    print('what\'s the did thing? (from bluesky)')
    didthing = input()
    hetznerkey = os.getenv('HETZNER_DNS_TOKEN')
    zoneid = zone_get(hetzner_dns_token=hetznerkey,
                    zone_name=zone,
                    id_only=True)
    print('got id of %s for %s' % (zoneid, zone))
    record = record_create(hetzner_dns_token=hetznerkey,
                           zone_id=zoneid,
                           record_type='TXT',
                           name='_atproto.%s' % (handle),
                           value=didthing,
                           ttl=60)
    print(record)
    return()
hetznerkey = os.getenv('HETZNER_DNS_TOKEN')
if hetznerkey == None:
    print('please export your hetzner DNS API key to bash by running \'export HETZNER_DNS_TOKEN=yourapikeygoeshere\'')
    quit()
        
while True:
    print('your hetzner key is', hetznerkey)
    print('input 1 of these options:')
    print('1.) list zones')
    print('2.) add bsky name')
    print('3.) exit')
    x = input()
    if x == '1':
        listzones()
    elif x == '2':
        addname()
    elif x == '3':
        quit()
    else:
        print('please enter 1, 2, or 3')
