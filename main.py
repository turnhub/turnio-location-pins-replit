from flask import Flask, request
import os
import requests

app = Flask('app')

# Repl provides these environment variables, we use it
# to construct the URL that this repl will be accessible on.
repl_owner = os.environ.get("REPL_OWNER")
repl_slug = os.environ.get("REPL_SLUG")
repl_url = "https://%s.%s.repl.co" % (repl_slug, repl_owner)

TOKEN = os.environ.get("TOKEN")
WEATHER_API_TOKEN = os.environ.get("WEATHER_API_TOKEN")

@app.route('/')
def hello_world():
  return 'The Turn UI integration API endpoint is at %s/location' % (repl_url,)

@app.route('/location', methods=["POST"])
def location():
  json = request.json
  # Skip status updates
  if "messages" not in json:
    return ''

  # Skip things that aren't location pins
  message = json["messages"][0]
  wa_id = message["from"]
  if message["type"] != "location":
    return ''

  latitude = message["location"]["latitude"]
  longitude = message["location"]["longitude"]
  
  r = requests.get(
    url='http://api.weatherapi.com/v1/current.json',
    params={
      'key': WEATHER_API_TOKEN,
      'q': '%s,%s' % (latitude,longitude)
    }
  )
  data = r.json()

  country = data["location"]["country"]
  city = data["location"]["name"]
  condition_text = data["current"]["condition"]["text"]
  condition_icon = data["current"]["condition"]["icon"]
  temp_c = data["current"]["temp_c"]
  temp_c_feeling = data["current"]["feelslike_c"]

  send_reply(
    wa_id, "https:%s" % (condition_icon,), 
    "At your location in %s, %s it is %s. The temperature is %s °C and feels like %s °C." % (
      city, country, condition_text, temp_c, temp_c_feeling
    ))
  return ''

def send_reply(wa_id, image_url, caption):
  return requests.post(
    url='https://whatsapp.turn.io/v1/messages',
    headers={
      'Authorization': f'Bearer {TOKEN}',
      'Content-Type': 'application/json'
    },
    json={
      'to': wa_id,
      'type': 'image',
      'image': {
        'link': image_url,
        'caption': caption
      }
    }
  )
app.run(host='0.0.0.0', port=8080)