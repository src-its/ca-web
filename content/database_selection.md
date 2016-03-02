## What would we select one database over another?

-[] mySQL vs. postgres SQL?
-[] relational databases vs. non-relational databases?


---

Just about any popular modern database will handle almost all commercial database tasks[^kolakowski], so why choose one versus another?

A lot of it comes down to preference. One database expert espouses Microsoft SQL Server while another prefers PostgreSQL. 


### Database Types

**Relational databases** are the usual databases that we've seen for years, including MySQL, PostgreSQL, SQLite, Oracle Database, etc.[^schrader]  These databases represent and store data in tables and rows, based on a branch of algebraic set theory known as relational algebra.[^homan] They comply with SQL standards and provide full ACID transactions.  That is, you can do a lot of data transformation directly in the platform and it is guaranteed that different people looking at the same data will see the same values. They are also relational in that data in different tables are typically joined together. [^schrader]  A relational database is ideal for already-homogenized transaction-based information such as banking or accounting records. Relational databases are appropriate for many data-warehousing implementations, with a finite number of attributes for each object-type and easy ways to relate objects on one collection (i.e. table to objects in another collection.[^kolakowski]

Relational databases use Structured Querying Language (SQL), making them a good choice for applications that involve the management of several transactions. The structure of a relational database allows you to link information from different tables through the use of foreign keys (or indexes), which are used to uniquely identify any atomic piece of data within that table. Other tables may refer to that foreign key, so as to create a link between their data pieces and the piece pointed to by the foreign key. This comes in handy for applications that are heavy into data analysis.[^homan]

If you want your application to handle a lot of complicated querying, database transactions and routine analysis of data, you’ll probably want to stick with a relational database. And if your application is going to focus on doing many database transactions, it’s important that those transactions are processed reliably. This is where ACID (the set of properties that guarantee database transactions are processed reliably) really matters, and where referential integrity comes into play.[^homan]

**Non-relational databases** like MongoDB represent data in collections of JSON documents.[^homan]  These so-called NoSQL systems, are appropriate for data with a variable number of attributes or columns for each main item in a particular data set—especially for data where there is simply no way of knowing in advance what attributes will exist for a particular object within a set. For data that’s loosely structured, with objects that feature a variable number of attributes (with some attributes composed of large binary data—think sound or video files), then a NoSQL database might prove best. [^kolakowski] A non-relational database just stores data without explicit and structured mechanisms to link data from different tables (or buckets) to one another.[^homan]

One of the biggest advantages in going with a non-relational database is that your database is not at risk for SQL injection attacks, because non-relational databases don’t use SQL and are, for the most part, schema-less. Another major advantage, at least with Mongo, is that you can theoretically shard it forever (although that does bring up replication issues). Sharding distributes the data across partitions to overcome hardware limitations.[^homan]

Other reasons for choosing a non-relational database include:[^homan]

* The need to store serialized arrays in JSON objects
* Storing records in the same collection that have different fields or attributes
* Finding yourself de-normalizing your database schema or coding around performance and horizontal scalability issues
* Problems easily pre-defining your schema because of the nature of your data model

In non-relational databases like Mongo, there are no joins like there would be in relational databases. This means you need to perform multiple queries and join the data manually within your code -- and that can get very ugly, very fast.[^homan]

### Common Database Software 

**Microsoft SQL Server** is generally regarded as simple to set up and maintain, and is especially popular in companies where most of the IT staff has strong Microsoft experience and is not fully conversant with open source.[^kolakowski]

**MongoDB** is an open-source platform with commercial licensing and support available.  MongoDB offers high performance, high availability and scalable solution licensing.[^kolakowski] The Mongo import utility can import JSON, CSV and TSV file formats. Mongo query targets of data are technically represented as BSON (binary JASON).[^homan] Mongo is a popular non-relational database for MongoDB Ember Angular and Node.js (MEAN) stack developers because it’s basically written in JavaScript; JSON is JavaScript Object Notation, which is a lightweight data interchange format. If your data model turns out to be very complex, or if you find yourself having to de-normalize your database schema, non-relational databases like Mongo may be the best way to go.[^homan] 

**MySQL** is a mature open-source relational platform offers little or no cost for a development environment, and native versions are available that can run on all major desktop and server platforms. MySQL instances are also available through virtual data centers supported by companies like Amazon, Dell or Rackspace. Another benefit: MySQL can scale in response to business strategy, and supports industry-standard security policies. Oracle (which took over MySQL when it acquired Sun) offers commercial support and licensing for production implementations.[^kolakowski]

**Oracle** has been described as "the aircraft carrier of databases".[^ist.berkeley] Oracle has the richest feature set and the largest market share of any of our databases. The list of what Oracle can't do that another database can is a very short list. Oracle supports a huge array of operating system types, for clients as well as servers. Practically every programming language has bindings for Oracle, and Oracle provides a free client for development and deployment. Server-side development programming is rich. Oracle performance is first rate. Most vendor packages support Oracle, and when open source packages support a commercial database engine, often it is Oracle.[^ist.berkeley]

The downside of Oracle is cost and management complexity. If you are using our services, management complexity is our problem, not yours. Oracle has been making great strides in simplifying this complexity while retaining the power of their engine over their last several major releases. Lastly, we are actively looking at ways to reduce the cost of our Oracle service.[^ist.berkeley]

The **PostgreSQL** slogan is "the world's most advanced open source database". The slogan is well-applied. This engine does not suffer at all from MySQL's "conceptual integrity problems". The core RDBMS functions are very mature, and the optimizer is far more intelligent than MySQL's. PostgreSQL runs on a very wide array of platforms, and has bindings for many popular languages. Server-side programming is dramatically richer than MySQL, and performance scales better. In many ways, PostgreSQL is Oracle-lite.[^ist.berkeley]



### Chosing the database that's right for you.

When choosing a database, it's important to consider who will be using it and what applications must connect to it.

If you are deploying a vendor or open source application, selecting the database that the application best supports will greatly reduce both initial setup time and ongoing support costs.[^ist.berkeley]


Also, consider the priority that scalability poses for that particular model. In order to whiteboard your data model as accurately as possible, you'll need to ask the right questions. Vague or inadequate questions, not surprisingly, result in bad or insufficient data. [^homan]



## References

* [Selecting Your Database Platform](https://ist.berkeley.edu/is/database/services/selecting_a_platform)
* [Relational vs. non-relational databases: Which one is right for you?](https://www.pluralsight.com/blog/software-development/relational-non-relational-databases)
* [In what situations should one use a given database over another?](https://www.quora.com/In-what-situations-should-one-use-a-given-database-over-another)
*[Choosing a Database That’s Right for Your Business](http://insights.dice.com/2012/04/23/choosing-a-database-right-for-business-2/)

[^kolakowski]:http://insights.dice.com/2012/04/23/choosing-a-database-right-for-business-2/ "Choosing a Database That’s Right for Your Business"
[^schrader]: https://www.quora.com/In-what-situations-should-one-use-a-given-database-over-another "Quora: In what situations should one use a given database over another?"
[^homan]: https://www.pluralsight.com/blog/software-development/relational-non-relational-databases "PluralSight:Relational vs. non-relational databases: Which one is right for you?"
[^ist.berkeley]: https://ist.berkeley.edu/is/database/services/selecting_a_platform "Selecting Your Database Platform"
