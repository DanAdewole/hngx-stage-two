# Hngx-stage-two

Simple CRUD Task. <br>

A Simple CRUD API to create a Person object with the attribute name.

## Table of Contents

- [Important Submission Links](#important-submission-links)
- [Steps for local installation](#steps-for-local-installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [License](#license)

## Important Submission Links

- ERD and UML Diagrams on LucidChart: []()
- Live URL: [https://hng-task-two-5pjl.onrender.com/api](https://hng-task-two-5pjl.onrender.com/api)
- Postman Documentation: [https://documenter.getpostman.com/view/16678700/UUy3Aq7o](https://documenter.getpostman.com/view/16678700/UUy3Aq7o)

## Steps for local installation

1. Clone the repository:

   ```
   git clone https://github.com/DanAdewole/hngx-stage-two.git
   ```

2. Navigate to the project directory:

   ```
   cd hngx-stage-two
   ```

3. Create a virtual environment:

   ```
   python -m venv ./venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```
     source venv/bin/activate
     ```

5. Install the project dependencies:

   ```
   pip install -r requirements.txt
   ```

6. Run database migrations:

   ```
   python manage.py migrate
   ```

7. Start the development server:

   ```
   python manage.py runserver
   ```

8. Access the API in POSTMAN at `http://127.0.0.1:8000/api`.

## Usage

Check [DOCUMENTATION.md](DOCUMENTATION.md)

## Technologies Used

- Django
- Django Rest Framework
- Python

## License

This project is licensed under the [MIT License](LICENSE).

---
