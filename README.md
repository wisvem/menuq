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
