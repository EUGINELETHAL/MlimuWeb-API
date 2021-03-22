M-limu 
======
M-limu is  mobile learning management platform designed to improve performance of  students across Kenya.Learning is designed to take place via  sms and web platforms.Our goal is to help young people in Africa use education to transform their lives. To do this, we use technology to make their learning easier, quicker and more efficient.

Out of 10 people in Africa, only 3 have internet access. We focus on the 7. Mtabe is a startup that uses a and SMS technology to deliver learning content to students who cannot afford textbooks and do not have internet access. We have made it so simple that an average African student does not need to master a new technology or get a new device to start using Mtabe.

A django rest  service built with DRF and Africa's talking Api


.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


:License: MIT


Settings
--------



Basic Commands
--------------



Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy m_limu

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest


Celery
^^^^^^

This app comes with Celery.

To run a celery worker:

.. code-block:: bash

    cd m_limu
    celery -A config.celery_app worker -l info

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.




Deployment
----------

The following details how to deploy this application.


Heroku
^^^^^^

See detailed `cookiecutter-django Heroku documentation`_.

.. _`cookiecutter-django Heroku documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-on-heroku.html





