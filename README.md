# Online Medical Sheba (OMS)

## Overview
Online Medical Sheba (OMS) is a Django-based web application that provides medical services, including appointment booking, ambulance services, medicine store management, and hospital information. The platform enables doctors and patients to connect easily and manage healthcare online.

## Repository Details
**Name**: Online Medical Sheba (OMS)  
**Description**: A Django-based healthcare platform for online medical services, including appointments, ambulance booking, and medicine management.  
**Owner**: Ashaduzzaman Ashik  
**License**: MIT License  

## Features
- **User Authentication**: Custom user model with profile management.
- **Appointments**: Patients can book appointments with doctors.
- **Ambulance Services**: Availability and booking of ambulances.
- **Medicine Store**: Users can order medicines online.
- **Hospital Management**: Information about hospitals and available facilities.
- **Payments**: Online payment integration.

## Technologies Used
- **Backend**: Django, Python
- **Database**: MySQL (MariaDB via XAMPP)
- **Frontend**: HTML, CSS, JavaScript
- **Other Tools**: Bootstrap, jQuery

## Installation Guide
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/Online-Medical-Sheba.git
   cd Online-Medical-Sheba
   ```
2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Configure database settings**:
   - Open `oms_project/settings.py`
   - Update `DATABASES` to match your MySQL configuration.
5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```
6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```
7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Contribution
Feel free to contribute by submitting issues and pull requests. Ensure to follow best coding practices.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

# LICENSE (MIT License)

```
MIT License

Copyright (c) 2025 Ashaduzzaman Ashik

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

