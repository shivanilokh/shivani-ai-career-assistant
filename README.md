# Shivani AI Career Assistant

## 1. What the Agent Does

Shivani AI Career Assistant is an AI-powered career assistance application built with Streamlit. It helps users get career-related guidance and answers through a simple conversational interface.

The application is designed to provide quick, easy-to-understand career assistance using a knowledge file and an AI model.

## 2. Who It Is For

The application is intended for:

- Students exploring career options
- Beginners preparing for data and AI-related roles
- Job seekers looking for career guidance
- Users who want quick answers to career-related questions

## 3. Project Structure

```text
shivani-ai-career-assistant/
│
├── app.py
├── knowledge.txt
├── requirements.txt
├── BUILD_LOG.md
├── .gitignore
└── README.md
```

## 4. How to Set Up

### Step 1 — Clone the repository

```bash
git clone https://github.com/shivanilokh/shivani-ai-career-assistant.git
cd shivani-ai-career-assistant
```

### Step 2 — Install the required packages

```bash
pip install -r requirements.txt
```

### Step 3 — Configure the required AI credentials

Set up the required API/model credentials used by the application before running the app.

Do not commit private API keys or access tokens to GitHub.

### Step 4 — Run the Streamlit application

```bash
streamlit run app.py
```

The application will open in the browser.

## 5. How to Use

1. Open the Streamlit application.
2. Enter a career-related question.
3. Submit the question.
4. The assistant processes the request using the application knowledge and AI model.
5. Review the generated response.

### Example

Example question:

```text
What skills are important for a Data Analyst role?
```

The assistant returns an AI-generated career-related response.

## 6. Simple Architecture

```text
User
  ↓
Streamlit Interface
  ↓
Question Processing
  ↓
Knowledge / Context
  ↓
AI Model
  ↓
Generated Response
  ↓
User
```

The main application logic is implemented in `app.py`, while supporting career information is stored in `knowledge.txt`.

## 7. Design Decision

A key design decision was to keep the application focused on career assistance instead of building a general-purpose chatbot.

This makes the purpose of the application clear and keeps the user experience simple and focused.

## 8. Evaluation

The updated version of the application was evaluated during the project.

The evaluation results are documented with the project deliverables and are used to assess the quality of the updated assistant.

## 9. Limitations

The assistant has several limitations:

- AI-generated responses may sometimes be incomplete or inaccurate.
- The assistant depends on the information available in its knowledge/context and the underlying AI model.
- Career information can change over time, so important information should be independently verified.
- The application is a prototype and is not intended to replace a professional career advisor.
- The system should not be used as the sole basis for important career decisions.

## 10. AI Transparency

This application uses an AI model to generate responses to user questions.

AI-generated responses may contain errors or outdated information. Users should verify important information from reliable sources before making decisions.

## 11. Demo

A live end-to-end demonstration of the application is provided as part of the FL-09 submission.

The demo shows the application running, a user question being submitted, the generated response, one design decision, and one limitation.

## 12. Project Files

- `app.py` — main Streamlit application
- `knowledge.txt` — supporting career knowledge/context
- `requirements.txt` — Python dependencies
- `BUILD_LOG.md` — project build notes
- `README.md` — project documentation
