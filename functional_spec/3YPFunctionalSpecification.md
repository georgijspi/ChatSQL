---
generator: pandoc
title: 3YPFunctionalSpecification
viewport: 'width=device-width, initial-scale=1.0, user-scalable=yes'
---

<div>

[]{.c16 .c27 .c49}

[]{.c49 .c16 .c27}

</div>

[CA326\
ChatSQL]{.c26 .c7 .c16}

[Functional Specification Document]{.c7 .c16 .c26}

[]{.c7 .c16 .c47}

[]{#t.9355cc9b6e69bc0b8a99fde3d28dc2dbadaaaeae}[]{#t.0}

  --------------------------- -----------------
  [Georgijs Pitkevics]{.c2}   [19355266]{.c2}
  [Chee Hin Choa]{.c2}        [21100497]{.c2}
  --------------------------- -----------------

[]{.c39 .c7 .c44} {#h.s1jr5f346z3v .c34 .c40}
=================

[0. Table of contents]{.c39 .c7 .c44} {#h.xjogniy57xer .c34}
=====================================

[[0. Table of contents        ](#h.fnnvelea07rg){.c15}]{.c7
.c16}[[1](#h.fnnvelea07rg){.c15}]{.c7}

[[1. Introduction        ](#h.139k4md7w1yu){.c15}]{.c7
.c16}[[1](#h.139k4md7w1yu){.c15}]{.c7}

[[1.1 Overview        ](#h.1d0m06h1nkhu){.c15}]{.c7
.c16}[[2](#h.1d0m06h1nkhu){.c15}]{.c7}

[[1.2 Business Context        ](#h.o4hgq1sjr4ub){.c15}]{.c7
.c16}[[2](#h.o4hgq1sjr4ub){.c15}]{.c7}

[[1.3 Glossary        ](#h.x47dfdtcrak4){.c15}]{.c7
.c16}[[2](#h.x47dfdtcrak4){.c15}]{.c7}

[[2. General Description        ](#h.qd4at0ke2h79){.c15}]{.c7
.c16}[[2](#h.qd4at0ke2h79){.c15}]{.c7}

[[2.1 Product / System Functions        ](#h.mgbhkq8ahx90){.c15}]{.c7
.c16}[[3](#h.mgbhkq8ahx90){.c15}]{.c7}

[[2.2 User Characteristics and
Objectives        ](#h.lbye5w296qfd){.c15}]{.c7
.c16}[[3](#h.lbye5w296qfd){.c15}]{.c7}

[[2.3 Operational Scenarios        ](#h.k43acux1u5zs){.c15}]{.c7
.c16}[[4](#h.k43acux1u5zs){.c15}]{.c7}

[[2.4 Constraints        ](#h.zhmaq8s278k7){.c15}]{.c7
.c16}[[5](#h.zhmaq8s278k7){.c15}]{.c7}

[[3. Functional Requirements        ](#h.8iaibjt2026s){.c15}]{.c7
.c16}[[6](#h.8iaibjt2026s){.c15}]{.c7}

[[3.1 User Interaction        ](#h.hsu6k91ws6qn){.c15}]{.c7
.c16}[[7](#h.hsu6k91ws6qn){.c15}]{.c7}

[[3.2 Natural Language Processing
(NLP)        ](#h.c5x4gzkcy2f9){.c15}]{.c7
.c16}[[7](#h.c5x4gzkcy2f9){.c15}]{.c7}

[[3.3 Data Retrieval        ](#h.w6nf2lte59yb){.c15}]{.c7
.c16}[[8](#h.w6nf2lte59yb){.c15}]{.c7}

[[3.4 Data Privacy and Security        ](#h.g7o733r8yk6a){.c15}]{.c7
.c16}[[8](#h.g7o733r8yk6a){.c15}]{.c7}

[[3.5 Additional Features        ](#h.do634jekmob6){.c15}]{.c7
.c16}[[9](#h.do634jekmob6){.c15}]{.c7}

[[4. System Architecture        ](#h.3ei66bw8x0jb){.c15}]{.c7
.c16}[[10](#h.3ei66bw8x0jb){.c15}]{.c7}

[[5. High-Level Design        ](#h.sezggz2kqkbg){.c15}]{.c7
.c16}[[15](#h.sezggz2kqkbg){.c15}]{.c7}

[[6. Preliminary Schedule        ](#h.bvnvssp3g8n){.c15}]{.c7
.c16}[[20](#h.bvnvssp3g8n){.c15}]{.c7}

[[7. Appendices        ](#h.qffi6xv1kj3n){.c15}]{.c7
.c16}[[21](#h.qffi6xv1kj3n){.c15}]{.c7}

[]{.c2}

[1. Introduction]{.c38 .c46}

[1.1 ]{.c7 .c27}[Overview]{.c21 .c7} {#h.1d0m06h1nkhu .c4}
------------------------------------

[The ChatSQL project emerges as a revolutionary solution aimed at
transforming the way users interact with databases. Fueled by the need
to simplify database interactions for individuals with minimal to none
IT literacy, ChatSQL is a user-friendly assistant designed to facilitate
natural language conversations about data and databases without
requiring extensive knowledge of SQL.]{.c3}

[1.2 ]{.c7 .c27}[Business Context]{.c21 .c7} {#h.o4hgq1sjr4ub .c4}
--------------------------------------------

[The ChatSQL project is designed to be the new advancement in user
interaction with databases. The target users are those who have
little-to-none IT literacy, this makes it a valuable asset for a wide
range of users. The project allows users to converse with the
application in regular english (natural language) about data and
databases, eliminating the need for in-depth knowledge of SQL
(Structured Query Language) - the traditional method of accessing
databases via SQL prompts which requires 2-3 weeks to become familiar
with the basics \[]{.c7
.c12}[[1](https://www.google.com/url?q=https://bootcamp.berkeley.edu/resources/coding/learn-sql/&sa=D&source=editors&ust=1701452943505082&usg=AOvVaw21AtHz8djLhlK6CnTNPu9x){.c15}]{.c7
.c12 .c14}^[\[a\]](#cmnt1){#cmnt_ref1}^[\].]{.c3}

[]{.c3}

[The tool is especially beneficial in scenarios where efficient and
user-friendly database management and access is required for business
and personal purposes. This makes ChatSQL an ideal solution for small
businesses, educational institutions, and non-technical individuals in
the many sectors that require database interactions without the learning
curve of traditional SQL queries.]{.c3}

[1.3 ]{.c7 .c27}[Glossary]{.c13} {#h.x47dfdtcrak4 .c4}
--------------------------------

[Define and technical terms used in this document. Only include those
with which the reader may not be familiar.]{.c3 .c32}

[]{.c3}

[2. General Description]{.c28 .c38} {#h.qd4at0ke2h79 .c19}
===================================

[2.1 ]{.c7 .c27}[Product / System Functions]{.c7 .c21} {#h.mgbhkq8ahx90 .c4}
------------------------------------------------------

[ChatSQL includes a range of functions aiming to simplify SQL database
interactions for users with different levels of technical expertise. The
core functionality include:]{.c3}

1.  [User Interaction and Experience:]{.c3}

```{=html}
<!-- -->
```
1.  [Database Selection: Users are free to interact with any database
    they desire.]{.c3}
2.  [Natural Language Queries: Users can ask the chatbot questions
    related to the database using natural language. This entails, the
    user typing in a statement in the format of a question into a
    message form.]{.c3}
3.  [Real-time feedback: Users are shown a progress indicator for
    queries that take longer to process, this enhances the transparency
    of the system's operations and visualizes the expected wait
    time.]{.c3}
4.  [Error detection: If a query is flagged as dangerous by the system,
    (ie; user entered a query which attempts to delete data from the
    database, or modify existing data), ChatSQL alerts the user with a
    friendly notification. The system refuses to enact the SQL statement
    and then continues to function as normal after the alert has been
    sent, asking the user for their next prompt.]{.c3}

```{=html}
<!-- -->
```
2.  [Large Language Model (]{.c7 .c12}[LLM]{.c7
    .c12}^[\[b\]](#cmnt2){#cmnt_ref2}^[):]{.c3}

```{=html}
<!-- -->
```
1.  [LLMs are utilized to understand and process the natural language
    and database tables. When a user gives the program a natural
    language sentence, the LLM analyzes the text to understand the
    intent and context.]{.c3}
2.  [Once the user intent is understood the LLM translates the natural
    language coupled with the database table titles into a structured
    SQL query. ]{.c3}
3.  [The LLM utilized should be able to handle a wide range of query
    complexities, from simple data retrievals to intricate data
    comparison. ]{.c3}

```{=html}
<!-- -->
```
3.  [Data Retrieval:]{.c3}

```{=html}
<!-- -->
```
1.  [The system connected to a Large Language Model (LLM) to convert
    natural language queries into SQL statements.]{.c3}
2.  [Responses are presented in natural language form, providing users
    with easily understandable information.]{.c3}

[2.2 ]{.c7 .c27}[User Characteristics and Objectives]{.c13} {#h.lbye5w296qfd .c4}
-----------------------------------------------------------

[]{.c3 .c32}

[        ]{.c7 .c12}[User Community:]{.c39 .c7 .c12}

[ChatSQL is made for a diverse user community with varying levels of
technical expertise. This includes individuals with minimal IT
experience, such as project managers or stakeholders, who may not be
familiar with SQL but require access to database information.]{.c3}

[        ]{.c7 .c12}[User Objectives:]{.c7 .c12 .c39}

[Users aim to interact with databases effectively, extracting meaningful
information from databases without diving into complex SQL
queries.]{.c3}

[        ]{.c7 .c12}[User Requirements:]{.c39 .c7 .c12}

[User would be required to upload database files and the ability to send
messages, ensuring accessibility for individual users with limited
technical knowledge.]{.c3}

[        ]{.c7 .c12}[Wish List:]{.c39 .c7 .c12}

[Quick Learning Curve: Minimal effort should be required for users to
start using the system effectively.]{.c3}

[Intuitive User Interface: Users would desire an interface that is
simple and easy to use, without any extensive training.]{.c3}

[]{.c3}

[2.3 ]{.c7 .c27}[Operational Scenarios]{.c13} {#h.k43acux1u5zs .c4}
---------------------------------------------

[]{.c3 .c32}

[Scenario 1: Database Query]{.c3}

[User Action:]{.c3}

[User uploaded and select the desired database.]{.c3}

[User asks, \"What are the total sales for the last year?\"]{.c3}

[System Response:]{.c3}

[ChatSQL interprets the query using NLP.]{.c3}

[Converts it into an SQL statement and runs it on SQL.]{.c3}

[Responds with, \"The total sales for the last year are \$Int.\"]{.c3}

[]{.c3}

[2.4 ]{.c7 .c27}[Constraints]{.c13} {#h.zhmaq8s278k7 .c4}
-----------------------------------

[Lists general constraints placed upon the design team, including speed
requirements, industry protocols, hardware platforms, and so
forth.]{.c3}

1.  [Security Measures: The system must prioritize data privacy and
    prevent any unauthorized modifications to the database.]{.c3}
2.  [Speed Requirements: The application should provide prompt responses
    to user queries, ensuring an enjoyable user experience.]{.c3}
3.  [Compatibility: ChatSQL should be compatible with different
    databases, considering differences in SQL syntax and
    structure.]{.c3}

[3. Functional Requirements]{.c7 .c28} {#h.8iaibjt2026s .c19}
======================================

[]{.c3 .c32}

[Description - A full description of the requirement.]{.c3 .c32}

[Criticality - Describes how essential this requirement is to the
overall system.]{.c3 .c32}

[Technical issues - Describes any design or implementation issues
involved in satisfying this requirement.]{.c3 .c32}

[Dependencies with other requirements - Describes interactions with
other requirements.]{.c3 .c32}

[Others as appropriate]{.c3 .c32}

[]{.c3}

[3.1 ]{.c7 .c27}[User Interaction]{.c13} {#h.hsu6k91ws6qn .c4}
----------------------------------------

3.1.1 Databases

-   [Description:\
    This feature allows users to choose the specific database they
    intend to query. It is designed to provide flexibility and control,
    enabling users to interact with their database of choice for data
    retrieval or manipulation.]{.c3}
-   [Criticality:\
    The ability to select different databases is of high importance, as
    it directly impacts the system\'s versatility and user
    accessibility. It is crucial for accommodating a diverse range of
    user needs and database environments.]{.c3}
-   [Technical Issues: ]{.c3}

[One of the main challenges is ensuring that the system is compatible
with a variety of database types and structures. This requires a robust
and adaptable framework capable of interfacing with different database
systems, ranging from traditional relational databases to more modern
NoSQL databases.]{.c3}

[Dependencies with Other Requirements: There are no direct dependencies
on other requirements. However, the effectiveness of this feature can
influence the system\'s overall performance and user satisfaction.]{.c3}

[Others: Maintaining updated support for new database technologies and
ensuring secure connections to different database systems are additional
considerations for this requirement.]{.c3}

[]{.c3}

[]{.c3}

[3.1.2 ]{.c7 .c12}[Natural Language Queries:]{.c3}

-   [Description: ]{.c3}

[This requirement focuses on the system\'s ability to interpret and
process user queries presented in natural language. The objective is to
enable an intuitive and straightforward interaction for users, allowing
them to formulate queries in everyday language rather than technical or
structured query formats.]{.c3}

[]{.c3}

-   [Criticality:]{.c3}

[This functionality is extremely critical as it shapes the core user
experience and broadens system accessibility, especially for those not
versed in technical query languages. It stands as a key differentiator
in enhancing user convenience.]{.c3}

[]{.c3}

-   [Technical Issues:]{.c3}

[The main challenge involves leveraging Large Language Models (LLM) to
accurately understand and translate the user\'s natural language queries
into actionable database queries. This requires the LLM to be highly
sophisticated in processing diverse linguistic expressions and
contextual nuances present in natural language.]{.c3}

[]{.c3}

-   [Dependencies with Other Requirements: ]{.c3}

[Although this feature can operate independently, its effectiveness is
amplified when integrated with other functionalities like database
selection. The precision of natural language interpretation by the LLM
is crucial in determining the system's response accuracy and error
management.]{.c3}

[]{.c3}

-   [Others: ]{.c3}

[Key challenges include adapting the LLM to evolving language usage and
expressions, ensuring the privacy and security of user inputs, and
maintaining a high level of interpretation accuracy amidst the
variability of natural language.]{.c3}

[]{.c3}

[]{.c3}

[]{.c3}

[3.2 ]{.c7 .c27}[Large Language Models (LLM)]{.c13} {#h.c5x4gzkcy2f9 .c4}
---------------------------------------------------

1.  [Conversion to SQL:]{.c3}

-   [Description: ]{.c3}

[This requirement involves the system\'s capability to transform
user-inputted natural language queries into structured SQL statements.
This process is central to enabling the system to interact with
databases based on user commands expressed in everyday language.]{.c3}

[]{.c3}

-   [Criticality: ]{.c3}

[The conversion of natural language to SQL holds high importance ]{.c3}

[as it forms the bridge between user input and actionable database
queries. This feature is fundamental for the system\'s operation and
effectiveness in handling user requests.]{.c3}

[]{.c3}

-   [Technical Issues: ]{.c3}

[The primary challenge is to develop a highly efficient algorithm or use
advanced Large Language Models (LLM) that can accurately interpret
natural language and convert it into valid SQL syntax. This includes
understanding the intent, context, and specifics of each query and
mapping them to the correct SQL commands and structures.]{.c3}

[]{.c3}

-   [Dependencies with Other Requirements: ]{.c3}

[This functionality is dependent on the effective operation of the LLM
for understanding natural language inputs. It is crucial that the LLM
correctly interprets the user\'s intent and query specifics to
facilitate accurate SQL conversion.]{.c3}

[]{.c3}

-   [Others: ]{.c3}

[Ongoing efforts are required to continuously improve the accuracy of
the conversion algorithm or LLM, ensuring it keeps pace with changes in
both natural language usage and SQL standards. Additionally, maintaining
a balance between user-friendly query input and the technical
specificity required for SQL statements is a key consideration.]{.c3}

-   []{.c3}

[]{.c3}

2.  [Understanding Complex Queries:]{.c7 .c12}

-   [Description: ]{.c3}

[ChatSQL should possess the ability to comprehend and process complex
queries that involve interactions with multiple database tables. This
feature aims to facilitate advanced data retrieval and manipulation
across different tables within a database.]{.c3}

[]{.c3}

-   [Criticality: ]{.c3}

[Understanding complex queries has a medium level of criticality. While
it significantly enhances the system\'s capabilities in handling
advanced user requirements, it is secondary to the fundamental functions
of basic query processing.]{.c3}

[]{.c3}

-   [Technical Issues: ]{.c3}

[The key challenge lies in considering and correctly implementing table
relationships and SQL joins. The system must be able to identify and
construct the necessary joins and conditions when queries span multiple
tables, ensuring accurate and efficient data retrieval.]{.c3}

[]{.c3}

-   [Dependencies with Other Requirements: ]{.c3}

[This advanced functionality depends on the successful completion and
reliability of basic natural language to SQL conversion processes. It
builds upon the foundational interpretation and conversion mechanisms to
handle more intricate query structures.]{.c3}

[]{.c3}

-   [Others: ]{.c3}

[Additional considerations include optimizing query execution for
complex queries to prevent performance issues, continuously updating the
system to handle evolving database schemas, and ensuring that complex
query processing remains user-friendly and accessible to those without
extensive SQL knowledge.]{.c3}

[]{.c3}

[3.3 ]{.c7 .c27}[Data Retrieval]{.c13} {#h.w6nf2lte59yb .c4}
--------------------------------------

1.  [Query Large Language Model (LLM):]{.c7 .c12}

-   [Description: This requirement involves ChatSQL utilizing a Large
    Language Model (LLM) to facilitate the conversion of natural
    language queries into SQL statements. The system must effectively
    communicate with the LLM to interpret user inputs and generate
    corresponding SQL queries.]{.c3}
-   [Criticality: Querying the LLM is of high importance as it is
    pivotal for translating user queries from natural language into a
    format that the database can understand and process. This feature is
    central to the system\'s functionality.]{.c3}
-   [Technical Issues: Key challenges include integrating with the
    LLM\'s API effectively and managing the processing of large
    datasets. The system must be capable of sending complex natural
    language queries to the LLM and receiving SQL statements in return,
    all while ensuring efficient data handling and response times.]{.c3}
-   [Dependencies with Other Requirements: This process relies on the
    foundational capabilities of understanding natural language inputs
    and converting them into SQL. The effectiveness of querying the LLM
    is directly tied to these underlying functionalities.]{.c3}
-   [Others: Continuous monitoring and updating of the integration with
    the LLM are necessary to adapt to any changes in the LLM\'s
    operation or API. Additionally, maintaining the system\'s
    performance and scalability, especially when dealing with large or
    complex queries, is an essential ongoing consideration.]{.c3}

[]{.c3}

2.  [Presentation in Natural Language:]{.c7 .c12}

-   [Description: After executing SQL queries, ChatSQL should present
    the results back to the user in natural language. This involves
    translating the structured data obtained from the database into a
    format that is easily understandable and readable by the user.]{.c3}
-   [Criticality: The presentation of query results in natural language
    is highly critical as it directly impacts the user experience. It is
    essential for ensuring that users can easily comprehend the
    information retrieved from the database, especially those not
    familiar with reading raw database outputs.]{.c3}
-   [Technical Issues: The primary challenge is to ensure that the
    conversion of query results into natural language maintains
    coherence and readability. This requires sophisticated algorithms or
    LLM implementations that can interpret and articulate database data
    in a user-friendly manner.]{.c3}
-   [Dependencies with Other Requirements: The ability to present
    results in natural language is dependent on the successful execution
    of SQL queries. It is the final step in the user interaction flow,
    relying on the accuracy and effectiveness of the preceding
    processes.]{.c3}
-   [Others: Ongoing tasks include refining the natural language
    generation to enhance clarity and conciseness, adapting to various
    data formats and types for coherent presentation, and ensuring that
    the language used aligns with the user\'s level of technical
    expertise. Additionally, maintaining a balance between detailed data
    representation and user-friendly language is crucial for this
    requirement.]{.c3}

[]{.c3}

[3.4 ]{.c7 .c27}[Data Privacy and Security]{.c13} {#h.g7o733r8yk6a .c4}
-------------------------------------------------

1.  [Read-Only Operations:]{.c7 .c12}

[Description: ChatSQL should only execute read-only operations on the
database.]{.c3}

[Criticality: High]{.c3}

[Technical Issues: Implement security measures to prevent
modifications.]{.c3}

[Dependencies: None]{.c3}

[]{.c3}

2.  [User Authentication:]{.c7 .c12}

[Description: Implement a secure user authentication system.]{.c3}

[Criticality: Medium]{.c3}

[Technical Issues: Design a user authentication mechanism.]{.c3}

[Dependencies: Successful completion of security measures.]{.c3}

[3.5 ]{.c7 .c27}[Additional Features]{.c13} {#h.do634jekmob6 .c4}
-------------------------------------------

1.  [User-Friendly Interface:]{.c3}

[]{.c3}

[Description: Design an intuitive and user-friendly interface.]{.c3}

[Criticality: High]{.c3}

[Technical Issues: Incorporate responsive design and user experience
principles.]{.c3}

[Dependencies: None]{.c3}

2.  [Error Handling:]{.c7 .c12}

[Description: Implement effective error handling and provide clear error
messages.]{.c3}

[Criticality: Medium]{.c3}

[Technical Issues: Identify potential error scenarios and develop
appropriate responses.]{.c3}

[Dependencies: None]{.c3}

[]{.c3}

[4. System Architecture]{.c7 .c28} {#h.3ei66bw8x0jb .c19}
==================================

[The architecture of ChatSQL is designed to be modular, flexible, and
scalable, emphasizing simplicity and efficiency in its components. Here
is a high-level overview of the anticipated system architecture:]{.c3}

[]{.c3}

[4.1 ]{.c48 .c12}[User Interface (UI) Module:]{.c12 .c31}

[Description: The UI module handles user interactions, providing a
seamless and intuitive interface for users to communicate with
ChatSQL.]{.c3}

[]{.c3}

[Components:]{.c3}

[]{.c3}

[HTML/CSS for layout and styling.]{.c3}

[Javascript for dynamic updates without full page reloads.]{.c3}

[TailWindCSS for streamlined styling.]{.c3}

[Interaction:]{.c3}

[]{.c3}

[Receives user queries and displays results.]{.c3}

[Communicates with the Backend Module for data retrieval.]{.c3}

[]{.c3}

[4.2 ]{.c12 .c48}[Backend Module:]{.c31 .c12}

[Description: The Backend Module serves as the core of ChatSQL, managing
the conversion of natural language to SQL, querying the Large Language
Model (LLM), and interacting with the database.]{.c3}

[]{.c3}

[Components:]{.c3}

[]{.c3}

[Flask framework for Python, handling HTTP requests and responses.]{.c3}

[Large Language Model (LLM) for natural language to SQL
conversion.]{.c3}

[Database connector for communication with selected databases.]{.c3}

[Interaction:]{.c3}

[]{.c3}

[Receives user queries from the UI Module.]{.c3}

[Utilizes the LLM for natural language to SQL conversion.]{.c3}

[Executes SQL queries on the chosen database.]{.c3}

[Sends results back to the UI Module.]{.c3}

[4.3 Natural Language Processing (NLP) Module:]{.c3}

[Description: The NLP Module focuses on interpreting and understanding
user queries in natural language.]{.c3}

[]{.c3}

[Components:]{.c3}

[]{.c3}

[Natural Language Processing algorithms and libraries.]{.c3}

[Interaction:]{.c3}

[]{.c3}

[Integrates with the Backend Module to provide accurate conversion from
natural language to SQL.]{.c3}

[Handles complex queries and table relationships.]{.c3}

[4.4 Security Module:]{.c3}

[Description: The Security Module ensures data privacy and protects
against unauthorized modifications.]{.c3}

[]{.c3}

[Components:]{.c3}

[]{.c3}

[User authentication mechanisms.]{.c3}

[Security protocols to restrict database operations.]{.c3}

[Interaction:]{.c3}

[]{.c3}

[Integrates with the Backend Module to enforce read-only
operations.]{.c3}

[Validates user access rights.]{.c3}

[4.5 Database Module:]{.c3}

[Description: The Database Module manages the connection to various
databases and executes SQL queries.]{.c3}

[]{.c3}

[Components:]{.c3}

[]{.c3}

[Database connector libraries.]{.c3}

[Database-specific drivers.]{.c3}

[Interaction:]{.c3}

[]{.c3}

[Communicates with the Backend Module to execute SQL queries.]{.c3}

[Retrieves data from the database.]{.c3}

[4.6 External Services:]{.c3}

[Description: External services, if any, may include third-party tools
or APIs that enhance functionality.]{.c3}

[]{.c3}

[Components:]{.c3}

[]{.c3}

[Potential integration with Prisma DB services for visualization.]{.c3}

[LLM API for natural language to SQL conversion.]{.c3}

[Interaction:]{.c3}

[]{.c3}

[May involve API calls for additional functionalities.]{.c3}

[Enhances system capabilities through external tools.]{.c3}

[4.7 Reused or 3rd Party Components:]{.c3}

[HTMX: Utilized in the UI Module for dynamic updates without full page
reloads.]{.c3}

[TailWindCSS: Employed for streamlined styling in the UI Module.]{.c3}

[Flask: Utilized as the web framework for the Backend Module.]{.c3}

[Large Language Model (LLM): Integrated into the NLP Module for natural
language to SQL conversion.]{.c3}

[Third-party database connectors: Used in the Database Module for
compatibility with various database types.]{.c3}

[4.8 Communication Flow:]{.c3}

[User Query:]{.c3}

[]{.c3}

[User interacts with the UI Module, posing queries in natural
language.]{.c3}

[NLP Conversion:]{.c3}

[]{.c3}

[The UI Module sends user queries to the NLP Module for
conversion.]{.c3}

[SQL Generation:]{.c3}

[]{.c3}

[The NLP Module converts queries into SQL and sends them to the Backend
Module.]{.c3}

[Database Interaction:]{.c3}

[]{.c3}

[The Backend Module interacts with the Database Module to execute SQL
queries.]{.c3}

[Security Checks:]{.c3}

[]{.c3}

[The Security Module ensures read-only operations and validates user
access rights.]{.c3}

[Result Presentation:]{.c3}

[]{.c3}

[The Backend Module sends query results back to the UI Module for
presentation to the user.]{.c3}

[]{.c3}

[5. High-Level Design]{.c7 .c29} {#h.sezggz2kqkbg .c19}
================================

[This section should set out the high-level design of the system. It
should include one or more system models showing the relationship
between system components and the systems and its environment. These
might be object-models, DFD, etc.]{.c3 .c32}

[5.1 System Model]{.c3}

[The high-level design of ChatSQL is represented through a system model
that illustrates the relationships between key components and their
interactions with the system and its environment.]{.c3}

[]{.c3}

[System Model]{.c3}

[]{.c3}

[Components:]{.c3}

[]{.c3}

[User Interface (UI):]{.c3}

[]{.c3}

[Receives user queries.]{.c3}

[Displays results to the user.]{.c3}

[Natural Language Processing (NLP) Module:]{.c3}

[]{.c3}

[Interprets user queries in natural language.]{.c3}

[Converts queries to SQL.]{.c3}

[Backend Module:]{.c3}

[]{.c3}

[Orchestrates the overall system functionality.]{.c3}

[Manages communication between UI, NLP, Security, and Database
Modules.]{.c3}

[Executes SQL queries.]{.c3}

[Security Module:]{.c3}

[]{.c3}

[Ensures data privacy and security.]{.c3}

[Validates user access rights.]{.c3}

[Database Module:]{.c3}

[]{.c3}

[Connects to various databases.]{.c3}

[Executes SQL queries.]{.c3}

[Retrieves and stores data.]{.c3}

[External Services:]{.c3}

[]{.c3}

[Integrates with third-party tools or APIs for enhanced
functionality.]{.c3}

[5.2 Data Flow Diagram (DFD)]{.c3}

[The Data Flow Diagram provides a visual representation of the flow of
data within the ChatSQL system.]{.c3}

[]{.c3}

[Data Flow Diagram]{.c3}

[]{.c3}

[Key Components:]{.c3}

[]{.c3}

[User Interaction:]{.c3}

[]{.c3}

[Users interact with the system by posing queries through the UI.]{.c3}

[SQL Generation:]{.c3}

[Database Interaction:]{.c3}

[]{.c3}

[The Backend Module communicates with the Database Module to execute SQL
queries.]{.c3}

[Security Checks:]{.c3}

[]{.c3}

[The Security Module ensures read-only operations and validates user
access rights.]{.c3}

[Result Presentation:]{.c3}

[]{.c3}

[The Backend Module sends query results to the UI for presentation to
the user.]{.c3}

[5.3 Object Model]{.c3}

[The Object Model provides an overview of the key objects and their
relationships within the system.]{.c3}

[]{.c3}

[Object Model]{.c3}

[]{.c3}

[Key Objects:]{.c3}

[]{.c3}

[User:]{.c3}

[]{.c3}

[Represents individuals interacting with the system.]{.c3}

[Query:]{.c3}

[]{.c3}

[Represents user queries in natural language.]{.c3}

[SQL Statement:]{.c3}

[]{.c3}

[Represents the SQL generated from user queries.]{.c3}

[Database:]{.c3}

[]{.c3}

[Represents the various databases available for querying.]{.c3}

[Result Set:]{.c3}

[]{.c3}

[Represents the data retrieved from the database in response to user
queries.]{.c3}

[Security Token:]{.c3}

[]{.c3}

[Represents authentication and user access rights.]{.c3}

[5.4 Interaction Flow]{.c3}

[The Interaction Flow diagram outlines the step-by-step flow of actions
and communication between system components during a typical user
interaction.]{.c3}

[]{.c3}

[Interaction Flow]{.c3}

[]{.c3}

[Interaction Steps:]{.c3}

[]{.c3}

[User Query:]{.c3}

[]{.c3}

[User interacts with the UI, posing a query.]{.c3}

[NLP Conversion:]{.c3}

[]{.c3}

[The UI sends the user query to the NLP Module.]{.c3}

[SQL Generation:]{.c3}

[]{.c3}

[The NLP Module converts the query into an SQL statement.]{.c3}

[Database Interaction:]{.c3}

[]{.c3}

[The Backend Module communicates with the Database Module to execute the
SQL.]{.c3}

[Security Checks:]{.c3}

[]{.c3}

[The Security Module validates user access rights.]{.c3}

[Result Presentation:]{.c3}

[]{.c3}

[The Backend Module sends query results to the UI for presentation to
the user.]{.c3}

[]{.c3}

[]{.c3}

[6. Preliminary Schedule]{.c29 .c7} {#h.bvnvssp3g8n .c19}
===================================

[This section provides an initial version of the project plan, including
the major tasks to be accomplished, their interdependencies, and their
tentative start/stop dates. The plan also includes information on
hardware, software, and wetware resource requirements.]{.c3 .c32}

[The project plan should be accompanied by one or more PERT or GANTT
charts.]{.c3 .c32}

[\#\#Link to compare different between pert chart and gantt chart\
\#\# I recommend doing pert chart]{.c3 .c32}

[[https://www.forbes.com/advisor/business/pert-chart-vs-gantt-chart/](https://www.google.com/url?q=https://www.forbes.com/advisor/business/pert-chart-vs-gantt-chart/&sa=D&source=editors&ust=1701452943519627&usg=AOvVaw35zdSVUJ6q3lOan6uG3_xU){.c15}]{.c14
.c7 .c12 .c32}

[7. Appendices]{.c29 .c7} {#h.qffi6xv1kj3n .c19}
=========================

[Specifies other useful information for understanding the requirements.
]{.c3 .c32}

[ ]{.c3}

[]{.c2}

::: {.c50}
[\[a\]](#cmnt_ref1){#cmnt1}[TODO: Add citation to references, add a link
to \'\[1\]\', which links to the reference.]{.c35 .c16 .c12}

[]{.c35 .c16 .c12}

[Perhaps there could be a better reference to use? This one is good
already since it comes from the official UC Berkley website.]{.c16 .c12
.c35}
:::

::: {.c50}
[\[b\]](#cmnt_ref2){#cmnt2}[Add LLM and SQL to glossary]{.c35 .c16 .c12}
:::
