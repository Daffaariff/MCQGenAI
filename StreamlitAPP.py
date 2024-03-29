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
from src.mcqgenerator.MCQGenerator import generate_evaluate_chain


# load JSON Response
with open('.\Response.json', 'r') as file:
    RESPONSE_JSON = json.load(file)

# Title app
st.title("MCQs App with langchain")

#create a form 
with st.form('users_input'):
    uploaded_file=st.file_uploader('Upload a PDF or txt file')

    mcq_count=st.number_input('No. of MCQs', min_value=3, max_value=10)

    subject=st.text_input("Insert Subject", max_chars=26)

    tone=st.text_input('Complexity level of Questions', max_chars=20, placeholder="Simple")

    button=st.form_submit_button('Create MCQs')

    # make sure all of the input have been filled 

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("Running...!!!"):
            try: 
                text = read_file(uploaded_file)

                with get_openai_callback() as cb:
                    response = generate_evaluate_chain(
                        {
                            'text': text,
                            'number': mcq_count,
                            'subject': subject,
                            'tone': tone,
                            'response_json': json.dumps(RESPONSE_JSON)
                        }
                    )

                    print(f"Total Tokens:{cb.total_tokens}")
                    print(f"Prompt Tokens:{cb.prompt_tokens}")
                    print(f"Completion Tokens:{cb.completion_tokens}")
                    print(f"Total Cost:{cb.total_cost}")

                    if isinstance(response, dict):
                        # Extract the quiz data from Response
                        quiz = response.get('quiz', None)
                        if quiz is not None:
                            table_data = get_table_data(quiz)
                            if table_data is not None:
                                df = pd.DataFrame(table_data)
                                df.indexer = df.index + 1
                                st.table(df)
                                # st.text_area(label="Review", value=response["review"])
                            else:
                                st.error('Error in the table data')
                    else:
                        st.write(response)

            except Exception as e:
                traceback.print_exception(type(e), e, e.__traceback__)
                st.error('Error')