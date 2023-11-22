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
    .then(async (resp) => {
      const temp = resp.json();
      if (!resp.ok) {
        throw {
          basicErrorType: parseInt(resp.status / 100),
          content: await temp,
        };
      }
      messageBox.classList.add("ok");

      return temp;
    })
    .then((j) => {
      messageBox.textContent = j["content"];
    })
    .catch(({ basicErrorType, content }) => {
      let msgClass = "connection-error";

      if (basicErrorType === 4) {
        msgClass = "user-error";
      } else if (basicErrorType === 5) {
        msgClass = "server-error";
      }

      messageBox.classList.add(msgClass);
      messageBox.textContent =
        content.content || "Connection Error, Try again later.";
    })
    .finally(() => {
      outDialog.showModal();
    });
});
