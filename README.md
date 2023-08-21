# Diversity Management System

Welcome to the Diversity Management System, a Django-based web application for managing diversity information within educational modules.

## Table of Contents
- [Project Overview](#project-overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The Diversity Management System is a web application designed to help educational institutions track diversity data within various modules. It provides features for creating, updating, and deleting module data and related diversity information. The application also includes interactive charts for visualizing diversity statistics.

## Features

- User authentication and access control.
- Create, update, and delete educational modules.
- Add diversity information to each module, including ethnic group and student count.
- Interactive charts for visualizing diversity statistics.
- Admissions team members can manage module and diversity data.
- Users can view a list of modules and their diversity information.
- ... (List any additional features here)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/diversity-management-system.git

cd diversity-management-system
python -m venv venv

#on windows
venv\Scripts\activate

#on mac
source venv/bin/activate

pip install -r requirements.txt

#database setup
python manage.py migrate


python manage.py createsuperuser


python manage.py runserver

Usage
Log in with the superuser account created during installation.
Use the application to manage modules and diversity information.
Navigate to different views, such as module lists, diversity details, and charts.
Create, update, and delete modules and diversity data as needed.
Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

Fork the repository.
Create a new branch for your feature/bugfix.
Make your changes and commit them.
Push your branch to your forked repository.
Open a pull request on the main repository.
License
This project is licensed under the MIT License.

