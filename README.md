# AI-pdf-summarization
I built a local-first PDF AI Summarizer using Streamlit, Ollama, and LangChain. I originally planned to use the Google Gemini API but pivoted to Ollama for 100% privacy and zero API costs. My app extracts text from a PDF, chunks it, and uses my local llama3:8b model to summarize each chunk. Finally, it combines these into one cohesive summary.

# 📄 PDF AI Summarizer (Local-First with Ollama)

This is a web-based application I built with Streamlit and LangChain that allows you to upload any PDF, extract its text, and generate various types of AI-powered summaries.

This project runs **100% locally** using Ollama and the Llama 3 model, ensuring your data remains completely private and there are no API costs.

## 💡 The Journey: From Google Gemini to Ollama

I originally started this project with the goal of using the Google Gemini API. You can still see remnants of this in the code (like `check_models.py` and old comments in `summarizer.py`). However, due to difficulties in acquiring a working API key, I pivoted the project to a "local-first" approach.

By switching to **Ollama** and **LangChain**, the application gained several new advantages:
* **Privacy-Focused:** No data is ever sent to a third-party server. The entire summarization process happens on your local machine.
* **No API Costs:** Run as many summaries as you want for free.
* **Offline Capable:** Once the model is downloaded, the app can run without an internet connection.

## ✨ Features

* **PDF Upload:** Easily upload PDF documents from your computer.
* **Multiple Summary Types:**
    * **Brief:** A concise 2-3 sentence summary.
    * **Detailed:** A thorough summary covering key arguments and findings.
    * **Bullet Points:** An organized list of main points.
    * **Executive:** A high-level summary for business leaders.
* **Smart Chunking:** Handles very large PDFs by splitting them into manageable chunks and then combining the results for a cohesive final summary.
* **Document Analysis:** Provides a high-level analysis of the document's type, themes, and target audience.
* **Key Quote Extraction:** Pulls out the most important quotes or statements from the text.
* **Export Results:** Download the final summary as a `.txt` file or a `.csv` of the processing statistics.

## 🛠️ Technology Stack

* **Framework:** Streamlit
* **AI Orchestration:** LangChain
* **LLM:** Ollama (`llama3:8b`)
* **PDF Processing:** PyPDF2
* **Text Processing:** Tiktoken, Pandas

## 🚀 How to Run

### 1. Prerequisites

You must have **Ollama** installed and running on your system.

1.  [Download and install Ollama](https://ollama.com/).
2.  Pull the `llama3:8b` model (which I used in `summarizer.py`) by running this in your terminal:
    ```sh
    ollama pull llama3:8b
    ```
3.  Ensure the Ollama application is running in the background.

### 2. Project Setup

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/your-username/your-project-name.git](https://github.com/your-username/your-project-name.git)
    cd your-project-name
    ```

2.  **Create a virtual environment:**
    ```sh
    python -m venv .venv
    ```
    *On macOS/Linux:*
    ```sh
    source .venv/bin/activate
    ```
    *On Windows:*
    ```sh
    .\.venv\Scripts\activate
    ```

### 3. Install Dependencies

[cite_start]The `requirements.txt` file [cite: 2] in the repo is from before I switched to Ollama. **Replace** the contents of your `requirements.txt` file with the following:

**`requirements.txt`**
```text
streamlit>=1.28.0
langchain>=0.0.350
langchain-community
langchain-ollama
python-dotenv>=1.0.0
PyPDF2>=3.0.1
pandas>=2.0.0
tiktoken>=0.5.0

```
### now run the commands in terminal 
```

1 FIRST
pip install -r requirements.txt

2 SECOND
streamlit run app.py


```
## 📂 File Structure

```
.
├── app.py              # The main Streamlit application logic
├── summarizer.py       # Core AI logic (LangChain + Ollama)
├── pdf_processor.py    # PDF text extraction and chunking
├── utils.py            # Helper functions for Streamlit display and exports
[cite_start]├── requirements.txt    # List of Python dependencies [cite: 2]
[cite_start]├── .gitignore          # Tells Git to ignore files (like .env) [cite: 3]
[cite_start]├── .env                # (Remnant) Was used for my Google API Key [cite: 1]
└── check_models.py     # (Remnant) A helper script I wrote to test the Google API


