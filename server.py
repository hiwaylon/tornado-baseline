"""The Rock Strongo web server."""

import logging

from tornado import ioloop
from tornado import web

from api.utils import routes
from api.handlers import create_routes


logging.basicConfig(filename="server.log", level=logging.DEBUG)


def main():
    """Run the server.

    All command line arguments and configuration is handled here before the
    server is started.

    """
    route_map = routes.Routes.instance().routes
    application = web.Application(route_map)

    logging.info("Starting server on port 1337.")
    print("Server started.")
    print(route_map)

    application.listen(port=1337)
    ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()
