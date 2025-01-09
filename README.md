# Courier Management System Project

This project is a **Courier Management System (CMS)** built using **Python**, **Django**, and **SQLite3** as the database. The web application is designed to help courier and logistical services companies manage and track packages more efficiently, reducing paperwork and increasing operational efficiency.

## Features

- Admin Panel: The admin can log in to the system and add receiver information such as name, ID number, and other relevant details. 
- Package Tracking: After the admin enters the receiver information, it is stored in the database. Users can track the status of their packages using a tracking ID.
- Package Status: The system provides a real-time update of the package status.
- Optimized Delivery Routes: It automates the planning and optimization of delivery routes.
- Communication: The system sends notifications to both the sender and receiver about the status of the delivery.
- Order and Billing: The system generates a unique tracking ID for each order, which users can use to track the delivery.
- Access Control: Only the admin has access to the system to manage and process courier requests.

## Modules

1. Admin Login:
   - Admin can log in to manage the system and handle orders.
   - Admin has the ability to view all order details, including sender, receiver, package details, and payment information.

2. User Login/Registration:
   - Users can register an account and log in to track the status of their packages.
   - Users can enter their information for delivery and get updates on their package.

3. Order Management:
   - The system allows the admin to enter the details of the order and generate a tracking ID for each order.
   - Users can enter the tracking ID to check the current status of their delivery.

4. Package Tracking:
   - Users and admin can track the package in real-time by using the unique tracking ID.
   - The status of the package is updated and can be accessed instantly.

5. Billing System:
   - The system generates a bill for each package, including delivery charges and other details.
   - The bill is automatically created when an order is placed, and users can access it through the system.

## Technologies Used

- Python**: The programming language used for building the backend of the system.
- SQLite3: A lightweight relational database management system used to store the data.

