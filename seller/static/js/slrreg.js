function removeMsg() {
    
    const msgElement = document.querySelector("h4");
    msgElement.remove();
  }

const textBox = document.getElementById("form3Example1m");
textBox.addEventListener("mouseover", removeMsg);