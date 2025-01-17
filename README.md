# FlirtyHuh

FlirtyHuh is a fun and interactive flirt bot that brings a touch of humor and charm to your conversations. This project involves creating a custom dataset, fine-tuning a T5-small model, and developing a user-friendly front-end using HTML, CSS, and JavaScript.

<p align="center">
  <img src="https://github.com/ranzeet013/FlirtyHuh/blob/main/image/1000029006.png" alt="FlirtyHuh Logo" width="300">
</p>

## Features
- A custom-trained T5-small model for generating flirty responses.
- User-friendly interface built with HTML, CSS, and JavaScript.
- Fun and engaging interaction with users.
- Responsive design for accessibility across various devices.
- Real-time message exchange with dynamic bot responses.

## Project Overview

### 1. Dataset Creation
- Created a custom dataset tailored for flirtatious responses.
- The dataset includes a variety of prompts and witty replies designed to emulate a charming conversationalist.
- Employed techniques to ensure diversity and creativity in the dataset.

### 2. Model Training
- Fine-tuned the T5-small model using the custom dataset.
- Leveraged Hugging Face Transformers library for training and evaluation.
- Optimized the model to generate creative, relevant, and engaging responses.
- Incorporated evaluation metrics such as BLEU and Rouge to measure response quality.

### 3. Front-End Development
- Designed a clean and intuitive front-end using HTML, CSS, and JavaScript.
- Implemented a responsive design for seamless usage across desktops, tablets, and smartphones.
- Built features to send messages, display bot responses dynamically, and manage session states.

## Tech Stack
- **Model**: [T5-small](https://huggingface.co/t5-small)
- **Libraries**: Hugging Face Transformers, PyTorch
- **Front-End**: HTML, CSS, JavaScript
- **Backend**: Flask or FastAPI (for hosting the bot logic)

## Setup Instructions

### Backend
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd flirtyhuh
   ```
2. Install dependencies:
   ```bash
   pip install torch transformers flask
   ```
3. Load the fine-tuned T5 model and set up the backend script.
4. Run the backend server:
   ```bash
   python app.py
   ```

### Front-End
1. Open the `frontend` folder.
2. Edit the `config.js` file to point to the backend server URL if necessary.
3. Open `bot.html` in a web browser.
4. Start chatting with the bot and enjoy!

## Usage
1. Open the web interface.
2. Type a message into the input box and hit send.
3. The bot will respond with a witty or flirty reply in real time.

## Future Enhancements
- Add support for multiple languages to cater to a wider audience.
- Integrate with popular messaging platforms like WhatsApp and Telegram.
- Expand the dataset for more nuanced and varied responses.
- Implement additional personality modes for the bot (e.g., humorous, poetic, etc.).
- Add user analytics to improve bot performance and user satisfaction.

## Contributing
Feel free to contribute to FlirtyHuh! If you have suggestions for improvement or encounter any issues, please submit a pull request or create an issue in the repository.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

---

Enjoy chatting with FlirtyHuh and spread the charm!
