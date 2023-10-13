# School of Computing
## CA326 Year 3 Project Proposal Form

### SECTION A

**Project Title:** ChatSQL: Smart Data Chatbot

- **Student 1 Name:** Georgijs Pitkevics
  - **ID Number:** 19355266

- **Student 2 Name:** Chee Hin Choa
  - **ID Number:** 21100497


**Staff Member Consulted:** Brian Davis

### Project Description (1-2 pages):

ChatSQL is a smart data assistant that redefines how users interact with databases. ChatSQL is a user-friendly assistant that the user can talk to and engage in conversation about data and databases, without requiring extensive knowledge of databases or SQL.

**The core principles of ChatSQL:**

1. **User-Centric Design:** ChatSQL is catered to people with minimal IT literacy. The only two skills required are the ability to upload a file to a web page and send a message, ensuring users with minimal technical proficiency can interact with databases.

2. **Understanding of Natural Language:** ChatSQL is capable of understanding natural language and taking in the user’s queries in English without the need for SQL input.

3. **Data Privacy and Security:** ChatSQL is designed to only query the database, without the ability to perform modifications or deletions of tables or data within the database to protect it from unintentional or malicious modification.

**How it works:**

1. User selects the database they wish to query, e.g., `covid-vaccinations.sqlite3`.
2. The user can ask the chatbot a question about the database, e.g., "What was the average vaccination rate in Dublin?"
3. The chatbot queries our chosen Large Language Model (LLM) which converts natural language into an SQL query and replies with the result in natural language form, e.g., "The average vaccination rate in Dublin is 95.4%." Conversation can continue further if the user requires more information.

**Example scenario:**

A startup’s Data Analyst is on annual leave. The Project Manager needs information on some data for an upcoming meeting with stakeholders. The data analyst has preloaded the databases onto ChatSQL. The project manager goes onto the company's configuration of ChatSQL and queries the chatbot about the data he needs for his meeting. ChatSQL allows the PM to understand the data so that he can get ready for his meeting without bothering the Data Analyst.

### Division of Work

Outlines how the work is envisaged to be split equally among the team members:

We will work simultaneously together to approach this task so that we stay on the right track. The complex parts of the project can be grouped into:

1. **"Natural Language to SQL" LLM development:** This may include Natural Language Processing (NLP) as well as 1-2 LLMs to generate an SQL statement from a given sentence, with the option to utilize the table names taken from the database for better accuracy and efficiency.

2. **HTML/HTMX/TailWindCSS Frontend:** UI/UX design, implementing the chat UI, making it easy to understand and use for first-time users. Tying it in with the backend with HTMX and WebSockets (Flask SocketIO).

3. **Flask backend:** Overall structure of the code to handle the POST/GET requests from the frontend, hosting the web application, handling networking to and from the client, and implementing the "Natural language to SQL" within the Web Application as well as handling database access.

4. **Security Layer:** This will be an important undertaking in implementing security measures within the web application to ensure the user cannot modify or delete data from the database, e.g., filtering out and refusing to perform requests such as 'DROP TABLE your_table_name'.

Chee Hin will undertake task 2, and Georgijs will undertake tasks 3 & 4. While we are dividing the main workload, we will first develop the LLM functionality (Task 1) together in a pair programming approach to ensure we both understand how the essential functionality of ChatSQL works.

### Programming language(s)

List the proposed language(s) to be used:

- Python
- HTML
- HTMX
- CSS
- JavaScript (Optional)
- TailWindCSS
- SQL/SQLite/PostgreSQL Databases

### Programming tool(s)

List tools (compiler, database, web server, etc.) to be used:

- Github - for version control, tracking changes during development
- Visual Studio Code - IDE for writing, debugging, and managing your code effectively
- Powershell/Bash Terminal - for testing the Flask application locally during development stages
- Potential research into utilizing Prisma DB services to better visualize the models and their associated databases, e.g., user login, chat history, SQL generation history with accompanying prompts.

### Learning Challenges

List the main new things (technologies, languages, tools, etc) that you will have to learn:

Developing ChatSQL will be an exciting and equally challenging learning opportunity for the two of us. Here are the main challenges that we expect to encounter:

1. **HTMX:** HTMX is a fairly new up-and-coming tool based on hypertext that handles "AJAX, CSS Animations, WebSockets, and Server Sent Events directly in HTML." This will allow us to speed up the development of the application as it eliminates the need for JavaScript altogether, giving us more flexibility in our choice of technologies and time to develop/refine features.

2. **TailWindCSS:** TailWind is a modern CSS framework which offers a unique way of styling web applications directly within the HTML. We'll need to become familiar with this framework to design an appealing and easy-to-use interface.

3. **Flask:** Flask is a Python web framework that we'll be utilizing to create the backend of our web app. It offers a multitude of additional libraries such as 'Flask Socket-IO', 'Flask Login', and 'SQLAlchemy'. It will be quite challenging to learn how to utilize it for this project, however, we believe this is the best framework for this, as Python is one of the best languages for utilizing LLMs and NLP.

4. **User Experience:** To stay true to our core principle of User-Centric Design, we need to research and understand how to create an intuitive user-friendly interface that is easy to use and requires no prior training by utilizing UI design guidelines as well as a simple prompting system that the average user can understand from the moment they enter the application.

5. **Large Language Model (LLM):** We will need to research LLMs and how they work. We need to decide whether we will use an off-the-shelf LLM like OpenAI’s GPT-4 API, which would prove more efficient for hardware, meaning we would not have to worry about using powerful GPUs for computation, or if we would like to have the model run locally on the webserver, utilizing open source models like the many that can be found on huggingface.co and further trained.

6. **Database Administration:** To work with various databases, we need to understand how they work and what level of complexity in SQL statements we need to aim for when querying databases.

### Hardware / software platform

State the hardware and software platform for development, e.g., PC, Linux, etc.

- Personal machines/laptops:
  - Georgijs will utilize his Windows 11 Laptop and Dualboot (Windows 11 & Arch Linux) Desktop
  - Chee Hin will utilize his Linux (Ubuntu 22.04.2 LTS) Laptop

We plan to look into Jupyter Notebook (as found in Google Colab) for research and development of the LLM functionality.

### Special hardware / software requirements

Describe any special requirements.

- **Note 1:** In general, the School of Computing is not in a position to supply and support special hardware/software for 3rd-year projects. Accordingly, any special needs should be provided by the students and discussed with your supervisor.

- **Note 2:** It is assumed that all projects will be developed/demonstrated using standard lab machines. Students may use their hardware, but all projects must be demonstrated in a School of Computing lab, either on a lab machine or the student's machine.

**NOT APPLICABLE**
