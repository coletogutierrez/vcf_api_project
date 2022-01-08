=============
django-vcfapi
=============

VCFAPI is a simple Django app to conduct Web-based VCFAPI.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "vcfapi" to your INSTALLED_APPS setting like this:

      INSTALLED_APPS = (
          ...
          'vcfapi',
      )

2. Include the vcfapi URLconf in your project urls.py like this::

      url(r'^vcfapi/', include('vcfapi.urls')),

3. Run `python manage.py makemigrations` to create the vcfapi models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
  to create items (you'll need the Admin app enabled).


