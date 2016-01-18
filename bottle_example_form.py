import bottle

@bottle.route('/')
def home_page():
    mythings = ['apple','orange','banana','peach']
    #return bottle.template('hello_world', username="Rob", things=mythings)
    return bottle.template('input_form', {'username' : "Rob", 'things' : mythings})

@bottle.post('/favourite_fruit')
def favourite_fruit():
    fruit = bottle.request.forms.get('fruit')
    if (fruit == None or fruit == ""):
        fruit = "No fruit selected"

    return bottle.template('input_confirmation', {'fruit':fruit})

bottle.debug(True)
bottle.run(host='localhost', port=8080)
