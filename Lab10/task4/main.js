import { rectArea } from "./geometry.js";
const result = document.querySelector("#result");

document.querySelector("#btn-rect").addEventListener("click", () => {
    const w = Number(document.querySelector("#w").value);
    const h = Number(document.querySelector("#h").value);
    result.textContent = "Площадь: " + rectArea(w, h);
});