const chatButton = document.createElement('button');
chatButton.id = 'chatButton';
chatButton.innerText = '💬';
document.body.appendChild(chatButton);

const chatWindow = document.createElement('div');
chatWindow.id = 'chatWindow';
chatWindow.innerHTML = `
  <div class="header">Chat with Us</div>
  <div class="content" id="chatContent"></div>
  <div class="inputSection">
    <input type="text" id="inputMessage" placeholder="Type a message..." />
    <button type="submit" id="sendButton">Send</button>
  </div>
`;
document.body.appendChild(chatWindow);

chatButton.addEventListener('click', () => {
  if (chatWindow.style.display === 'none' || chatWindow.style.display === '') {
    chatWindow.style.display = 'flex';
  } else {
    chatWindow.style.display = 'none';
  }
});

const sendButton = document.getElementById('sendButton');
const inputMessage = document.getElementById('inputMessage');
const chatContent = document.getElementById('chatContent');

sendButton.addEventListener('click', async () => {
  const message = inputMessage.value.trim();
  console.log(inputMessage)
  if (message) {
    displayMessage(message, 'user');
    try {
      const response = await fetch('http://127.0.0.1:8000/send_message', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ message: message }),
      });
      const data = await response.json();
      if (data.reply) {
        displayMessage(data.reply, 'server');
      }
    } catch (error) {
      console.error('Error sending message:', error);
    }
  }
  inputMessage.value = '';
});

function displayMessage(message, sender) {
  const messageElement = document.createElement('div');
  messageElement.classList.add('message', sender);
  messageElement.textContent = message;
  chatContent.appendChild(messageElement);
  chatContent.scrollTop = chatContent.scrollHeight;
}

function getVideoId() {
  const urlParams = new URLSearchParams(window.location.search);
  console.log(urlParams.get("v"))
  return urlParams.get("v");
}

async function fetchTranscript(videoId) {
  const url = `http://localhost:8000/transcript?videoId=${videoId}`;
  try {
    const responsea = await fetch(url);
  } catch (error) {
    console.error("Failed to fetch transcript:", error);
  }
}

const videoId = getVideoId();
fetchTranscript(videoId);