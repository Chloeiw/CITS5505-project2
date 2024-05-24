## CITS5505 Project2 - IntelliShare

## Group Members

| UWA Id   | Student Name | Github Username |
| -------- | ------------ | --------------- |
| 24019456 | Chloe Wu     | Chloeiw         |
| 23966753 | Yifan Gao    | GAOYifan10062   |
| 23687777 | Ho Yeung Law | jasonlawhy      |
| 23955182 | Melo Xue     | tivxuee         |

## Application Introduction

### Purpose of Design

IntelliShare is an app for willing learners. It allows you to post your questions about all fields when you encounter any questions or have any ideas in life or study, and get answers of expertise spanning every conceivable topic from netizens all over the world. Also, if you are an expert in one area, you can also answer questions for others, engaging with a vibrant community of experts, enthusiasts, and learners alike.
In a universe brimming with questions, curiosities, and insights, IntelliShare can satisfy your knowledge desire. It is a bustling digital marketplace of ideas where minds converge to learn, share, and grow together, connecting seekers and sharers of knowledge.

### Summary of Architecture

The first version of the App has five feature modules, which are as follows:

1. **The account module**
   In this module, users can create new accounts, log in, and modify account information, such as avatar, and user name.
2. **The post-question module**
   In this module, users can publish their issues and questions in many fields by editing their titles, content, and even cover images.
3. **The answer module**
   In this module, users can write only text comments on a question.
4. **The searching module**
   In this module, users can search for the question and reply by inputting keywords of the title.
5. **The information feed**
   The feed feature allows users to browse recommended questions and their answers. The Recommended contents are presented based on a simple ranking algorithm: prioritize matching user interest with problem classification, then recommend according to the latest time in the database.

 **wireframe drawing**
 https://www.figma.com/design/037QbF52714lWJ2t7Aw0OL/IntelliShare?node-id=0-1&t=SJKTDwLkZQLGTXQA-1

 **UI design**
 https://app.zeplin.io/project/662fb9c824b5ce0de500f801

### Models

**Table: users**

| Column Name  | Data Type | Constraints                 |
| ------------ | --------- | --------------------------- |
| id           | INT       | AUTO_INCREMENT, PRIMARY KEY |
| username     | CHAR(50)  | NOT NULL                    |
| password     | CHAR(20)  | NOT NULL                    |
| image        | VARCHAR   | NOT NULL                    |


**Table: question**

| Column Name | Data Type         | Constraints                 |
| ----------- | ----------------- | --------------------------- |
| id          | INT               | AUTO_INCREMENT, PRIMARY KEY |
| title       | VARCHAR           | NOT NULL                    |
| subtitle    | VARCHAR           | NOT NULL                    |
| content     | VARCHAR           | NOT NULL                    |
| cover       | VARCHAR           | NOT NULL                    |
| post_time   | CURRENT_TIMESTAMP | NOT NULL                    |
| category_id | INT               | NOT NULL                    |
| user_id     | INT               | NOT NULL                    |

**Table: answer**

| Column Name | Data Type         | Constraints                 |
| ----------- | ----------------- | --------------------------- |
| id          | INT               | AUTO_INCREMENT, PRIMARY KEY |
| comment     | VARCHAR           | NOT NULL                    |
| answer_time | CURRENT_TIMESTAMP | NOT NULL                    |
| user_id     | INT               | NOT NULL                    |
| question_id | INT               | NOT NULL                    |

**Table: category**

| Column Name | Data Type | Constraints                 |
| ----------- | --------- | --------------------------- |
| id          | INT       | AUTO_INCREMENT, PRIMARY KEY |
| name        | VARCHAR   | NOT NULL                    |

**Table: userInterest**

| Column Name | Data Type | Constraints                 |
| ----------- | --------- | --------------------------- |
| id          | INT       | AUTO_INCREMENT, PRIMARY KEY |
| user_id     | INT       | NOT NULL                    |
| category_id | INT       | NOT NULL                    |



### **Routes**

#### 1. Homepage

> Route Path URL: /

Description: The homepage is the main landing page of the application. It provides an overview of the website's content and features, such as featured questions, popular categories, and recent activity.

#### 2. Register

> Route Path URL: /register

Description: The register page allows new users to create an account on the website. Users can fill out a registration form with their desired username, password, and other relevant information.

#### 3. Login

> Route Path URL: /login

Description: The login page provides a way for registered users to log into their accounts. Users can enter their username and password to authenticate and gain access to their personalized features and content.

#### 4. Question

> Route Path URL: /question/{question_id}

Description: The question page displays a specific question identified by its unique question_id. It showcases the question's title, content, comments, and related answers. Users can interact with the question by posting comments and providing answers.

#### 5. Profile

> Route Path URL: /profile/{username}

Description: The profile page showcases a user's profile information and activity. It displays details such as the user's username, profile picture, bio, and a list of their posted questions and answers. Other users can view profiles to learn more about each other.

#### 6. Search

> Route Path URL: /search

Description: The search page allows users to search for specific content within the application. Users can enter keywords or filters to find relevant questions, answers, users, or categories. The search results are displayed in a structured manner.

### **APIs**

### 1. Register API

-   **Endpoint:** `/register`
-   **Method:** POST
-   **JSON Data:**

```
{
  "username": "example_username",
  "password": "example_password",
}
```

-   **Description:** This API allows a user to register an account on the website. It expects a JSON payload containing the user's registration information, such as username, password, and additional details. Upon successful registration, a new user record will be created.

### 2. Login API

-   **Endpoint:** `/login`
-   **Method:** POST
-   **JSON Data:**

```
{
  "username": "example_username",
  "password": "example_password",
}
```

-   **Description:** This API handles user authentication. Users can submit their login credentials (username and password) in a JSON payload to this endpoint. If the credentials are valid, the API will generate a session token or authentication token and return it in the response. The token can be used for subsequent requests to authenticate the user.

### 3. Logout API

-   **Endpoint:** `/logout`
-   **Method:** POST
-   **JSON Data:**

```
{
  "username": "example_username",
}
```

-   **Description:** This API invalidates the user's current session or authentication token, effectively logging them out of the application. It requires the user to be authenticated, either by including the session token or authentication token in the request headers or through another form of authentication.

### 4. Create Question API

-   **Endpoint:** `/createQuestion`
-   **Method:** POST
-   **JSON Data:**

```
{
  "title": "example_question_title",
  "subtitle": "example_question_subtitle",
  "content": "example_question_content",
  "category_id": "example_category_id",
  "user_id": "example_user_id"
}
```

-   **Description:** This API allows an authenticated user to create a new question. The user must provide the necessary details of the question, such as the title, content, and category ID, in a JSON payload. Upon successful creation, the API will store the question in the database and return the newly created question's details.

### 5. Answer Question API

-   **Endpoint:** `/answerQuestion`
-   **Method:** POST
-   **JSON Data:**

```
{
  "question_id": "example_question_id",
  "answer_text": "example_answer_text"
  "user_id": "example_user_id"
}
```

-   **Description:** This API enables an authenticated user to provide an answer to a specific question. The user needs to include the question ID and their answer text in a JSON payload. The API will validate the request and store the answer in the database, associating it with the corresponding question and user.

### 6. Delete Question API

-   **Endpoint:** `/delQuestion/{question_id}`
-   **Method:** DELETE
-   **Description:** This API allows an authenticated user to delete their own question. The user needs to provide the question ID as part of the endpoint URL. The API will verify ownership and delete the question from the database, along with its associated answers and comments.

### 7. Search Question API

-   **Endpoint:** `/searchQuestion`
-   **Method:** POST
-   **Description:** This API enables users to search for questions based on specific criteria. Users can include search parameters in the request query string, such as keywords, category, or other filters. The API will query the database and return a list of relevant questions that match the search criteria.

## Instruction for Launching

> start app using `flask` cmd

in repo foler run cmd below

```
flask --app intelliShare run --debug
```

## Instruction for Testing

test Flask app using cmd as below

```
pytest
```

we test 5 apis:

> test_home  `GET`

> test_registration `POST`

> test_question `POST`

> test_answer `POST`

> test_search `POST`


