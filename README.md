# Django REST Authentication System

An advanced authentication system built with Django REST Framework (DRF), featuring JWT token-based authentication and a robust password reset mechanism.

## Features

- **JWT Token Authentication**: Secure user login and token management.
- **Password Reset**: A seamless password recovery process with email verification.
- **User Registration**: Flexible user signup with validation.
- **Account Management**: Update and manage user details efficiently.
- **Secure API Endpoints**: Fully protected endpoints using DRF permissions.

## Installation

Follow these steps to set up the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/7amota/Django-REST-Authentication-System.git
   cd Django-REST-Authentication-System
   ```

2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

4. Start Redis:
   ```bash
   redis-server
   ```

5. Run Celery worker:
   ```bash
   celery -A project_name worker --loglevel=info
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

### API Endpoints

- **User Registration**:
  - Endpoint: `POST /api/register/`
  - Payload: `{ "username": "", "password": "", "email": "" }`

- **Login**:
  - Endpoint: `POST /api/token/`
  - Payload: `{ "email": "", "password": "" }`

- **Password Reset**:
  1. Request Reset:
     - Endpoint: `POST /auth/email_request/`
     - Payload: `{ "email": "" }`
  2. Check Reset OTP:
     - Endpoint: `POST /auth/check_otp/`
     - Payload: `{ "token": "", "otp": "" }`
  3. Change Password:
     - Endpoint `POST /auth/reset_password/`
     - Playload `{"token":"","new_password":""}`
      
### Highlight: Reset Password Feature
The password reset feature ensures a secure workflow:
1. User requests a reset using their email.
2. A unique otp is sent via email.
3. caching otp and token in redis
4. User submits the token and new password to complete the process.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feat/name`
3. Commit your changes: `git commit -m 'feat:name'`
4. Push to the branch: `git push origin feat/name`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

### Questions or Suggestions?
Feel free to open an issue or contact the maintainer via the repository.
