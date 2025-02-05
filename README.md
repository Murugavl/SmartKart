# SmartKart

SmartKart is a Django-based e-commerce platform that allows users to browse and purchase products. The project uses MySQL as the database backend.

## Features
- User authentication (Login/Signup)
- Product catalog with categories
- Add to cart functionality
- Admin panel for managing products and orders

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS
- **Database**: MySQL

## Installation

### Prerequisites
Ensure you have the following installed:
- Python 3.10+
- MySQL Server
- pip (Python package manager)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/Murugavl/SmartKart.git
   cd SmartKart
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   venv\Scripts\activate
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure the database settings in `settings.py`:
   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'your_database_host',
           'PORT': '3306',
       }
   }
   ```

5. Apply migrations:
   ```sh
   python manage.py migrate
   ```

6. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
   Follow the prompts to set up an admin account.

7. Run the development server:
   ```sh
   python manage.py runserver
   ```
   Access the application at `http://127.0.0.1:8000/`.

## Usage
- Users can browse products, add them to the cart, and place orders.
- Admins can manage products and orders via the Django admin panel (`/admin`).


## Contributing
1. Fork the repository.
2. Create a new branch:
   ```sh
   git checkout -b feature-branch
   ```
3. Make changes and commit:
   ```sh
   git commit -m "Added new feature"
   ```
4. Push to the branch:
   ```sh
   git push origin feature-branch
   ```
5. Create a pull request.

## License
This project is licensed under the MIT License.
