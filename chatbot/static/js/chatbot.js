const messageBot = document.querySelector('.chat-container')
const formInput = document.querySelector('.text-form')
const userInput = document.querySelector('.prompt')

formInput.addEventListener('submit', (event)=>{
    event.preventDefault();
    const userMessage = userInput.value.trim()

    if (userMessage.length == 0){
        return;
    }
    const message = document.createElement('div');
    message.classList.add('user');
    message.innerHTML = `
    <div class="message-content">
    ${userMessage}
    </div>
    <img class="profile-pic" src="${a}">
    `
    
    messageBot.appendChild(message);
    userInput.value = "";

    fetch('',
    {
       method : 'POST',
       headers : {'Content-Type' : 'application/x-www-form-urlencoded'},
       body : new URLSearchParams(
        {
        'csrfmiddlewaretoken' : document.querySelector('[name=csrfmiddlewaretoken]').value,
        'message' : userMessage
       })
    }).then(response => response.json())
    .then(data =>
        {
            const response = data.response;
            const botMessage = document.createElement('div');
            botMessage.classList.add('bot');
            botMessage.innerHTML = `
            <img class="bot-pic" src="/static/images/logo.png">
            <div class="content-bot">
            ${response}
            </div>`;
            messageBot.append(botMessage);
        });
});
