# FL-07 Build Log — Shivani AI Career Assistant

## Project

Shivani AI Career Assistant

## Goal

Build a working AI career assistant that can answer questions about Shivani Lokhande's skills, projects, education, work experience and career direction.

---

## Day 1 — Initial Build

### What I built

* Created a Streamlit application.
* Connected the application to Gemini.
* Created a separate knowledge base file called `knowledge.txt`.
* Added Shivani's skills, projects, education and experience to the knowledge base.
* Added instructions to prevent the assistant from inventing information.

### What worked

* Streamlit application launched successfully.
* Gemini API connection worked.
* The assistant generated answers to questions about Shivani.

### What I tested

* Skills
* Projects
* Machine learning projects
* Work experience
* Unknown company/experience information

---

## Iteration

### Problem

The initial version used the `gemini-2.5-flash` model, but the Gemini API returned a 404 error because that model was no longer available to new users.

### Change

Updated the model from `gemini-2.5-flash` to `gemini-3.6-flash`.

### Result

The application successfully connected to the available Gemini model and generated responses.

### Second Improvement

The assistant could potentially answer using general model knowledge instead of only Shivani's information.

### Change

Created a separate `knowledge.txt` file and instructed the assistant to use it as the primary source.

### Reason

This makes the assistant more grounded in Shivani's actual information and reduces the chance of hallucinating personal information.

---

## Final Testing

The agent was tested with questions about:

* Technical skills
* Machine learning projects
* Work experience
* Career-related information
* Information that was not present in the knowledge base

### Test Results

The agent successfully generated answers using the connected `knowledge.txt` file.

The agent was also tested with information that was not present in the knowledge base. It was instructed not to invent unsupported information and to clearly indicate when information was unavailable.

The successful tests confirmed that the core question-answering workflow was working end to end.

---

## Features Cut From Initial Spec

The following features were not included in the MVP:

* Voice input
* Resume upload
* Email integration
* Advanced UI
* Multiple external APIs
* Automated job application features

### Reason

The FL-07 MVP focuses on making the core question-answering workflow work end to end before adding additional features.

---

## Final MVP

The current agent can:

1. Receive a career-related question.
2. Read the connected knowledge base.
3. Send the question and knowledge to Gemini.
4. Generate an answer.
5. Display the answer in the Streamlit interface.

The MVP uses `knowledge.txt` as its connected data source.

---

## Current Status

The core MVP is working successfully in the local Streamlit environment.

Next steps are:

* Push the project to GitHub.
* Deploy the application using Streamlit Community Cloud.
* Test the deployed version.
* Submit the working agent, build log and raw run capture.
