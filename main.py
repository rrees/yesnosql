import webapp2

import handlers

routes = [('/', handlers.Home),
	('/questionnaire', handlers.Questionnaire),
	('/examples', handlers.Examples),
	('/flowchart', handlers.FlowchartStart),
	(r'/flowchart/(.+)', handlers.Flowchart),
	]

app = webapp2.WSGIApplication(routes, debug=True)
