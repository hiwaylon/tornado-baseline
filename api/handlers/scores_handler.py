"""Example request handler."""

from tornado import web

from api.handlers import mixins
from api.utils import routes


@routes.route("/api/v1/scores")
class ScoresHandler(web.RequestHandler, mixins.ResourceCreationMixin):
    def post(self):
        """Handles requests for diet quality scores."""
        request_data = self.request.to_dict()
        score = self.create_resource(request_data)
        self.set_status(201)
        self.write(score.simple_view())

    def _validate_internal(self, request_data):
        return True

    def _create_internal(self, request_data):
        pass
