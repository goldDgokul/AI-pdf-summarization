# AI-pdf-summarization
I built a local-first PDF AI Summarizer using Streamlit, Ollama, and LangChain. I originally planned to use the Google Gemini API but pivoted to Ollama for 100% privacy and zero API costs. My app extracts text from a PDF, chunks it, and uses my local llama3:8b model to summarize each chunk. Finally, it combines these into one cohesive summary.
