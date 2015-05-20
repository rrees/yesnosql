from markdown2 import markdown
from descriptions import cassandra, couch, riak, mongo, jackrabbit, voldemort
from descriptions import redis, tokyo
from descriptions import query

class Link:
	def __init__(self, entry, text):
		self.href = "/flowchart/%s" % entry
		self.text = text

class Entry:
	def __init__(self, title, content, links):
		self.title = title
		self.content = markdown(content)
		self.links = links
		
flowchart = {'1' : Entry('Start', """Do you need full peer-to-peer clustering?

Peer to peer clustering allows any node in a cluster to respond to datastore requests. It also covers the mechanisms of replicating data between nodes and also node discovery. It is very robust compared to more common solutions like [sharding](http://en.wikipedia.org/wiki/Shard_%28database_architecture%29) or read-slaves. However it brings with it a lot of complexity in the construction of a robust store structure, operational issues with provision of storage nodes and potential application complexity.

To help answer it might be worth running through a few disaster situations and looking at what you would like the system to do. If you can tolerate less than maximum availability for read and write operations you have a broader range of options open to you. It is also worth considering that it is not worth running a complex distributed management system if you are only going to have a few nodes in the cluster.""",
	[Link(2, "I need a solution with full peer to peer capabilities"), Link(3, "I don't need this")]),
	'2' : Entry('Need to query?', query, [Link(4, "I need to query my data"), Link('cassandra', "My data is not queryable")]),
	'3' : Entry('Durability?', """Do you need *durable* data?

The biggest issue here is what should happen in a machine crash situation. If someone pulls out the power from your server should the system resume in exactly the same state that it was in when the power went out?

It is tempting to think that all data needs to be durable but don't make ephemeral information like catalogue browsing history or an 'I like this' style button-click equivalent to, say, the placing of an order or the creation of a user account. Durable data comes at the cost of speed, as it means coordinating the persistence of the data.""",
	[Link(2, "I want to minimise the risk of data loss"), Link(5, "I'm prepared to compromise on data durability for other features")]),
	'4' : Entry('JSON?', """Would you prefer to work with JSON as your data format?""", [Link('couch', "Yes"), Link('riak', "No")]),
	'5' : Entry('Need to query?', query, [Link(6, "I need to query my data"), Link(8, "My data is not queryable or I intend to query it outside of my store")]),
	'6' : Entry('Date support', """Would you like built-in support for dates?""", [Link('mongo', "Yes"), Link(7, "No")]),
	'7' : Entry('Fancy a free Web API?', """Do you want to avoid having to wrap a webservice around your store?""", [Link('couch', "Yes"), Link('mongo', "No")]),
	'8' : Entry('Binary data or unicode', """Will the larger part of your data consist of binary data or unicode strings?""", [Link(9, "Binary"), Link(10, "Unicode")]),
	'9' : Entry('Media support?', """Do you want rich content support in the store's API?""", [Link('riak', "No"), Link('jackrabbit', "Yes")]),
	'10' : Entry('JVM', """Are you using a JVM-language?

Although all of the stores mentioned here can be placed behind a webservice to expose platform-neutral services some stores make this easier than others.""", [Link(11, "Yes"), Link(12, "No")]),
	'11' : Entry('Pluggable architecture?', """Would it be valuable to have a pluggable architecture where you can mix and match persistence engines, data storage formats and so on?""", [Link('voldemort', "Yes"), Link(12, "No")]),
	'12' : Entry('Time to get out the testing tools', """At this point in the decision making tree there are many really good NoSql products that could suit your needs.

The best thing to do is to organise a performance and soak test with the leading contenders: [Redis](http://code.google.com/p/redis/) and [Tokyo/Kyoto Cabinet](http://fallabs.com/). You may also want to include things like [memcachedb](http://memcachedb.org/).

Only by working through examples of your proposed data structures, sizes and hardware setup can you exercise the subtle details between the implementations. Your testing should provide a clear choice.

Of course if you don't have time or this is not a big strategical decision that warrants hours of testing, click on below.
""", [Link('tokyo', "Let's play safe"), Link('redis', "I've heard good things about Redis")]),
	'cassandra' : Entry('Cassandra', cassandra, []),
	'riak' : Entry('Riak', riak, []),
	'couch' : Entry('CouchDb', couch, []),
	'mongo' : Entry('MongoDb', mongo, []),
	'jackrabbit' : Entry('Jackrabbit', jackrabbit, []),
	'voldemort' : Entry('Voldemort', voldemort, []),
	'tokyo' : Entry('Tokyo/Kyoto Cabinet', tokyo, []),
	'redis' : Entry('Redis', redis, []),
	}