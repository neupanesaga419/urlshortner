# URL Shortener

A Django-based URL shortening service that allows users to create short, manageable links from long URLs.

## Features

- Create short URLs from long URLs

## Prerequisites

Before running this project, make sure you have the following installed:

- Python 3.8 or higher
- pip (Python package installer)

## Installation and Setup

### 1. Clone the Repository

```bash
git clone <this-repo-url>
cd urlshrotner
```

### 2. Create a Virtual Environment

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create Environment File

Create a `.env` file in the root directory of the project:

```bash
# On Windows
echo. > .env

# On macOS/Linux
touch .env
```

Add the following environment variables to your `.env` file:

```env
DJANGO_SECRET_KEY=your-secret-key-here

```

**Note**: Replace `your-secret-key-here` with a secure Django secret key. You can generate one using Python:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 5. Run Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

To access the admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up your admin credentials.

### 7. Run the Development Server

```bash
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000/`

## Usage

1. **Access the Application**: Open your web browser and navigate to `http://127.0.0.1:8000/`

2. **Shorten a URL**: 
   - Enter a long URL in the input field
   - Click "Shorten URL" to generate a short link

3. **Use the Short URL**: Copy the generated short URL and use it to redirect to the original long URL



## Project Structure

```
urlshrotner/
├── core/                    # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View logic
│   ├── urls.py             # URL routing
│   └── migrations/         # Database migrations
├── templates/              # HTML templates
│   └── shorten.html        # Main page template
├── static/                 # Static files
│   ├── css/
│   │   
│   └── js/
│       
├── urlshrotner/            # Django project settings
│   ├── settings.py         # Project configuration
│   └── urls.py             # Main URL configuration
├── manage.py               # Django management script
├── requirements.txt        # Python dependencies
└── README.md              
```

## Development



### Making Migrations

If you modify the models, create new migrations:

```bash
python manage.py makemigrations
python manage.py migrate
```



## Environment Variables


- `DJANGO_SECRET_KEY`: Django secret key


## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request



## Support

If you encounter any issues or have questions, please open an issue on the project repository. 