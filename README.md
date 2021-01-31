# bot

If ports are occupied, find PID FOR 5005/5055:
```
lsof -i tcp:5055
```

and run `kill -9 PID`

To start it together:
```
rasa run -m models --enable-api --cors "*" --debug & rasa run actions
```