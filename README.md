# onlineChat
Chat room website

## Install

Guide to install the project as localhost

### Requirements

- Python3
- Django version > 4
- Docker
- package Daphne 
```console
sudo apt-get install python3-daphne
```

### Redis

The project needs Redis to be able to send each user the messages.
Install the Redis 5 image, and run it in a container.

```console
docker pull redis:5
docker run -p 6379:6379 redis:5
```

### Website

Clone the project locally.
Inside the main directory onlineChat/ , run 
```python
python3 manage.py runserver
```
You have now acess to the website at localhost:8000
You can now create an account, sign in, join a room and chat


## Docker

I initially wanted to create a signe container for all the project, but unfortunately, I couldn't make that possible.
I left the docker-compose.yml, the Dockerfile and the requirement.txt I used.

With the docker version of the project, you will be able to access the website and log in, but the chat will not work. An error occure on sent message, and users will not recieve it.
