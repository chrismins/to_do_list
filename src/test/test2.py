from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule, NotFound, RequestRedirect, HTTPException

url_map = Map([
    Rule('/', endpoint='blog/index'),
    Rule('/<int:year>/', endpoint='blog/archive'),
    Rule('/<int:year>/<int:month>/', endpoint='blog/archive'),
    Rule('/<int:year>/<int:month>/<int:day>/', endpoint='blog/archive'),
    Rule('/<int:year>/<int:month>/<int:day>/<slug>', endpoint='blog/show_post'),
    Rule('/about', endpoint='blog/about_me'),
    Rule('/feeds/', endpoint='blog/feeds'),
    Rule('/feeds/<feed_name>.rss', endpoint='blog/show_feed')
])


def on_index(request):
    return Response("Hello from the index")


def application(environ, start_response):
    urls = url_map.bind_to_environ(environ)
    try:
        endpoint, args = urls.match()
    except HTTPException as e:
        raise e
    # request = Request(environ)
    # views = {'blog/index': on_index(request)}
    # response = Response("Hello %s" % request.args.get('name', 'World!'))
    start_response('200 OK', [('Content-Type', 'text/plain')])
    # return response(environ, start_response)
    return ['Rule points to %s with arguments %s' % (endpoint, args)]


if __name__ == '__main__':
    from werkzeug.serving import run_simple

    run_simple('localhost', 4000, application)
