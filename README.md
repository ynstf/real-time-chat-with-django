# Chat Project

## Description

A real-time chat application built with Django, Django Channels, and Redis for message brokering. This project demonstrates a simple chat system with WebSocket support.

## Features

- Real-time chat rooms
- WebSocket communication
- Redis for message brokering
- User authentication

## Installation

1. **Clone the Repository:**
   ```
   git clone https://github.com/ynstf/real-time-chat-with-django.git
   ```

2. **Navigate to the Project Directory:**
   ```
   cd real-time-chat-with-django
   ```

3. **Create a Virtual Environment:**
   ```
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

5. **Install the Requirements:**
   ```
   pip install -r requirements.txt
   ```

6. **Run Migrations:**
   ```
   python manage.py migrate
   ```

7. **Start the Server:**

   - For redis:
     ```
     cd redis-windows
     redis-server.exe redis.conf
     ```
   - For development:
     ```
     python manage.py runserver
     ```
   - For production (using Daphne):
     ```
     daphne -p 8000 chat_project.asgi:application
     ```

## Configuration

Update `settings.py` with your environment-specific settings, such as Redis configuration.

## Contributing

Feel free to contribute by creating a pull request or opening an issue.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
