## Why would we select one database over another?

- [] mySQL vs. postgres SQL?
- [] relational databases vs. non-relational databases?


---

Just about any popular modern database will handle almost all commercial database tasks[^kolakowski], so why choose one versus another?

A lot of it comes down to preference. One database expert espouses Microsoft SQL Server while another prefers PostgreSQL. 


### Database Types

**Relational databases** are the traditional databases, including MySQL, PostgreSQL, SQLite, Oracle Database, etc.[^schrader]  These databases represent and store data in tables and rows, based on a branch of algebraic set theory known as relational algebra.[^homan] They comply with SQL standards and provide full ACID transactions, meaning that the data transformation you do in the platform is guaranteed to be seen by anybody looking at that data. These databases are also relational in that different tables are usually linked together.[^schrader] <!-- A relational database is ideal for already-homogenized transaction-based information such as banking or accounting records. Relational databases are appropriate for many data-warehousing implementations, with a finite number of attributes for each object-type and easy ways to relate objects on one collection (i.e. table to objects in another collection [^kolakowski].--> <!-- I changed the previous text to avoid plagiarism but someone else but I'm not 100% this means the same thing as what used to be here, so someone might want to check. --> These properties mean relational databases are good for containing transaction-based information described by largely identical data-sets. For instance, relational databases can be used in many data-warehousing implementations where each object-type contains a finite number of properties and can be easily related to other objects in the collection. [^factora]

Relational databases use Structured Querying Language (SQL), making them appropriate for applications which must manage several transactions. Relational databases make use of foreign keys (or indexes) to uniquely identify every atomic piece of data in each table, allowing other tables to refer to that foreign key and create a link between their data pieces. This can be useful for applications which require a lot of data analysis.[^homan]

Relational databases are usually the best choice for applications involving complicated querying, database transactions, and regular data analysis. If you need to handle many database transactions, the referential integrity of a relational database and ACID ensure that they are processed reliably.[^homan]

**Non-relational databases** like MongoDB represent data in collections of JSON documents.[^homan] NoSQL systems are useful for data structures where objects may have a varying number of attributes or in which you can't no beforehand how many attributes it may have, or for data which may have attributes with large binary data, such as sound or vide files. [^kolakowski] In a nonrelational database, such data can be stored without explicitly being linked to data in other tables. [^homan]

Non-relational databases offer a major security advantage in that they don't use SQL and for the most part have no schema, meaning they are immune to SQL injection. Some non-relational databases, such as Mongo, also allow databases to be sharded indefinitely, i.e. to be broken up into multiple partitions to overcome hardware limitations at the expense of replicability. [^homan]

Other reasons for choosing a non-relational database include:[^homan]

* The need to store serialized arrays in JSON objects
* Storing records in the same collection that have different fields or attributes
* Finding yourself de-normalizing your database schema or coding around performance and horizontal scalability issues
* Problems easily pre-defining your schema because of the nature of your data model

However, a major pitfall of non-relationanl databases is the lack of joins, requiring you instead to join the data manually inside your code and creating opportunities for problems to arise. [^homan]

### Common Database Software 

**Microsoft SQL Server** is generally regarded as simple to set up and maintain, and is a popular choice for companies whose IT staff has more experience with Microsoft than with open source. [^kolakowski]

<!-- more work needed -->

**MongoDB** is an open-source platform with commercial licensing and support available, offering high performance, high availability and scalable solution licensing.[^factora] IT can handle data in JSON, CSV and TSV file formats, which are represented internally as BSON (binary JASON).[^homan] Mongo is popular amongst MongoDB Ember Angular and Node.js (MEAN) stack developers because it's written in JSON, a lightweight data interchange format based on JavaScript. Mongo may turnIf your data model turns out to be very complex, or if you find yourself having to de-normalize your database schema, non-relational databases like Mongo may be the best way to go.[^homan] 

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
[^factora]:http://insights.dice.com/2012/04/23/choosing-a-database-right-for-business-2/ "quoted in Kolakowski, Choosing a Database That's Right for Your Business"
[^ist.berkeley]: https://ist.berkeley.edu/is/database/services/selecting_a_platform "Selecting Your Database Platform"
