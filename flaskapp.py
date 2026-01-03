from flask import Flask
import redis
import os


app = Flask(__name__)
r = redis.Redis(host='redis', port=6379)

@app.route('/')
def welcome():
  return 'Welcome to Flask + Redis App'

@app.route('/count')
def count():
  count = r.incr('visits')
  return f'Amount of visits {count}'

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5002)

















# import os
# from flask import Flask
# import redis

# app = Flask(__name__)

# r = redis.Redis(
#     host="redis",
#     port=6379,      
#     db=0,
#     decode_responses=True,
# )


# r = redis.Redis(
#     host=os.getenv("REDIS_HOST", "redis"),
#     port=int(os.getenv("REDIS_PORT", "6379")),
#     db=int(os.getenv("REDIS_DB", "0")),
#     decode_responses=True,
# )

# @app.route("/")
# def index():
#     return "Welcome to the Flask + Redis app!"


# @app.route("/count")
# def count():
#     visits = r.incr("visits")
#     return f"Visit count: {visits}"


# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5002)
