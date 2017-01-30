from setuptools import setup


setup(
    name='flake8-import-order-spoqa',
    version='1.0.0',
    description="Spoqa's import order style for flake8-import-order",
    url='https://github.com/spoqa/flake8-import-order-spoqa',
    author='Hong Minhee',
    author_email='hong.minhee' '@' 'gmail.com',
    maintainer='Spoqa',
    maintainer_email='dev' '@' 'spoqa.com',
    license='GPLv3 or later',
    py_modules=['flake8_import_order_spoqa'],
    install_requires=['flake8-import-order'],  # TODO: version specifier
    entry_points='''
        [flake8_import_order.styles]
        spoqa = flake8_import_order_spoqa:Spoqa
    ''',
    test_suite='flake8_import_order_spoqa.TestCase',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Flake8',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',  # noqa
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Quality Assurance',
    ]
)