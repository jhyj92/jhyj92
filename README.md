Hello! 👋 This repository now hosts a proof-of-concept backend for an AI-driven local services marketplace in Australia. The backend is built with Django and provides REST APIs for user management, service listings, and bookings.

**The Project:**

This is a personal project focused on learning the fundamentals of mobile app creation.

**Why Contribute?**

* **Witness a Learning Process:** See how a mobile app takes shape from the ground up.
* **Beginner-Friendly Context:** A good opportunity for others learning mobile development.
* **Collaborative Environment:** Open to insights, suggestions, and contributions.
* **Live Deployment (Eventually):** The project will be deployed via Vercel, allowing you to see progress.

**Current Stage:**

Currently exploring backend fundamentals with Django Rest Framework.

**How You Can Help:**

* Offer feedback and ideas.
* Report any issues that arise.
* Suggest potential improvements.

**Getting Involved (For Developers):**

1.  Clone the repository.
2.  Navigate to the project directory.
3.  Setup instructions will be provided as the project evolves.

**Future Direction:**

The project will progress through iterative development and feature implementation. The current version includes:

* User registration and JWT-based login
* CRUD APIs for service listings
* Booking endpoints to schedule services
* Simple search and filtering

Thank you for your interest in this learning endeavor! 😊

## Quickstart

1.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

2.  Apply migrations and create a superuser:

    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

3.  Run the development server:

    ```bash
    python manage.py runserver
    ```

APIs will be available under `/api/`.
