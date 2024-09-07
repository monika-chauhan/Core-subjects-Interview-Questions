Question1 : What is DBMS? Mention Advantanges?
Answer : Database Management System (DBMS) is a software for storing and retrieving users' data while considering appropriate security measures. It consists of a group of programs which manipulate the database. The DBMS accepts the request for data from an application and instructs the operating system to provide the specific data. In large systems, a DBMS helps users and other third-party software to store and retrieve data.
Advantages:
1.Improved data sharing
2.Improved data security
3.Better data integration
4.Minimised data inconsistency
5.Improved data access
6.Improved decision making
7.Improved end-user productivity

Question2 : What is Database?
Answer : A database is an organised collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just a database.

Question3 : What is a database system?
Question4 : What is RDBMS? Properties ..
A Relational Database Management system (RDBMS) is a database management system that is based on the relational model. It has the following major components: Table, Record/Tuple/Row, Field, and Column/Attribute. Examples of the most popular RDBMS are MYSQL, Oracle, IBM DB2, and Microsoft SQL Server database.

Relational databases have the following properties:

Values are atomic.
All of the values in a column have the same data type.
Each row is unique.
The sequence of columns is insignificant.
The sequence of rows is insignificant.
Each column has a unique name.
Integrity constraints maintain data consistency across multiple tables.

Question5 : Types of Database languages.
Answer : Data Definition Language: DDL stands for Data Definition Language. It is used to define database structure or pattern.
Data Manipulation Language: DML stands for Data Manipulation Language. It is used for accessing and manipulating data in a database. It handles user requests.
Data Control Language: DCL stands for Data Control Language. It is used to retrieve the stored or saved data.
Transaction Control Language: TCL is used to run the changes made by the DML statement. TCL can be grouped into a logical transaction.

Question6 : ACID Properties (VV IMP).
Answer : 
1.Atomicity ensures that a transaction is treated as a single indivisible unit, either executing all its operations or none at all.
2.Consistency ensures that the database remains in a valid state before and after a transaction.
3.Isolation ensures that concurrent transactions do not interfere with each other, maintaining data integrity.
4.Durability guarantees that once a transaction is committed, its effects are permanent and survive any system failures. Together, 
these properties ensure reliability and maintain data integrity in DBMS operations.

- Advantages of ACID properties in DBMS
1.Data Integrity: ACID properties ensure data remains consistent and free from corruption.
2.Reliability: ACID properties provide consistent and reliable execution of transactions.
3.Concurrency Control: ACID properties enable simultaneous access to data without conflicts.
4.Fault Tolerance: ACID properties ensure data durability, surviving system failures.
5.Transaction Management: ACID properties offer structured transaction handling.
6.Compliance and Auditability: ACID properties facilitate regulatory compliance and auditing.

- Disadvantages of ACID properties in DBMS
1.Performance Overhead: ACID properties can impact system performance and throughput due to additional processing and resource utilization.
2.Complexity: Implementing ACID properties adds complexity to database systems, increasing design and maintenance challenges.
3.Scalability Challenges: ACID properties can pose difficulties in highly distributed or scalable systems, limiting scalability.
4.Potential for Deadlocks: ACID transactions using locking mechanisms can lead to deadlocks and system halts.
5.Limited Concurrency: ACID properties may restrict concurrency, impacting overall system throughput.
6.Recovery Complexity: ACID properties introduce complexities in recovery and backup strategies.
7.Trade-off with Availability: Strict adherence to ACID properties may affect system availability in certain situations.

Question7 : What is Database Transaction?
Answer : A transaction is a logical unit of work that accesses and updates the contents of a database. Read and write operations are used by transactions to access data. 


Question7 : Difference between vertical and horizontal scaling?
Answer : Scaling alters the size of a system. In the scaling process, we either compress or expand the system to meet the expected needs. The scaling operation can be achieved by adding resources to meet the smaller expectation in the current system, or by adding a new system in the existing one, or both.
1.Vertical scaling keeps your existing infrastructure but adds computing power. Your existing pool of code does not need to change — you simply need to run the same 
code on machines with better specs. By scaling up, you increase the capacity of a single machine and increase its throughput. Vertical scaling allows data to live 
on a single node, and scaling spreads the load through CPU and RAM resources for your machines.

2.Horizontal scaling simply adds more instances of machines without first implementing improvements to existing specifications. By scaling out, you share the 
processing power and load balancing across multiple machines.

Question8 : What is sharding?
Sharding is a method of splitting and storing a single logical dataset in multiple databases. By distributing the data among multiple machines, a cluster of 
database systems can store larger dataset and handle additional requests. Sharding is necessary if a dataset is too large to be stored in a single database.
Moreover, many sharding strategies allow additional machines to be added. Sharding allows a database cluster to scale along with its data and traffic growth.

Question9 : Keys in DBMS?
Answer : A key is a set of attributes that can identify each tuple uniquely in the given relation.
Types of Keys:
1.Super Key - A superkey is a set of attributes that can identify each tuple uniquely in the given relation. A super key may consist of any number of attributes.
2.Candidate Key - A set of minimal attribute(s) that can identify each tuple uniquely in the given relation is called a candidate key.
3.Primary Key - A primary key is a candidate key that the database designer selects while designing the database. Primary Keys are unique and NOT NULL.
4.Alternate Key - Candidate keys that are left unimplemented or unused after implementing the primary key are called alternate keys.
5.Foreign Key - An attribute ‘X’ is called as a foreign key to some other attribute ‘Y’ when its values are dependent on the values of attribute ‘Y’. The relation in which attribute ‘Y’ is present is called the referenced relation. The relation in which attribute ‘X’ is present is called the referencing relation.
6.Composite Key - A primary key composed of multiple attributes and not just a single attribute is called a composite key.
9.Unique Key - It is unique for all the records of the table. Once assigned, its value cannot be changed i.e. it is non-updatable. It may have a NULL value.

Question10 : Types in relationship?
Answer : A relationship is defined as an association among several entities.
1.Unary Relationship Set - Unary relationship set is a relationship set where only one entity set participates in a relationship set.
2.Binary Relationship Set - Binary relationship set is a relationship set where two entity sets participate in a relationship set.
3.Ternary Relationship Set - Ternary relationship set is a relationship set where three entity sets participate in a relationship set.
4.N-ary Relationship Set - N-ary relationship set is a relationship set where ‘n’ entity sets participate in a relationship set.

Question11 : Data abstraction in DBMS, three levels of it 
Answer : Data Abstraction is a process of hiding unwanted or irrelevant details from the end user. It provides a different view and helps in achieving data independence which is used to enhance the security of data.
Database systems include complex data-structures. In terms of retrieval of data, reduce complexity in terms of usability of users and in order to make the system efficient, developers use levels of abstraction that hide irrelevant details from the users. Levels of abstraction simplify database design.
1. Physical or Internal Level:
The physical or internal layer is the lowest level of data abstraction in the database management system. It is the layer that defines how data is actually stored 
in the database. It defines methods to access the data in the database. It defines complex data structures in detail, so it is very complex to understand, 
which is why it is kept hidden from the end user.

2. Logical or Conceptual Level:
The logical or conceptual level is the intermediate or next level of data abstraction. It explains what data is going to be stored in the database and what the
relationship is between them.
It describes the structure of the entire data in the form of tables. The logical level or conceptual level is less complex than the physical level.
With the help of the logical level, Data Administrators (DBA) abstract data from raw data present at the physical level.

3. View or External Level:
View or External Level is the highest level of data abstraction. There are different views at this level that define the parts of the overall data of the database.
This level is for the end-user interaction; at this level, end users can access the data based on their queries.

Question12 : Indexing in DBMS 

Question13 : What is DDL (Data Definition languages)
Answer : DDL stands for Data Definition Language. It is used to define database structure or pattern.
        It is used to create schema, tables, indexes, constraints, etc. in the database.
        Using the DDL statements, you can create the skeleton of the database.
        Data definition language is used to store the information of metadata like the number of tables and schemas, their names, indexes, columns in each table, constraints, etc.
Question14 : What is DML (Data Manipulation Langauge)
Question15 : What is normalization? Types of normalization/
Question16 : What is denormalization?
Answer : Denormalization is a database optimization technique in which we add redundant data to one or more tables. This can help us avoid costly joins in a relational database. 
        Note that denormalization does not mean not doing normalisation. It is an optimization technique that is applied after doing normalisation.

Question17 : what is functional dependency?
Answer : A functional dependency is a constraint that specifies the relationship between two sets of attributes where one set can accurately determine the value of 
other sets. It is denoted as X → Y, where X is a set of attributes that is capable of determining the value of Y. The attribute set on the left side of the arrow, 
X is called Determinant, while on the right side, Y is called the Dependent.


Question18 : E-R Model
Answer : ER model stands for an Entity-Relationship model. It is a high-level data model. This model is used to define the data elements and relationship for a specified system.
        It develops a conceptual design for the database. It also develops a very simple and easy to design view of data.
        In ER modelling, the database structure is portrayed as a diagram called an entity-relationship diagram. 

Question19 : Conflict serializablity in DBMS?
Answer ; Serializability is a concept that helps us to check which schedules are serializable. A serializable schedule is the one that always leaves the database in
consistent state.
A schedule is called conflict serializability if after swapping of non-conflicting operations, it can transform into a serial schedule.
The schedule will be a conflict serializable if it is conflict equivalent to a serial schedule.

Question20 : What is CCP(concurrency Control Protocols)?
Answer : Concurrency Control is the management procedure that is required for controlling concurrent execution of the operations that take place on a database.
The concurrency control protocols ensure the atomicity, consistency, isolation, durability and serializability of the concurrent execution of the database transactions.
Therefore, these protocols are categorised as:
1.Lock Based Concurrency Control Protocol
2.Timestamp Concurrency Control Protocol
3.Validation Based Concurrency Control Protocol

Question21 : Entity, Entity Type, Entity Set, Weak Entity Set?
Answer : Entity in DBMS can be a real-world object with an existence, For example, in a College database, the entities can be Professor, Students, Courses, etc.

The entity type is a collection of the entity having similar attributes.

Types of Entity type:
1.Strong Entity Type:Strong entities are those entity types which have a key attribute. The primary key helps in identifying each entity uniquely. It is represented by a rectangle.
2.Weak Entity Type: Weak entity type doesn't have a key attribute. Weak entity types can't be identified on their own. It depends upon some other strong entity for its distinct identity.
3.Entity Set: Entity Set is a collection of entities of the same entity type. We can say that entity type is a superset of the entity set as all the entities are included in the entity type.

Question22 : What are SQL commands? Types of them.
Question23 : What is Nested Queries in SQL and its types?
Question24 : What is JOINS. Explain types of Joins?
Question25 : Difference between 2 tier and 2 tier Architecture.
Answer : 1.Two-Tier Database Architecture – In two-tier, the application logic is either buried inside the User Interface on the client or within the database on 
        the server (or both). With two-tier client/server architectures, the user system interface is usually located in the user’s desktop environment and the 
        database management services are usually in a server that is a more powerful machine that services many clients.
        2. Three-Tier Database Architecture –In three-tier, the application logic or process lives in the middle-tier, it is separated from the data and the user 
        interface.Three-tier systems are more scalable, robust and flexible. In addition, they can integrate data from multiple sources. In the three-tier 
        architecture, a middle tier was added between the user system interface client environment and the database management server environment. There are a 
        variety of ways of implementing this middle tier, such as transaction processing monitors, message servers, or application servers.


Difference Between Two-Tier And Three-Tier Database Architecture

Two-Tier Database Architecture	
1.It is a Client-Server Architecture.	
2.In two-tier, the application logic is either buried inside the user interface on the client or within the database on the server (or both).	
3.Two-tier architecture consists of two layers : Client Tier and Database (Data Tier).	
4.It is easy to build and maintain.	
5.Two-tier architecture runs slower.
6.It is less secured as client can communicate with database directly.
7.It results in performance loss whenever the users increase rapidly.
8.Example - Contact Management System created using MS-Access or Railway Reservation System, etc.	

Three-Tier Database Architecture:
1.It is a Web-based application.
2.In three-tier, the application logic or process resides in the middle-tier, it is separated from the data and the user interface.
3.Three-tier architecture consists of three layers : Client Layer, Business Layer and Data Layer.
4.It is complex to build and maintain.
5.Three-tier architecture runs faster.
6.It is secured as client is not allowed to communicate with database directly.
7.It results in performance loss whenever the system is run on Internet but gives more performance than two-tier architecture.
8.Example - Designing registration form which contains text box, label, button or a large website on the Internet, etc.

Question26 : Difference between TRUNCATE and DELETE command.
Question27 : Difference between Intension and Extension in a Database.
Answer : Difference between Intension and Extension in a DataBase
Intension Database	
1.The intension corresponds to what is specified in the relational schema.The intension thus defines all permissible extensions.
2.The intension of a given relation is independent of time. It is the permanent part of the relationship.
3.The intension is a combination of two things: a structure and a set of integrity constraints.	

Extension Database:
1.The extension of a given relation is the set of tuples appearing in that relationship at any given instance
2.The intension of a given relation is independent of time. It is the permanent part of the relationship.
3.It changes as tuples are created, destroyed, and updated.


-Example of Intension Database

Employee (Reg  No.(5) Not NULL, Name Char(20), Age Number (2), Company Char(20))
This is the intension of employee relation.

-Example of Extension Database
Relation: Extension of employees at time t1 when 2 tuples are added-

Reg No.	        Name	            Age 	        Company
22501	    Sonakshi Sahni	        27	        Yagesh Export Ltd.
22502	    Sneha Sarin	            30	        Smile Crafters Dental Cooperates

Relation: Extension of employees at time t2 when 2 more tuples are added and one is updated-

Reg No.	        Name	            Age	            Company
22501	      Sonakshi Sahni	    27	        Yagesh Export Ltd.
22502	      Sneha Arora	        30	        Smile Crafters Dental Cooperates
22504	      Rajat Mishra	        29	        RTF Bank 
22509	      Varun Kakkar	        24	        HSM Management 


Question28 : Difference between share lock and exclusive lock, definition of lock.
ANswer : Lock :-VSAM record-level sharing has multiple lock structures that are defined in the active storage management subsystem (SMS) configuration. 
        The multiple, secondary lock structures can be defined by using the parameter, Lock Set, in the SMS Storage Class definition. 
        Using the lock set attribute, additional Coupling Facility DFSMS Lock Structure to be associated with a single SMS storage class.
        VSAM supports two types of locks for files accessed in RLS mode. These two types are:

1.Exclusive Lock 
2.Shared Lock

Exclusive Lock	Shared Lock
1.The Exclusive Lock is used and valid on a single transaction, that locks either row or a page depending on the data. 	
2.An exclusive lock is read as well as a write lock.	
3.It protects updates to file resources, both recoverable and non-recoverable.	
4.This lock is issued when a transaction wants to update unlocked items.
5.There cannot be more than one exclusive lock on the same resource. 	
6.Any transaction that requires an exclusive lock must wait if another task currently owns an exclusive lock or a shared lock against the requested resource.

Exclusive Lock	Shared Lock
1.  The shared lock ensures that a record is not in the process of being updated during a read-only request. It is also used to prevent updates of a record between the time that a record is read and the next sync point.
2.	A shared lock is basically a read-only lock for a row level.
3.	A Shared Lock is basically a read-only lock for a row level. Any number of resources can fetch the data to read when the shared lock is present on the resource.
4.	This lock is issued when a transaction wants to read an item that doesn't have an exclusive lock.
5.	Many process IDs can have a shared lock on the same resource to read the respective data.
6.	Several tasks can own shared locks, there are some circumstances in which tasks can be forced to wait for a lock: 
    A request for a shared lock must wait if another task currently owns an exclusive lock on the resource.
    A request for an exclusive lock must wait if other tasks currently own shared locks on this resource. 
    A new request for a shared lock must wait if another task is waiting for an exclusive lock on a resource that already has a shared lock.