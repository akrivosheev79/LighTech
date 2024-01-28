# Test task from LighTech
_This code decides tasks described in <a href="https://docs.google.com/document/d/1zCC8fZwi9Zs2I77d-NbQP0GXVYQ7dI_snYO1g-fFjTg/mobilebasic"> this technical requirements </a>. You can test API running code local by uvicorn server. For this you might do next some steps._

## Installation
### Install python
I sure you know how to do it

### Clone repo
```commandline
$ git clone https://github.com/akrivosheev79/LighTech.git
```

### Install dependencies
```commandline
$ pip install -r requirements.txt
```

### Run server
```commandline
$ python main.py
```

### Check responsibility

Be sure that all is OK opening link `http://{any_your_host_ip}}:8080/` in your favorite browser
Your might see message "Welcome". API documentation you can see in `http://{any_your_host_ip}}:8080/docs`

### Create users

For testing API you need at least two users. Empty database will create automatically while you will 
run server so for create test users invoke `user/signup` POST endpoint. Specification for do it
you can see [here](http://localhost:8080/docs).

## Testing

__*While following all below steps use [documentation](http://localhost:8080/docs) You will find
ready to use `curl` code snippets there*__ 

### Login
Sign in by created user to API by invoke signin endpoint and save your token. 
It will be needed in future steps

### Increase balance
To increase balance authorizated user invoke `transaction/new` endpoint

### Transfer money
To transfer money another user invoke `transaction/transfer` endpoint

### Inspect balance
To retrieve balance of current authorizated user invoke `transaction/retrieve` endpoint

## Neglect
1. Developer doesn't check sign of pay. So user balance can be negative.
2. Developer did all finance operations without distribution manager transactions. 
So it possible when user's balance will update, but transaction detail won't commit to DB. We all
understand inadmissibility that in production.
3. There are no any logging functionality in this API. To do it in production.
4. Server port and ip address was hardcode for simplicity. In production config will need. 

## License
Only LighTech employees or outsourcing by them employees can use this API