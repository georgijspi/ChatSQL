   3YPFunctionalSpecification code{white-space: pre-wrap;} span.smallcaps{font-variant: small-caps;} span.underline{text-decoration: underline;} div.column{display: inline-block; vertical-align: top; width: 50%;} div.hanging-indent{margin-left: 1.5em; text-indent: -1.5em;} ul.task-list{list-style: none;}

CA326  
ChatSQL

Functional Specification Document

Georgijs Pitkevics

19355266

Chee Hin Choa

21100497

0\. Table of contents
=====================

0\. Table of contents

1\. Introduction

1.1 Overview

1.2 Business Context

1.3 Glossary

2\. General Description

2.1 Product / System Functions
2.2 User Characteristics and Objectives

2.3 Operational Scenarios

2.4 Constraints

3\. Functional Requirements

3.1 User Interaction

3.2 Natural Language Processing (NLP)

3.3 Data Retrieval

3.4 Data Privacy and Security

3.5 Additional Features

4\. System Architecture

5\. High-Level Design

6\. Preliminary Schedule

7\. Appendices

1\. Introduction

1.1 Overview
------------

The ChatSQL project emerges as a revolutionary solution aimed at transforming the way users interact with databases. Fueled by the need to simplify database interactions for individuals with minimal to none IT literacy, ChatSQL is a user-friendly assistant designed to facilitate natural language conversations about data and databases without requiring extensive knowledge of SQL.

1.2 Business Context
--------------------

The ChatSQL project is designed to be the new advancement in user interaction with databases. The target users are those who have little-to-none IT literacy, this makes it a valuable asset for a wide range of users. The project allows users to converse with the application in regular english (natural language) about data and databases, eliminating the need for in-depth knowledge of SQL (Structured Query Language) - the traditional method of accessing databases via SQL prompts which requires 2-3 weeks to become familiar with the basics \[[1](https://www.google.com/url?q=https://bootcamp.berkeley.edu/resources/coding/learn-sql/&sa=D&source=editors&ust=1701452943505082&usg=AOvVaw21AtHz8djLhlK6CnTNPu9x)[\[a\]](#cmnt1)\].

The tool is especially beneficial in scenarios where efficient and user-friendly database management and access is required for business and personal purposes. This makes ChatSQL an ideal solution for small businesses, educational institutions, and non-technical individuals in the many sectors that require database interactions without the learning curve of traditional SQL queries.

1.3 Glossary
------------

Certainly! For a project like ChatSQL, here's a list of terms that could be valuable additions to the glossary section of your documentation:

1. **SQL (Structured Query Language):** A standard language for accessing and manipulating databases.
2. **Natural Language Processing (NLP):** A branch of artificial intelligence that helps computers understand, interpret, and manipulate human language.
3. **Large Language Model (LLM):** Advanced AI models capable of understanding and generating human-like text based on training from extensive text datasets.
4. **User Interface (UI):** The space where interactions between humans and machines occur, involving the design of screens, buttons, icons, and other visual elements.
5. **Backend Module:** The part of the software that does not come in direct contact with the users, responsible for managing the application's data and serving it to the UI.
6. **Flask (Web Framework):** A lightweight WSGI web application framework in Python, used for developing web applications.
7. **API (Application Programming Interface):** A set of rules that allow different software entities to communicate with each other.
8. **Database Connector:** A software library providing an interface for users to connect to a database server.
9. **TailWindCSS:** A utility-first CSS framework for creating custom designs without leaving your HTML.
10. **HTMX:** A modern JavaScript library that allows web pages to be updated asynchronously by exchanging small amounts of data with the server behind the scenes.
11. **Data Privacy:** The aspect of data protection focused on the proper handling of sensitive information, particularly personal data.
12. **NoSQL Databases:** A type of database that provides a mechanism for storage and retrieval of data modeled in means other than the tabular relations used in relational databases.
13. **JavaScript:** A programming language commonly used to create interactive effects within web browsers.
14. **HTML/CSS:** Standard markup languages for creating web pages and web applications.

Adding these terms to your glossary will help provide clarity and aid in understanding for readers who might not be familiar with these specific technical concepts.

2\. General Description
=======================

2.1 Product / System Functions
------------------------------

ChatSQL includes a range of functions aiming to simplify SQL database interactions for users with different levels of technical expertise. The core functionality include:

1.  User Interaction and Experience:

1.  Database Selection: Users are free to interact with any database they desire.
2.  Natural Language Queries: Users can ask the chatbot questions related to the database using natural language. This entails, the user typing in a statement in the format of a question into a message form.
3.  Real-time feedback: Users are shown a progress indicator for queries that take longer to process, this enhances the transparency of the system’s operations and visualizes the expected wait time.
4.  Error detection: If a query is flagged as dangerous by the system, (ie; user entered a query which attempts to delete data from the database, or modify existing data), ChatSQL alerts the user with a friendly notification. The system refuses to enact the SQL statement and then continues to function as normal after the alert has been sent, asking the user for their next prompt.

2.  Large Language Model (LLM[\[b\]](#cmnt2)):

1.  LLMs are utilized to understand and process the natural language and database tables. When a user gives the program a natural language sentence, the LLM analyzes the text to understand the intent and context.
2.  Once the user intent is understood the LLM translates the natural language coupled with the database table titles into a structured SQL query.
3.  The LLM utilized should be able to handle a wide range of query complexities, from simple data retrievals to intricate data comparison.

3.  Data Retrieval:

1.  The system connected to a Large Language Model (LLM) to convert natural language queries into SQL statements.
2.  Responses are presented in natural language form, providing users with easily understandable information.

2.2 User Characteristics and Objectives
---------------------------------------

        User Community:

ChatSQL is made for a diverse user community with varying levels of technical expertise. This includes individuals with minimal IT experience, such as project managers or stakeholders, who may not be familiar with SQL but require access to database information.

        User Objectives:

Users aim to interact with databases effectively, extracting meaningful information from databases without diving into complex SQL queries.

        User Requirements:

User would be required to upload database files and the ability to send messages, ensuring accessibility for individual users with limited technical knowledge.

        Wish List:

Quick Learning Curve: Minimal effort should be required for users to start using the system effectively.

Intuitive User Interface: Users would desire an interface that is simple and easy to use, without any extensive training.

2.3 Operational Scenarios
-------------------------

Scenario 1: Database Query

User Action:

User uploaded and select the desired database.

User asks, "What are the total sales for the last year?"

System Response:

ChatSQL interprets the query using NLP.

Converts it into an SQL statement and runs it on SQL.

Responds with, "The total sales for the last year are $Int."

2.4 Constraints
---------------

Lists general constraints placed upon the design team, including speed requirements, industry protocols, hardware platforms, and so forth.

1.  Security Measures: The system must prioritize data privacy and prevent any unauthorized modifications to the database.
2.  Speed Requirements: The application should provide prompt responses to user queries, ensuring an enjoyable user experience.
3.  Compatibility: ChatSQL should be compatible with different databases, considering differences in SQL syntax and structure.

3\. Functional Requirements
===========================

Description - A full description of the requirement.

Criticality - Describes how essential this requirement is to the overall system.

Technical issues - Describes any design or implementation issues involved in satisfying this requirement.

Dependencies with other requirements - Describes interactions with other requirements.

Others as appropriate

3.1 User Interaction
--------------------

3.1.1 Databases

*   Description:  
    This feature allows users to choose the specific database they intend to query. It is designed to provide flexibility and control, enabling users to interact with their database of choice for data retrieval or manipulation.
*   Criticality:  
    The ability to select different databases is of high importance, as it directly impacts the system's versatility and user accessibility. It is crucial for accommodating a diverse range of user needs and database environments.
*   Technical Issues:

One of the main challenges is ensuring that the system is compatible with a variety of database types and structures. This requires a robust and adaptable framework capable of interfacing with different database systems, ranging from traditional relational databases to more modern NoSQL databases.

Dependencies with Other Requirements: There are no direct dependencies on other requirements. However, the effectiveness of this feature can influence the system's overall performance and user satisfaction.

Others: Maintaining updated support for new database technologies and ensuring secure connections to different database systems are additional considerations for this requirement.

3.1.2 Natural Language Queries:

*   Description:

This requirement focuses on the system's ability to interpret and process user queries presented in natural language. The objective is to enable an intuitive and straightforward interaction for users, allowing them to formulate queries in everyday language rather than technical or structured query formats.

*   Criticality:

This functionality is extremely critical as it shapes the core user experience and broadens system accessibility, especially for those not versed in technical query languages. It stands as a key differentiator in enhancing user convenience.

*   Technical Issues:

The main challenge involves leveraging Large Language Models (LLM) to accurately understand and translate the user's natural language queries into actionable database queries. This requires the LLM to be highly sophisticated in processing diverse linguistic expressions and contextual nuances present in natural language.

*   Dependencies with Other Requirements:

Although this feature can operate independently, its effectiveness is amplified when integrated with other functionalities like database selection. The precision of natural language interpretation by the LLM is crucial in determining the system’s response accuracy and error management.

*   Others:

Key challenges include adapting the LLM to evolving language usage and expressions, ensuring the privacy and security of user inputs, and maintaining a high level of interpretation accuracy amidst the variability of natural language.

3.2 Large Language Models (LLM)
-------------------------------

1.  Conversion to SQL:

*   Description:

This requirement involves the system's capability to transform user-inputted natural language queries into structured SQL statements. This process is central to enabling the system to interact with databases based on user commands expressed in everyday language.

*   Criticality:

The conversion of natural language to SQL holds high importance

as it forms the bridge between user input and actionable database queries. This feature is fundamental for the system's operation and effectiveness in handling user requests.

*   Technical Issues:

The primary challenge is to develop a highly efficient algorithm or use advanced Large Language Models (LLM) that can accurately interpret natural language and convert it into valid SQL syntax. This includes understanding the intent, context, and specifics of each query and mapping them to the correct SQL commands and structures.

*   Dependencies with Other Requirements:

This functionality is dependent on the effective operation of the LLM for understanding natural language inputs. It is crucial that the LLM correctly interprets the user's intent and query specifics to facilitate accurate SQL conversion.

*   Others:

Ongoing efforts are required to continuously improve the accuracy of the conversion algorithm or LLM, ensuring it keeps pace with changes in both natural language usage and SQL standards. Additionally, maintaining a balance between user-friendly query input and the technical specificity required for SQL statements is a key consideration.

2.  Understanding Complex Queries:

*   Description:

ChatSQL should possess the ability to comprehend and process complex queries that involve interactions with multiple database tables. This feature aims to facilitate advanced data retrieval and manipulation across different tables within a database.

*   Criticality:

Understanding complex queries has a medium level of criticality. While it significantly enhances the system's capabilities in handling advanced user requirements, it is secondary to the fundamental functions of basic query processing.

*   Technical Issues:

The key challenge lies in considering and correctly implementing table relationships and SQL joins. The system must be able to identify and construct the necessary joins and conditions when queries span multiple tables, ensuring accurate and efficient data retrieval.

*   Dependencies with Other Requirements:

This advanced functionality depends on the successful completion and reliability of basic natural language to SQL conversion processes. It builds upon the foundational interpretation and conversion mechanisms to handle more intricate query structures.

*   Others:

Additional considerations include optimizing query execution for complex queries to prevent performance issues, continuously updating the system to handle evolving database schemas, and ensuring that complex query processing remains user-friendly and accessible to those without extensive SQL knowledge.

3.3 Data Retrieval
------------------

1.  Query Large Language Model (LLM):

*   Description: This requirement involves ChatSQL utilizing a Large Language Model (LLM) to facilitate the conversion of natural language queries into SQL statements. The system must effectively communicate with the LLM to interpret user inputs and generate corresponding SQL queries.
*   Criticality: Querying the LLM is of high importance as it is pivotal for translating user queries from natural language into a format that the database can understand and process. This feature is central to the system's functionality.
*   Technical Issues: Key challenges include integrating with the LLM's API effectively and managing the processing of large datasets. The system must be capable of sending complex natural language queries to the LLM and receiving SQL statements in return, all while ensuring efficient data handling and response times.
*   Dependencies with Other Requirements: This process relies on the foundational capabilities of understanding natural language inputs and converting them into SQL. The effectiveness of querying the LLM is directly tied to these underlying functionalities.
*   Others: Continuous monitoring and updating of the integration with the LLM are necessary to adapt to any changes in the LLM's operation or API. Additionally, maintaining the system's performance and scalability, especially when dealing with large or complex queries, is an essential ongoing consideration.

2.  Presentation in Natural Language:

*   Description: After executing SQL queries, ChatSQL should present the results back to the user in natural language. This involves translating the structured data obtained from the database into a format that is easily understandable and readable by the user.
*   Criticality: The presentation of query results in natural language is highly critical as it directly impacts the user experience. It is essential for ensuring that users can easily comprehend the information retrieved from the database, especially those not familiar with reading raw database outputs.
*   Technical Issues: The primary challenge is to ensure that the conversion of query results into natural language maintains coherence and readability. This requires sophisticated algorithms or LLM implementations that can interpret and articulate database data in a user-friendly manner.
*   Dependencies with Other Requirements: The ability to present results in natural language is dependent on the successful execution of SQL queries. It is the final step in the user interaction flow, relying on the accuracy and effectiveness of the preceding processes.
*   Others: Ongoing tasks include refining the natural language generation to enhance clarity and conciseness, adapting to various data formats and types for coherent presentation, and ensuring that the language used aligns with the user's level of technical expertise. Additionally, maintaining a balance between detailed data representation and user-friendly language is crucial for this requirement.

3.4 Data Privacy and Security
-----------------------------

1.  Read-Only Operations:

Description: ChatSQL should only execute read-only operations on the database.

Criticality: High

Technical Issues: Implement security measures to prevent modifications.

Dependencies: None

2.  User Authentication:

Description: Implement a secure user authentication system.

Criticality: Medium

Technical Issues: Design a user authentication mechanism.

Dependencies: Successful completion of security measures.

3.5 Additional Features
-----------------------

1.  User-Friendly Interface:

Description: Design an intuitive and user-friendly interface.

Criticality: High

Technical Issues: Incorporate responsive design and user experience principles.

Dependencies: None

2.  Error Handling:

Description: Implement effective error handling and provide clear error messages.

Criticality: Medium

Technical Issues: Identify potential error scenarios and develop appropriate responses.

Dependencies: None

4\. System Architecture
=======================

The architecture of ChatSQL is designed to be modular, flexible, and scalable, with a focus on simplicity and efficiency in its components.

## 4.1 User Interface (UI) Module
- **Description:** Handles user interactions, offering a seamless and intuitive interface for communication with ChatSQL.
- **Components:**
  - HTML/CSS for layout and styling.
  - Javascript for dynamic updates.
  - TailWindCSS for streamlined styling.
- **Interaction:**
  - Receives user queries and displays results.
  - Communicates with the Backend Module for data retrieval.

## 4.2 Backend Module
- **Description:** Serves as ChatSQL's core, managing natural language to SQL conversion and database interactions.
- **Components:**
  - Flask framework for handling HTTP requests.
  - Large Language Model (LLM) for query conversion.
  - Database connector for database communication.
- **Interaction:**
  - Receives queries from the UI Module.
  - Uses LLM for query conversion.
  - Executes SQL queries and sends results back to the UI.

## 4.3 Natural Language Processing (NLP) Module
- **Description:** Focuses on interpreting user queries in natural language.
- **Components:**
  - Natural Language Processing algorithms and libraries.
- **Interaction:**
  - Integrates with Backend Module for accurate query conversion.

## 4.4 Security Module
- **Description:** Ensures data privacy and protects against unauthorized changes.
- **Components:**
  - User authentication mechanisms.
  - Security protocols for database operations.
- **Interaction:**
  - Integrates with Backend Module for operation validation.

## 4.5 Database Module
- **Description:** Manages connections to various databases and executes SQL queries.
- **Components:**
  - Database connector libraries and drivers.
- **Interaction:**
  - Communicates with Backend Module to execute and retrieve data.

## 4.6 External Services
- **Description:** May include third-party tools or APIs for added functionality.
- **Components:**
  - Potential Prisma DB services for visualization.
  - LLM API for query conversion.
- **Interaction:**
  - API calls for additional functionalities.

## 4.7 Reused or 3rd Party Components
- HTMX for dynamic UI updates.
- TailWindCSS for UI styling.
- Flask as the web framework.
- Large Language Model (LLM) for query conversion.
- Third-party database connectors.

## 4.8 Communication Flow
1. **User Query:** User poses queries in natural language via the UI.
2. **NLP Conversion:** UI sends queries to NLP for conversion.
3. **SQL Generation:** NLP converts to SQL and sends to Backend.
4. **Database Interaction:** Backend interacts with Database Module.
5. **Security Checks:** Security Module validates operations.
6. **Result Presentation:** Backend sends results back to UI.

5\. High-Level Design
=====================

This section outlines the high-level design of ChatSQL through system models showing the relationship between components.

## 5.1 System Model
- **Components:**
  - **User Interface (UI):** Receives and displays queries and results.
  - **Natural Language Processing (NLP) Module:** Interprets and converts queries.
  - **Backend Module:** Orchestrates functionality and manages communication.
  - **Security Module:** Ensures data security and user access validation.
  - **Database Module:** Connects to and queries databases.
  - **External Services:** Integrates with third-party tools or APIs.
<div hidden>
```
@startuml
class User {
  +ID: int
  +name: String
  +email: String
}

class Query {
  +ID: int
  +text: String
}

class SQLStatement {
  +ID: int
  +text: String
}

class SecurityLayer {
  +rule: String
  +approve: Boolean
}

class Database {
  +ID: int
  +name: String
}

class ResultSet {
  +ID: int
  +data: String
}

class UserInterface {
  +displayQueryResults(result: ResultSet): void
}

class NaturalLanguageProcessing {
  +convertToSQL(query: Query): SQLStatement
}

class Backend {
  +executeSQL(sql: SQLStatement, database: Database, user: User): ResultSet
}

class SecurityModule {
  +authenticateUser(user: User): boolean
}

class DatabaseModule {
  +connectToDatabase(database: Database): void
  +executeQuery(sql: SQLStatement): ResultSet
}

User --|> Query
Query --|> SQLStatement
SQLStatement --|> SecurityLayer
SecurityLayer --|> Database
ResultSet --|> Database
ResultSet --|> Query
UserInterface -- Backend
Backend --|> SecurityModule
Backend --|> DatabaseModule
NaturalLanguageProcessing --|> Backend
@enduml
```
</div>

![](firstDiagram.svg)



## 5.2 Data Flow Diagram (DFD)
- **Key Components:**
  - **User Interaction:** Users query through UI.
  - **SQL Generation:** Conversion to SQL for database interaction.
  - **Database Interaction:** Backend communicates with Database Module.
  - **Security Checks:** Security Module ensures safe operations.
  - **Result Presentation:** Backend presents results via UI.

<div hidden>
```
@startuml
' Define components
class User {
    User
}
class UserInterface {
    User Interface
}
class ChatBotInterface {
    Natural Language Processing
}
class LargeLanguageModel {
    Large Language Model
}
class BackendModule {
    Backend Module
}
class DatabaseModule {
    Database Module
}
class SecurityModule {
    Security Module
}

' Define stereotypes
class User <<Actor>>
class UserInterface <<UI>>
class ChatBotInterface <<Chatbot>>
class LargeLanguageModel <<LLM>>
class BackendModule <<Process>>
class DatabaseModule <<Database>>
class SecurityModule <<Security>>

' Define relationships
User -down-> UserInterface : "Enters Queries with Table Names"
UserInterface -right-> ChatBotInterface : "User Queries in Natural Language"
ChatBotInterface -right-> LargeLanguageModel : "Analyzes Queries and Database Info"
LargeLanguageModel -down-> BackendModule : "Structured SQL Query"
BackendModule -down-> SecurityModule : "SQL Statement for Security Check"
SecurityModule -right-> DatabaseModule : "Execute SQL Query (if safe)"
DatabaseModule -up-> BackendModule : "Query Results"
BackendModule -up-> UserInterface : "Results and Feedback to User"
@enduml
```
</div>

![](dfd.svg)


## 5.3 Object Model
- **Key Objects:**
  - **User:** Individuals using the system.
  - **Query:** User queries in natural language.
  - **SQL Statement:** SQL version of user queries.
  - **Database:** Various databases available.
  - **Result Set:** Data retrieved in response to queries.
  - **Security Token:** User authentication and access rights.

## 5.4 Interaction Flow
- **Interaction Steps:**
  1. **User Query:** Interaction via UI.
  2. **NLP Conversion:** UI sends query to NLP.
  3. **SQL Generation:** NLP converts to SQL.
  4. **Database Interaction:** Backend and Database Module communication.
  5. **Security Checks:** Security Module validation.
  6. **Result Presentation:** Backend presents results to UI.

6\. Preliminary Schedule
========================

This section provides an initial version of the project plan, including the major tasks to be accomplished, their interdependencies, and their tentative start/stop dates. The plan also includes information on hardware, software, and wetware resource requirements.

The project plan should be accompanied by one or more PERT or GANTT charts.

##Link to compare different between pert chart and gantt chart  
\## I recommend doing pert chart

[https://www.forbes.com/advisor/business/pert-chart-vs-gantt-chart/](https://www.google.com/url?q=https://www.forbes.com/advisor/business/pert-chart-vs-gantt-chart/&sa=D&source=editors&ust=1701452943519627&usg=AOvVaw35zdSVUJ6q3lOan6uG3_xU)

7\. Appendices
==============

Specifies other useful information for understanding the requirements.

[\[a\]](#cmnt_ref1)TODO: Add citation to references, add a link to '\[1\]', which links to the reference.

Perhaps there could be a better reference to use? This one is good already since it comes from the official UC Berkley website.

[\[b\]](#cmnt_ref2)Add LLM and SQL to glossary