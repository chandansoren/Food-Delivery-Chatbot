# Food-Delivery-Chatbot

Developed a conversational chatbot using GPT-3.5 Turbo and Chainlit for a food delivery service.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [Technologies Used](#technologies-used)
- [License](#license)

## Overview

Food-Delivery-Chatbot is an AI-powered conversational assistant designed to streamline food ordering and customer interactions for a food delivery service. Leveraging OpenAI's GPT-3.5 Turbo and Chainlit, this chatbot can handle user queries, take orders, provide restaurant recommendations, and manage order statuses in a natural, user-friendly way.

## Features

- Natural language understanding and conversation
- Menu browsing and food ordering
- Real-time order status updates
- Restaurant and cuisine recommendations
- Order history retrieval
- Error handling and user guidance for edge cases
- Easily extensible for new features


## Setup and Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/chandansoren/Food-Delivery-Chatbot.git
   cd Food-Delivery-Chatbot
   ```

2. **Create a virtual environment (optional but recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   - `OPENAI_API_KEY`: Your OpenAI API key for GPT-3.5 Turbo.
   - Any other relevant configuration (see [Configuration](#configuration)).

   You can use a `.env` file for local development.

## Usage

1. **Start the chatbot server**
   ```bash
   python app.py
   ```

   Or, if using Chainlit:
   ```bash
   chainlit run app.py
   ```

2. **Interact with the chatbot**
   - Access the chatbot via the provided web interface or integration point.
   - Start chatting to order food, ask for recommendations, or check order status.

## Configuration

- **`config.py` or `.env`**: Contains API keys and configuration options.
- **Supported settings:**
  - `OPENAI_API_KEY`
  - Service endpoints
  - Menu data source paths

## Project Structure

```
Food-Delivery-Chatbot/
├── app.py
├── requirements.txt
├── config.py / .env
├── chatbot/               # Core chatbot logic and modules
│   ├── __init__.py
│   ├── conversation.py
│   ├── order_management.py
│   └── ... 
├── data/                  # Menu and restaurant data
│   └── menu.json
└── README.md
```

## Technologies Used

- Python 3.x
- [OpenAI GPT-3.5 Turbo](https://platform.openai.com/)
- [Chainlit](https://www.chainlit.io/)
- (Optional) Flask/FastAPI for REST endpoints

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Feel free to open issues or submit pull requests for improvements or new features!*
