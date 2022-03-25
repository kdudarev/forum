# Forum

**[Forum](https://github.com/kdudarev/forum)** is a discussion board where people with similar interests can create and discuss various topics.  You can reply to any member's comment and like any topic.

### Technology Stack:
- **[Python](https://www.python.org/)** - programming language (3.9.6)
- **[HTML](https://html.com/)** - markup language (HTML5)
- **[Django](https://www.djangoproject.com/)** - Python Web framework (4.0.3)
- **[PostgreSQL](https://www.postgresql.org/)** - object-relational database system (PostgreSQL 14)
- **[Bootstrap](https://getbootstrap.com/)** - HTML, CSS and JavaScript framework (django-bootstrap4 22.1)

# Installation

**1. Clone this repository:**
```
git clone https://github.com/kdudarev/forum.git
```
**2. Change SECRET_KEY in settings.py:**
```
SECRET_KEY = "Your Secret Key"
```
**3. Change DATABASES in settings.py to yours or use the example:**
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```
**4. Use virtualenv to install requirements:**
```
pip install -r requirements.txt
```
**5. Run the migration:**
```
python manage.py migrate
```
**6. Create super user:**
```
python manage.py createsuperuser
```
**7. Start the server:**
```
python manage.py runserver
```
