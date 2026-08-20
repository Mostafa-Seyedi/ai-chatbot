# 🤖 AI Chatbot

A full-stack AI chatbot web application built with **Django** and the **OpenAI API**.

The application provides authenticated users with a simple conversational interface where they can interact with an AI assistant while keeping their recent conversation history associated with their account.

The project demonstrates how to integrate an AI model into a Django application while working with authentication, databases, forms, templates, environment variables, and external APIs.

---

## ✨ Features

* 🤖 AI-powered responses using the OpenAI API
* 🔐 User authentication

  * Registration
  * Login
  * Logout
  * Password reset
* 💬 Interactive chatbot interface
* 🗂️ Per-user conversation history
* 🕒 Conversation timestamps
* 💾 Persistent storage using SQLite
* 🛡️ Protected chatbot routes for authenticated users
* 👤 Django user profiles
* ⚙️ Environment-variable based OpenAI API configuration
* 🧑‍💻 Django Admin support
* 📧 Password recovery support through email

---

## 🛠️ Tech Stack

| Technology              | Purpose                         |
| ----------------------- | ------------------------------- |
| Python                  | Backend programming language    |
| Django 5                | Web framework                   |
| OpenAI API              | AI response generation          |
| SQLite                  | Development database            |
| HTML / Django Templates | User interface                  |
| Django ORM              | Database interaction            |
| Django Authentication   | User accounts and sessions      |
| python-dotenv           | Environment variable management |

---

## 🧠 How It Works

The application follows a straightforward request flow:

```text
User
  │
  ▼
Django Authentication
  │
  ▼
Chat Interface
  │
  ▼
Django View
  │
  ├──► OpenAI API
  │       │
  │       ▼
  │    AI Response
  │
  ▼
Conversation Model
  │
  ▼
SQLite Database
  │
  ▼
Response displayed to user
```

When an authenticated user sends a message:

1. Django receives the submitted message.
2. The message is validated using `ChatForm`.
3. The backend sends the prompt to the OpenAI API.
4. OpenAI generates an assistant response.
5. The user's message and AI response are saved to the database.
6. The response is displayed in the chat interface.
7. The user's most recent conversations are loaded from the database.

Each conversation is connected to the authenticated Django user, keeping conversation records separated between accounts.

---

## 📁 Project Structure

```text
ai-chatbot/
│
├── ToDo.txt
│
└── chatproject/
    │
    ├── manage.py
    ├── requirements.txt
    ├── .env.example
    ├── .gitignore
    │
    ├── chatproject/
    │   ├── __init__.py
    │   ├── settings.py
    │   ├── urls.py
    │   ├── asgi.py
    │   └── wsgi.py
    │
    └── chatbot/
        ├── migrations/
        ├── templates/
        │   ├── chatbot/
        │   └── registration/
        │
        ├── __init__.py
        ├── admin.py
        ├── apps.py
        ├── authentication_views.py
        ├── forms.py
        ├── models.py
        ├── tests.py
        ├── urls.py
        └── views.py
```

### Main components

**`chatbot/views.py`**

Handles the main chatbot logic, including:

* receiving user messages
* communicating with OpenAI
* saving conversations
* loading conversation history

**`chatbot/models.py`**

Contains the database models for:

* `Conversation`
* `UserProfile`

**`chatbot/authentication_views.py`**

Handles authentication functionality such as:

* account registration
* login
* logout

**`chatproject/settings.py`**

Contains the Django configuration, database settings, OpenAI API key loading, authentication configuration, and email configuration.

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Mostafa-Seyedi/ai-chatbot.git
cd ai-chatbot/chatproject
```

---

### 2. Create a virtual environment

Creating a virtual environment is strongly recommended.

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 OpenAI API Configuration

The chatbot requires an OpenAI API key.

Create a `.env` file inside the `chatproject` directory:

```text
chatproject/
├── manage.py
├── .env
├── .env.example
└── ...
```

Add your API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

> **Important:** Never commit your real API key to GitHub.

The application loads the key from the environment in Django settings:

```python
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```

The `.env.example` file can be used as a template for local configuration.

---

## 🗄️ Database Setup

The project uses **SQLite** by default, so no separate database server is required for local development.

Apply the Django migrations:

```bash
python manage.py migrate
```

If you make changes to the models:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

## 👑 Create an Admin User

To access the Django Admin panel, create a superuser:

```bash
python manage.py createsuperuser
```

Follow the prompts to choose a username, email address, and password.

---

## ▶️ Run the Application

Start the Django development server:

```bash
python manage.py runserver
```

Django will normally start the development server on:

```text
http://127.0.0.1:8000/
```

Open it in your browser.

You can then create an account, log in, and begin chatting with the AI assistant.

---

## 🔐 Authentication

The chatbot is protected using Django's authentication system.

Users must log in before accessing the chat interface.

Main application routes include:

| Route              | Purpose                           |
| ------------------ | --------------------------------- |
| `/`                | Home / authentication entry point |
| `/login/`          | User login                        |
| `/register/`       | Create an account                 |
| `/logout/`         | Log out                           |
| `/chatbot/`        | AI chatbot                        |
| `/password-reset/` | Password recovery                 |
| `/admin/`          | Django Admin                      |

The chatbot view uses Django's `login_required` protection, preventing unauthenticated users from accessing conversations.

---

## 💬 Conversation Storage

Every successful interaction is stored in the database using the `Conversation` model.

A conversation contains:

```text
Conversation
├── user
├── user_input
├── bot_response
└── timestamp
```

Because each conversation is connected to a Django `User`, users only see their own conversation history.

The current interface retrieves the **five most recent conversations** for the logged-in user.

---

## 👤 User Profiles

The project also contains a `UserProfile` model associated with Django's built-in user model.

It currently provides fields for:

```text
preferred_language
chat_theme
created_at
```

This provides a foundation for future personalization features such as language preferences and configurable chat themes.

---

## 🤖 OpenAI Integration

The chatbot uses the official OpenAI Python library.

The current implementation sends a system instruction and the user's message to the configured chat model.

Conceptually:

```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": user_input
        }
    ]
)
```

The returned assistant message is then saved together with the original user input.

> The model is currently configured directly in the chatbot view and can easily be changed or moved to an environment/configuration variable in a future version.

---

## 📧 Password Reset & Email

Django's password-reset views are included in the project.

For real email delivery, configure valid SMTP credentials in your Django settings or move them into environment variables.

For development, Django's console email backend can also be used so password-reset emails are printed directly to the terminal instead of being sent.

Example:

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

This is particularly useful while developing locally.

---

## 🧪 Running Tests

Run Django's test suite with:

```bash
python manage.py test
```

As the project grows, tests should cover areas such as:

* authentication
* access control
* conversation ownership
* chatbot form validation
* OpenAI API error handling
* database persistence

---

## 🔒 Security Notes

When using this project outside local development:

* Never commit `.env` files.
* Never expose your OpenAI API key.
* Store `SECRET_KEY` in an environment variable.
* Set `DEBUG=False`.
* Configure `ALLOWED_HOSTS`.
* Store email credentials in environment variables.
* Use HTTPS in production.
* Configure a production-ready database if necessary.
* Add rate limiting before exposing the chatbot publicly.
* Consider usage limits to prevent unexpected OpenAI API costs.

The current configuration is intended primarily for **development and learning**, not a production deployment without additional security configuration.

---

## 🛣️ Roadmap

Potential improvements for future versions include:

* [ ] Upgrade the configured OpenAI model
* [ ] Preserve full multi-message conversation context
* [ ] Add streaming AI responses
* [ ] Allow users to create multiple chat sessions
* [ ] Add conversation titles
* [ ] Delete individual conversations
* [ ] Clear conversation history
* [ ] Search previous conversations
* [ ] Add Markdown rendering for AI responses
* [ ] Add syntax highlighting for code
* [ ] Implement dark mode using the existing profile preference
* [ ] Add language selection
* [ ] Add API usage and rate limits
* [ ] Improve automated test coverage
* [ ] Add Docker support
* [ ] Add production deployment configuration
* [ ] Add CI/CD with GitHub Actions
* [ ] Simplify and clean the dependency list

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

A typical contribution workflow is:

1. Fork the repository.
2. Create a new branch.

```bash
git checkout -b feature/my-feature
```

3. Make your changes.
4. Commit them.

```bash
git commit -m "Add my feature"
```

5. Push your branch.

```bash
git push origin feature/my-feature
```

6. Open a Pull Request.

For larger changes, opening an issue first to discuss the idea is recommended.

---

## 🐛 Issues

Found a bug or have an idea for an improvement?

Open a GitHub Issue and include:

* a clear description of the problem
* steps to reproduce it
* expected behavior
* actual behavior
* relevant error messages
* screenshots when useful
* your Python and operating-system versions

---

## 📚 What This Project Demonstrates

This repository is useful as a practical example of combining several common backend-development concepts:

* Django project architecture
* Django authentication
* protected routes
* form processing
* relational data models
* Django ORM queries
* environment variables
* third-party API integration
* AI-generated responses
* per-user data isolation
* error handling
* server-rendered templates

It can serve as a foundation for building more advanced AI assistants, customer-support bots, personal assistants, educational tools, or other AI-powered Django applications.

---

## 📄 License

This repository currently does not include a license file.

If the project is intended for public reuse or open-source contributions, adding a `LICENSE` file is recommended.

---

## 👨‍💻 Author

**Mostafa Seyedi**

GitHub: `Mostafa-Seyedi`

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

Contributions and feedback are always welcome.

---

<p align="center">
  Built with Python, Django, and OpenAI 🤖
</p>
