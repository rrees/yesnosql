from google.appengine.ext import webapp
import os
from google.appengine.ext.webapp import template

from questions import questions
from flowchart import flowchart


def render_template(response, template_name, template_values):
	path = os.path.join(os.path.dirname(__file__), 'templates', template_name)
	response.out.write(template.render(path, template_values))

class Home(webapp.RequestHandler):
	def get(self):
		render_template(self.response, 'index.html', {})
	
class Questionnaire(webapp.RequestHandler):
	def get(self):
		template_values = {'questions' : questions}
		path = os.path.join(os.path.dirname(__file__), 'templates', 'questionnaire.html')
		self.response.out.write(template.render(path, template_values))

	def post(self):
		template_values = {}
		score = 0
		questions_answered = []
		for a in self.request.arguments():
			if self.request.get(a) == "yes":
				score = score + reduce(lambda x, y : x + y, [q.score for q in questions if q.name_value == a])
				questions_answered.extend([q for q in questions if q.name_value == a])
		
		template_values['score'] = score
		
		if score >= 0:
			template_values['questions_answered'] = [q for q in questions_answered if q.score >= 0]
			template_values['counterpoint'] = [q for q in questions_answered if q.score < -5]
		else:
			template_values['questions_answered'] = [q for q in questions_answered if q.score <= 0]
			template_values['counterpoint'] = [q for q in questions_answered if q.score > 5]
		
		template_values['result'] = 'NoSQL' if score >= 0 else 'Relational'
		
		template_values['weak'] = True if abs(score) < 10 else False
		
		path = os.path.join(os.path.dirname(__file__), 'templates', 'results.html')
		self.response.out.write(template.render(path, template_values))

class Examples(webapp.RequestHandler):
	def get(self):
		render_template(self.response, 'examples.html', {})

class FlowchartStart(webapp.RequestHandler):
	def get(self):
		render_template(self.response, 'flowchart.html', {})

class Flowchart(webapp.RequestHandler):
	def get(self, entry):
		if entry in flowchart:
			render_template(self.response, 'flowchart-entry.html', {'entry' : flowchart[entry]})
		else:
			self.redirect('/flowchart')