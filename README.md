# Hngx-stage-two
Simple CRUD Task.

<p>A Simple CRUD API to create a Person object with the attribute name.</p>

## Important Submission Links

- ERD and UML Diagrams on LucidChart: []()

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

8. Start the development server:

   ```
   python manage.py runserver
   ```

9. Access the API in POSTMAN at `http://127.0.0.1:8000/`.

## Usage

Check [DOCUMENTATION.md](DOCUMENTATION.md)

## Technologies Used

- Django
- Django Rest Framework
- Python

## License

This project is licensed under the [MIT License](LICENSE).

---
