# nav-brief
A simple REST API built using Flask providing up to date weather data on Canadian airports. 

This API is hosted on Heroku at the following endpoint:

```https://naviator.herokuapp.com```

Accessing weather data requires providing a valid airport code. This airport code should be included in the API endpoint.

Found below is an example of one such valid endpoint, which returns weather data on the Kitchener-Waterloo airport:

```https://naviator.herokuapp.com/?code=cykf```

To run this API locally, clone this repo and simply run the ```api.py``` file as follows:

```python api.py```

It will then, by default, deploy the API to the address ```http://localhost:8080/```.

Then, to get weather data on a specific airport, simply provide the code by adjusting the endpoint.

Below is an example of one such endpoint:

```http://localhost:8080/?q=cykf```
