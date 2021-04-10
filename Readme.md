# :wave: Project Local Setup

:point_right: You'll need Python installed (Preferably Python 3.6 or higher version)

Create a virtual environment:

```sh
python3 -m venv senv
```

To start the virtual environment on Windows:

```sh
name\Scripts\activate
```

Clone this repository:

```sh
git clone https://github.com/kothawleprem/StudentsBay.git
```

Enter into the directory:

Install requirements:

```sh
pip install -r requirements.txt
```

Migrations:

```sh
py manage.py makemigrations
```

```sh
py manage.py migrate
```

Create Super User:

```sh
py manage.py createsuperuser
```

-> Enter any required information.

Run:

```sh
python manage.py runserver
```

Locally available at 127.0.0.1:8000

Thanks :raised_hands:
