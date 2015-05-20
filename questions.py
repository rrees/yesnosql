
class Question:
	def __init__(self, question, score, name_value, analysis):
		self.question = question
		self.score = score
		self.name_value = name_value
		self.analysis = analysis

questions = [
	Question('Do any of your tables have null columns?', 10, 'Q1', 'Nullable columns indicate a low normal form requirement and your consumers have to have logic in handling null data.'),
	Question('Do you have a lot of link tables to child tables that contain small numbers of rows?', 5, 'Q2','Child tables with few rows indicate that there a few special forms of the main parent data that require a lot of schema work for a few exception cases. Denormalisation and sub-document ideas might help the burden here.'),
	Question('Is your schema heavily constrained?', -10, 'Q3', 'Relational data is great for representing consistent and heavily typed data.'),
	Question('Do you have code in your schema, e.g. stored procedures or triggers?', -10, 'Q4', 'Although it is possible to run scripting languages such as Javascript and Lua in NoSQL stores it is hard to translate things like triggers, jobs or grouped data manipulation into NoSQL equivalents currently'),
	Question('Does your schema have a lot of CLOBs or BLOBs?', 10, 'Q5', 'Large Objects or LOBs run contrary to the general theme of relational strong types and generally indicate data that could probably find a better expression outside the relational model.'),
	Question('Does your schema contain a lot of views?', -4, 'Q6', 'NoSQL prefers denormalistion to optimised query execution on-demand. If you are legitmately using a lot of views then you might struggle to express this with a NoSQL solution.'),
	Question('Will your child tables contain roughly one row for each row in the parent tables?', -10, 'Q7', 'Child tables that have one row for each row in the parent tend to indicate a high normal form. Such structures tend to work better in relational stores'),
	Question('Does the volume of data you anticipate mandate a sharded solution?', 6, 'Q8', 'Conventional sharding in relational data is often more problematic than many of the NoSQL clustering and replication solutions. Sharding also implies that there are some natural divisions in your data that can be used to distribute work across a cluster.'),
	Question('Will analysts be expected to run reports and queries against this database?', -7, 'Q9', 'There are a lot of reporting tools and learning resources for SQL that simply don''t exist yet for NoSQL databases.'),
	Question('When executing queries will you be comparing sets of data or using subsets of data as query predicates?', -8, 'Q10', 'Relational data has very strong set generation and comparision tools, SQL operators like EXISTS, GROUP BY and IN are very powerful and would have to be implemented from scratch in a lot of NoSQL products.'),
	]