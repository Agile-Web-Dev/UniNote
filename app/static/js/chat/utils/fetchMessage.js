import { receiveMessage } from "../events/receiveMessage.js";

jQuery(async () => {
  const currentPath = window.location.pathname;
  const classCode = currentPath.split("/");
  const response = await fetch("/api/messages/" + classCode[1]);
  const data = await response.json();
  for (const message of data) {
    await receiveMessage(message);
  }
});
