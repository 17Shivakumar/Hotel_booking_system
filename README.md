# Hotel Room Booking System - Django
Overview

A simple Django-based hotel booking system that allows users to book rooms, manage availability, and view booking details.

Features
	•	Hotel, Room, and Booking Management
	•	Automatic Room Availability Updates
	•	Search & Filter by Location/Availability
	•	Booking Confirmation Page
	•	Admin Panel for Managing Bookings
	•	Django Messages for Notifications

Technologies Used
	•	Django, SQLite/MySQL, HTML, CSS, Bootstrap

Setup
	1.	Clone the Repository

git clone https://github.com/yourusername/hotel-booking-system.git
cd hotel-booking-system

	2.	Install Dependencies & Run Server

python -m venv venv  
source venv/bin/activate  # On Windows use `venv\Scripts\activate`  
pip install -r requirements.txt  
python manage.py migrate  
python manage.py runserver  

	3.	Access the App
	•	User Interface: http://127.0.0.1:8000/
	•	Admin Panel: http://127.0.0.1:8000/admin/
