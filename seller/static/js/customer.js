function removeMsg() {
    
    const msgElement = document.querySelector("h4");
    msgElement.remove();
  }

const textBox = document.getElementById("firstname");
textBox.addEventListener("mouseover", removeMsg);