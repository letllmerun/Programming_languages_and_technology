const nameInput = document.querySelector("#name");
const groupInput = document.querySelector("#group");
const courseInput = document.querySelector("#course");
const card = document.querySelector("#card");

function createStudentCard() {
    const name = nameInput.value;
    const group = groupInput.value;
    const course = courseInput.value;

    if (name === "" || group === "" || course === "") {
        card.textContent = "Please fill in all fields";
        return;
    }

    card.innerHTML = `
        <h2>Student Card</h2>
        <p>Name: ${name}</p>
        <p>Group: ${group}</p>
        <p>Course: ${course}</p>
    `;
}

document.querySelector("#create").addEventListener("click", createStudentCard);