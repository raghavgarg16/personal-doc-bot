""" All Application Constants declare here... """

# Python Packages
from decouple import config


# App Constants
APP_ENV                         =   config('APP_ENV')
APP_SECRET_KEY                  =   config('APP_SECRET_KEY')


# OpenAI Constants
OPENAI_API_KEY		            =	config('OPENAI_API_KEY')
