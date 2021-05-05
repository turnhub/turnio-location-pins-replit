# turnio-location-pins-replit

An example Turn.io webhook integration on Replit for location pins. This will read location pins and return the weather at the given coordinates.

*This Replit assumes the following*:

1. You have gone through the [webhooks example](https://github.com/turnhub/turnio-webhooks-replit) and are comfortable with how to get an authentication for Turn and set it up as a secret in Repl.it

# How to run this Repl.it

[![Run on Repl.it](https://repl.it/badge/github/turnhub/turnio-location-pins-replit)](https://repl.it/github/turnhub/turnio-location-pins-replit)

1. Click the `Run on Repl.it` button above and install this example into your Repl.it workspace.
2. Get a Turn token and add it as a secret called `TOKEN` in Repl.it
3. Sign-up for a free [WeatherApi.com account](https://www.weatherapi.com/) and obtain an API token, add that as a secret called `WEATHER_API_TOKEN` in Repl.it
4. Set up the webhook in Turn using the URL generated for your workspace by Repl.it. 
5. Send a message with a location pin to your number and receive information about the current weather at your location.
