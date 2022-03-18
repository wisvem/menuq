# menuq

- Debug
```json
{
  "configurations": [
    {
      "name": "menuq",
      "type": "python",
      "request": "launch",
      "program": "${workspaceFolder}/manage.py",
      "args": ["runserver", "--settings=menuq.settings.dev"],
      "django": true
    }
  ]
}
```

- setup.py
```python
#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='menuq',
    version='1.0.0',
    description='menuq package',
    author='Wiston Venera Macías',
    author_email='wisvem@hotmail.com',
    packages=find_packages(),
    scripts=['manage.py']
)
```
