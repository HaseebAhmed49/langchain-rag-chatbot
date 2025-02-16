# **🚀 LangChain RAG Customer Chatbot**  

Welcome to the **LangChain RAG Customer Chatbot** project! This repository contains the code for a customer support chatbot powered by LangChain, OpenAI, and Retrieval-Augmented Generation (RAG). The chatbot integrates with a knowledge base to provide accurate and contextually relevant responses to user queries.  

![image](https://github.com/user-attachments/assets/4e31fb85-c117-47a3-8c22-02741018f1a9)

---

## **Table of Contents**  
1. [Project Overview](#project-overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Setup Instructions](#setup-instructions)  
5. [Backend Code](#backend-code)  
6. [Frontend Code](#frontend-code)  
7. [Knowledge Base](#knowledge-base)  
8. [Running the Application](#running-the-application)  
9. [Future Enhancements](#future-enhancements)  
10. [Contributing](#contributing)  
11. [Contact](#contact)  

---

## **Project Overview**  
This project demonstrates how to build a customer support chatbot using:  
- **LangChain**: For integrating large language models (LLMs) and retrieval-augmented generation (RAG).  
- **OpenAI GPT-4**: For generating natural language responses.  
- **FastAPI**: For the backend API.  
- **Streamlit**: For the frontend user interface.  
- **FAISS**: For efficient similarity search in the knowledge base.  

The chatbot retrieves information from a knowledge base (stored as a JSON file) and uses OpenAI's GPT-4 to generate responses.  

---

## **Features**  
- **Retrieval-Augmented Generation (RAG):** Combines retrieval from a knowledge base with generative AI for accurate and context-aware responses.  
- **Interactive Chat Interface:** Built with Streamlit for a seamless user experience.  
- **Scalable Backend:** FastAPI ensures high performance and scalability.  
- **Customizable Knowledge Base:** Easily update the knowledge base with new questions and answers.  

---

## **Tech Stack**  
- **Backend:** FastAPI, LangChain, OpenAI, FAISS  
- **Frontend:** Streamlit  
- **Knowledge Base:** JSON  
- **Environment:** Python, dotenv  

---

## **Setup Instructions**  

### **Prerequisites**  
1. Python 3.8 or higher installed.  
2. An OpenAI API key. You can get one from [OpenAI's website](https://platform.openai.com/).  

### **Steps**  
1. Clone the repository:

   ```bash
   git clone https://github.com/haseebahmed49/langchain-rag-chatbot.git
   cd langchain-rag-chatbot
   ```
2. Create a Virtual Environment
  ```bash
    python -m venv venv
    source venv/bin/activate
  ```

3. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```  

4. Create a `.env` file in the root directory and add your OpenAI API key:  
   ```plaintext
   OPENAI_API_KEY=your_openai_api_key_here
   ```  

5. Add your knowledge base to `backend/knowledge_base.json`. See the [Knowledge Base](#knowledge-base) section for an example.  

---

## **Backend Code**  
The backend is built using FastAPI and LangChain. It handles user queries by retrieving relevant information from the knowledge base and generating responses using OpenAI's GPT-4.  

---

## **Frontend Code**  
The frontend is built using Streamlit and interacts with the backend API to display the chatbot interface.  

---

## **Knowledge Base**  
The knowledge base is stored in `backend/knowledge_base.json`. It contains a list of questions and answers in JSON format.  

### **Example Knowledge Base**  
```json
[
    {
        "question": "What is your return policy?",
        "answer": "Our return policy allows you to return products within 30 days of purchase for a full refund."
    },
    {
        "question": "How do I track my order?",
        "answer": "You can track your order by logging into your account and visiting the 'Order History' section."
    }
]
```  

---

## **Running the Application**  
1. Start the backend server:  
   ```bash
   uvicorn backend.main:app --reload
   ```  

2. Start the frontend:  
   ```bash
   streamlit run frontend/app.py
   ```  

---

## **Future Enhancements**  
1. **Dynamic Knowledge Base Updates:** Integrate with a CMS or database for real-time updates.  
2. **Multi-Source Integration:** Combine multiple data sources (e.g., FAQs, product manuals).  
3. **Feedback Loop:** Allow users to rate responses for continuous improvement.  
4. **Advanced NLP:** Use fine-tuned models for industry-specific queries.  

---

## 🚀 **Contributing**
- Fork this repository
- Submit a pull request with enhancements
- Open issues for discussions

🔗 GitHub Repo: **[(https://github.com/haseebahmed49/langchain-competitor-analysis-pipeline)]**  

#LangChain #OpenAI #FastAPI #Streamlit #Automation

---

## 📞 **Contact**
👤 **Haseeb Ahmed**  
📍 **Location:** Greater London, UK  
📧 **Email:** haseebahmed02@gmail.com  
🔗 **LinkedIn:** [Haseeb Ahmed49](https://www.linkedin.com/in/haseebahmed49/)  
🔗 **GitHub:** [HaseebAhmed49](https://github.com/HaseebAhmed49)


**Happy coding! 🚀**  
