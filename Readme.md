# 🧐 Fact vs Opinion Analyzer

An interactive AI-powered application that classifies user statements as **Fact**, **Opinion**, or **Ambiguous** — and even fetches supporting evidence for fact-based claims. Built with **LangChain components** (Chains, Runnables, Prompt Templates, Output Parsers, etc) and deployed with a sleek **Streamlit UI**.

---

## 🚀 Features

- ✅ **Fact vs Opinion Classification**
- 🔎 **Evidence Fetching for Facts**
- 🛡️ **Misinformation & Moderation Layer**
- 🎨 **Streamlit UI with Background Customization**

---

## 🛠️ Tech Stack

- **LangChain**: PromptTemplates, Conditional Chains, Runnables, Output Parsers
- **OpenAI ChatModel**: Core LLM behind the scenes
- **DuckDuckGo Search API**: Fetch supporting evidence for facts
- **Streamlit**: Clean, responsive user interface

---

## ⚙️ How It Works

1. User enters a statement.
2. **Classifier Chain** labels it as *Fact*, *Opinion*, or *Ambiguous*.
3. **Conditional Chain** routes the input:
   - **Fact** → triggers evidence fetching + AI explanation with supporting URLs.
   - **Opinion** → generates a balanced counter-opinion explanatory AI response.
   - **Ambiguous** → prompts the user with a clarifying question.
4. Results are displayed in the Streamlit interface with dynamic styling.

---

## 📂 Project Structure

```
📦 fact_vs_opinion_analyzer
 ┣ 📂 code
 ┃ ┣ 📜 app.py                               # Streamlit app entrypoint. Routing logic for fact, opinion, ambiguous
 ┃ ┣ 📜 InformationClassifier.py             # classifier class with Pydantic output validation
 ┣ 📂 templates                              # Centralized prompt templates
   ┣ 📜 prompt_template_ambiguous.py         # Prompt template for response to ambiguous claims
   ┣ 📜 prompt_template_opinion.py           # Prompt template for response to opinion claims
   ┣ 📜 prompt_template_fact.py              # Prompt template for response to factual claims with supporting evidence from DDGS
   ┣ 📜 prompt_template_classifier.py        # Prompt template for classification of user statement
 ┣ 📜 prompt_template_amb.json               # Generated prompt in json format
 ┣ 📜 prompt_template_opinion.json           # Generated prompt in json format
 ┣ 📜 prompt_template_fact.json              # Generated prompt in json format
 ┣ 📜 prompt_template.json                   # Generated prompt in json format
 ┣ 📜 requirements.txt                       # Python dependencies
 ┗ 📜 README.md                              # Project documentation
```

---

## ▶️ Getting Started

1. Clone this repo:
   ```bash
   git clone https://github.com/your-username/fact-vs-opinion-analyzer.git
   cd fact-vs-opinion-analyzer
   ```
2. Create and activate virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app/main.py
   ```

---

## 🎯 Example Use Cases

- **Detect misinformation**: Quickly verify whether viral statements are factual or opinionated.
- **Education tool**: Teach students the difference between facts and opinions.
- **Content moderation**: Flag ambiguous or misleading claims in online platforms.

---

## 📸 Demo

| Input Statement | Classification | Example Output |
|-----------------|----------------|----------------|
| "The Eiffel Tower is in Paris." | Fact | ✅ Evidence with supporting URLs |
| "Python is the best programming language." | Opinion | 🤔 Balanced counter-opinion |
| "Aliens built the pyramids." | Ambiguous | ❓ Requests clarification + analysis |

**Screenshots/GIFs:**

- <img width="1160" height="780" alt="app_look" src="https://github.com/user-attachments/assets/a6b8f2ec-5130-4c9e-ae73-b656a0a2e53d" />
- <img width="851" height="728" alt="app_fact" src="https://github.com/user-attachments/assets/d0c5f8ed-9570-4c88-b8cc-8e2d293af3e5" />
- <img width="801" height="586" alt="app_opinion" src="https://github.com/user-attachments/assets/4111d2b6-7d23-490c-b8ee-0bc08cbad872" />
- <img width="762" height="494" alt="app_ambiguous" src="https://github.com/user-attachments/assets/f8117b91-189b-45fe-886b-e004c85a15f9" />


---

## 🤝 Contributing

Contributions are welcome! Fork this repo, open issues, or submit PRs to improve features or add new modules.

---

## 📜 License

This project is licensed under the MIT License.
