const contactForm = document.getElementById("contact");
const outDialog = document.getElementById("output");
const messageBox = document.getElementById("message");

document.getElementById("modal-close-btn").addEventListener("click", () => {
  outDialog.close();
  document
    .querySelectorAll("#contact input, #contact textarea")
    .forEach((el) => {
      el.value = "";
    });
});

contactForm.addEventListener("submit", (e) => {
  e.preventDefault();

  let data = {};

  document
    .querySelectorAll("#contact input, #contact textarea")
    .forEach((el) => {
      if (el.value !== "") {
        data[el.id] = el.value;
      }
    });

  fetch("/contact/api", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((resp) => {
      const basicErrorType = parseInt(resp.status / 100);
      let msgClass = "ok";

      if (basicErrorType === 4) {
        msgClass = "user-error";
      } else if (basicErrorType === 5) {
        msgClass = "server-error";
      }

      messageBox.classList.add(msgClass);

      return resp.json();
    })
    .then((j) => {
      messageBox.textContent = j["content"];
    })
    .catch(() => {
      messageBox.classList.add("connection-error");
      messageBox.textContent = "Connection Error, Try again later.";
    })
    .finally(() => {
      outDialog.showModal();
    });
});
