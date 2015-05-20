
cassandra = """[Cassandra](http://cassandra.apache.org/) is a distributed column store that is used by [Digg](http://digg.com) and others to store large quantities of irregular data structures.

Data is looked up strictly by key."""

couch = """[CouchDb](http://couchdb.apache.org/) is a document database that uses the elements of the web: Javascript, JSON and HTTP as its building blocks. It is developed as part of the Apache Foundataion.

One of the unique features of CouchDb is that it has full master-to-master replication.

You can start working with CouchDb immediately via the [Cloudant hosted service](http://cloudant.com/)."""

riak = """[Riak](http://www.basho.com/Riak.html) is an attempt to create a full implementation of a [Amazon's Dynamo store](http://www.allthingsdistributed.com/2007/10/amazons_dynamo.html).

It provides a Javascript map-reduce query system and allows runtime reallocation of resources. It is designed to be distributed with redundant copies of the data being held.

Riak allows the content of its buckets to have a MIME-type as metadata allowing for a deeper comprehension of what a given storage location contains.
"""

mongo = """[MongoDb](http://www.mongodb.org/) is a document database that uses its the [BSON](http://bsonspec.org/) ("bi-son") format to help storage and transportation over the wire.

Mongo includes a propriety query and manipulation language, based on JSON, that makes it easier to sort and compare the conventional relational datatypes. Straight JSON makes this difficult as types such as dates are not directly supported.

Mongo requires language specific-drivers for its format and network protocol. These are available for many languages but you will need to build your own wrapping webservice if you wish to expose a HTTP/JSON endpoint.

You can try Mongo out via the [MongoHQ cloud-hosted service](http://mongohq.com/).
"""

jackrabbit = """[Jackrabbit](http://jackrabbit.apache.org/) is an implementation of [JSR-170](http://jcp.org/en/jsr/detail?id=170), otherwise known as the Java Content Repository.

Jackrabbit is an opensource project that is part of the Apache Foundation. It is effectively a reference implementation for the API. It essentially works a tree-based store with each leaf being a node that is capable of holding metadata as well as content.

Jackrabbit was built to support CMS functions and therefore is content-orientated rather than trying to normalise data."""

voldemort ="""Despite the unusual name [Voldemort](http://project-voldemort.com/) is a capable JVM based key-value store that has been open-sourced by [LinkedIn](http://linkedin.com).

It has a plugable architecture that allows you to mix backends like Oracle BDB and MySQL and allows you a choice of storage formats like JSON and Thrift.

Data is partitioned across multiple nodes and reads and writes are transparently distributed. Similarly the store deals with node failure and recovery transparently too."""

redis ="""[Redis](http://code.google.com/p/redis/) is a key-value store that has big ambitions and is fast building a strong community. Users include [Engine Yard](http://www.engineyard.com/blog/2009/key-value-stores-for-ruby-part-4-to-redis-or-not-to-redis/) and [The Guardian](http://simonwillison.net/static/2010/redis-tutorial/).

Redis wants to move out of being a key-value store with atomic operations to being a set of atomic operations that are performed on data.

Keys are key in using Redis as it is possible to query them and therefore having a logical key-naming system can be very powerful. It is also possible to run the server in a durable mode (making the server fully ACID)."""

tokyo = """The [Tokyo products](http://fallabs.com/) are [extremely popular in the Rails world](http://www.engineyard.com/blog/2009/key-value-stores-for-ruby-part-2-tokyo-cabinet/) and therefore have a lot of deployments under their belt. Tokyo Cabinet is a key-value store with atomic operation support, it is strictly speaking a library rather like [GDB](http://www.vivtek.com/gdbm/). It is only when the Cabinet is combined with the server Tokyo Tyrant that it becomes NoSql store.

Tokyo Cabinet is written in C, while its successor Kyoto Cabinet is written in C++.

Tokyo has suffered in the English-speaking world from the Japanese focus of the developer, the development and roadmap have often seemed opaque and the community seems more user-based than developer based."""

query = """Do you need to be able to query your data?

Be careful when answering this as if you are not sure or find out later that you do need to query your data you will face greater difficulties retrofitting such an involved feature than having some form of it baked into the product.

You may want to consider using complementary search technologies like [Solr](http://lucene.apache.org/solr/) or even keep a subset of your data in a relational store to mitigate the risk of change in the future."""