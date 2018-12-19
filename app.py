from sys import argv
from bottle import route, run
from jinja2 import Template


counter = 0


@route('/')
def index():
    global counter
    counter = counter + 1
    template = Template('<h1>this server was accessed {{ count }} times</h1>')
    return template.render(count=counter)


if __name__ == "__main__":
    run(host='0.0.0.0', port=argv[1])