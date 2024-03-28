# load library 
import json
import os
import pandas as pd
import traceback
import PyPDF2

import streamlit as st

from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain.callbacks import get_openai_callback
from dotenv import load_dotenv
from src.mcqgenerator.utils import read_file, get_table_data
from src.mcqgenerator.logger import logging



# load JSON Response
with open('.\Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

# Creating 