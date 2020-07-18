from bottle import get, post, run, template, error, request, static_file, response, redirect

from draw import draw_circles


@get('/')
def index():
    return template('index')


@get('/draw')
def draw():
    red = bool(request.query.red)
    green = bool(request.query.green)
    blue = bool(request.query.blue)
    amount = int(request.query.amount)
    min_r = int(request.query.min)
    max_r = int(request.query.max)
    img_path = 'tmp/drawing.png'
    draw_circles(amount, min_r, max_r, (red, green, blue), path=img_path)
    return {'path': img_path}


@get('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/otso/projects/abc/static')


@get('/tmp/<filename>')
def server_tmp(filename):
    return static_file(filename, root='/home/otso/projects/abc/tmp')


@error(404)
def error404(error):
    return 'Nothing here, sorry'


if __name__ == '__main__':
    run(debug=True, reloader=True)
