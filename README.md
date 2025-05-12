# E-Commerce Platform

A full-featured e-commerce platform built with Django, featuring product management, category organization, and a user-friendly shopping interface.

## Features

- **Product Management**
  - Product catalog with categories
  - Detailed product listings with images
  - Stock management
  - Price tracking
  - Product availability status
  - Data integrity protection
  - Category relationship validation

- **Category Management**
  - Hierarchical category organization
  - Category-specific product listings
  - Category images and descriptions
  - Protected category deletion
  - Category validation

- **User Interface**
  - Responsive design
  - Product search and filtering
  - Shopping cart functionality
  - User-friendly navigation

## Technical Stack

- **Backend**: Django 5.1.7
- **Database**: SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Additional Features**: 
  - Image handling
  - URL routing
  - Admin interface
  - Data validation
  - Error handling

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd E_COMM
```

2. Create and activate virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run the development server:
```bash
python manage.py runserver
```

## Project Structure

```
E_COMM/
├── accounts/         # User authentication
├── category/         # Category management
├── store/           # Product management
├── templates/       # HTML templates
├── static/         # Static files (CSS, JS, images)
├── media/          # User-uploaded files
└── E_COMM/         # Project settings
```

## Usage

1. Access the admin interface at `/admin`
2. Add categories and products
3. Browse products at the store page
4. View product details and manage inventory

## Recent Updates

- Enhanced product model with improved category handling
- Added validation for product-category relationships
- Implemented data integrity protection
- Improved error handling for product updates
- Added category protection to prevent accidental deletion
- Implemented model validation for data consistency

## Model Changes

### Product Model
- Added category relationship protection
- Implemented validation for category existence
- Added data integrity checks
- Improved error handling for product updates
- Added fallback URL handling for products without categories

### Category Model
- Protected against accidental deletion
- Added validation for category relationships
- Improved data consistency checks

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 