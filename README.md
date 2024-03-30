# 📝 MCQs Generator with Langchain 🤖

This project is a Multiple Choice Questions (MCQs) generator built using the Langchain library, powered by OpenAI GPT-3.5 Turbo. The generator is integrated into a Streamlit web application, allowing users to easily create MCQs based on provided text inputs.

## 🌟 Overview

The MCQs Generator utilizes advanced natural language processing techniques provided by OpenAI's GPT-3.5 Turbo model to generate MCQs based on given text inputs. Users can specify various parameters to customize the generated MCQs, such as the number of questions, subject, and tone.

## 🚀 Usage

To use the MCQs Generator, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine.

**Install Dependencies**: Make sure you have Python installed. Install the required dependencies using pip:

   ```bash
   conda create --name <your_env_name> python=3.8
   source activate <your_env_name>
   pip install -r requirements.txt
   ```

3. **Set Up OpenAI API Key**: Obtain an API key from OpenAI and set it as an environment variable at .env file within `OPENAI_API_KEY`.

4. **Run the Streamlit App**: Launch the Streamlit web application by running the following command:

```bash
   streamlit run StreamlitAPP.py
```

5. **Input Parameters**: Fill in the required parameters in the web application.
    - **Upload File**: Upload a PDF or text file containing the input text.
    - **No. of MCQs**: Specify the number of multiple-choice questions to generate.
    - **Subject**: Provide the subject/topic for the generated MCQs.
    - **Complexity Level**: Specify the complexity level or tone for the questions (e.g., Simple, Intermediate, Advanced).


6. **Generate MCQs**: Click on the "Create MCQs" button to generate the MCQs based on the provided inputs.

7. **Review and Evaluate**: Review the generated MCQs and evaluate their complexity and suitability using the provided analysis.

## 📦 Dependencies

- langchain
- openai
- streamlit

## 📄 License

This project is licensed under the [MIT License](LICENSE).
