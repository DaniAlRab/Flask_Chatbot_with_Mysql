### Explicação Detalhada do Funcionamento da API do Projeto **Chatbot FAQ System**

Este projeto consiste em uma **API Flask** que interage com um **banco de dados MySQL** para fornecer respostas automáticas a perguntas frequentes (**FAQ**). A API permite que usuários consultem perguntas cadastradas, adicionem novas perguntas e obtenham respostas automaticamente.

---

## 🔹 **Fluxo de Funcionamento da API**
1. O usuário faz uma **requisição HTTP** para a API.
2. A API recebe essa requisição e verifica a ação solicitada (exemplo: buscar resposta para uma pergunta ou cadastrar uma nova FAQ).
3. Se a ação envolver **banco de dados**, a API realiza uma consulta ao **MySQL**.
4. A API retorna a resposta ao usuário no formato **JSON**, que pode ser interpretado por um sistema web ou outro software.

---

## 🔹 **Endpoints da API**
A API possui diferentes **endpoints**, ou seja, URLs específicas que permitem interações com o banco de dados.

### **1️⃣ Consultar Resposta do Chatbot**
#### **🖥️ Endpoint:** 
```plaintext
POST /chat
```
#### **📌 Como funciona?**
- O usuário envia uma **pergunta** no corpo da requisição.
- A API pesquisa no banco de dados por uma resposta correspondente.
- Caso encontre a resposta, retorna ao usuário.
- Se não encontrar, retorna uma mensagem informando que a pergunta não está cadastrada.

#### **📌 Exemplo de Requisição:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"question": "Qual seu nome?"}' http://127.0.0.1:5000/chat
```

#### **📌 Exemplo de Resposta JSON:**
```json
{
  "answer": "Eu sou o ChatBot, aqui para ajudar você!"
}
```

---

### **2️⃣ Listar Todas as Perguntas e Respostas**
#### **🖥️ Endpoint:** 
```plaintext
GET /faqs
```
#### **📌 Como funciona?**
- O usuário acessa esse endpoint para obter **todas as perguntas e respostas** cadastradas no banco de dados.
- A API retorna uma lista completa das FAQs.

#### **📌 Exemplo de Requisição:**
```bash
curl -X GET http://127.0.0.1:5000/faqs
```

#### **📌 Exemplo de Resposta JSON:**
```json
[
  {
    "question": "Qual seu nome?",
    "answer": "Eu sou o ChatBot, aqui para ajudar você!"
  },
  {
    "question": "Como mudar meu e-mail?",
    "answer": "Vá para as configurações e atualize seu e-mail."
  }
]
```

---

### **3️⃣ Adicionar uma Nova Pergunta e Resposta**
#### **🖥️ Endpoint:** 
```plaintext
POST /add_faq
```
#### **📌 Como funciona?**
- O usuário envia uma nova pergunta e sua respectiva resposta para serem armazenadas no banco de dados.
- A API insere esses dados no MySQL e retorna uma mensagem de sucesso.

#### **📌 Exemplo de Requisição:**
```bash
curl -X POST -H "Content-Type: application/json" -d '{"question": "Como redefinir minha senha?", "answer": "Clique em Esqueci minha senha na tela de login."}' http://127.0.0.1:5000/add_faq
```

#### **📌 Exemplo de Resposta JSON:**
```json
{
  "message": "Pergunta e resposta adicionadas com sucesso!"
}
```

---

## 🔹 **Fluxo do Banco de Dados**
A API interage com um **banco de dados MySQL**, que armazena perguntas e respostas na seguinte estrutura:

```sql
CREATE TABLE faqs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    question TEXT NOT NULL,
    answer TEXT NOT NULL
);
```

Quando o usuário adiciona ou busca perguntas, a API faz **consultas SQL** para inserir ou recuperar os dados.

---

## 🔹 **Resumo do Funcionamento**
1. **O usuário envia uma requisição HTTP** (`POST` ou `GET`).
2. **A API recebe a requisição e interage com o MySQL** para buscar ou armazenar informações.
3. **A API retorna uma resposta JSON** contendo o resultado da operação.
4. **O front-end exibe as informações ao usuário** ou outro sistema usa os dados retornados.

---

## 🔹 **Notas Finais**
✅ **Segurança:** A API pode ser aprimorada para aceitar apenas solicitações autenticadas.  
✅ **Escalabilidade:** Pode ser implementado um **cache** para melhorar a performance.  
✅ **Flexibilidade:** Pode ser integrado com **assistentes virtuais** ou chatbots no Telegram/WhatsApp.  

---

Esse projeto é uma excelente base para criar um **chatbot inteligente** e automatizar respostas frequentes em **sites, aplicativos e sistemas de suporte**! 🚀
