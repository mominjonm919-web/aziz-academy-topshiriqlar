const taskInput = document.getElementById("taskInput");
const addBtn = document.getElementById("addBtn");
const list = document.getElementById("list");

addBtn.addEventListener("click", function () {
    const text = taskInput.valuez.trim();

    if (text === "") {
        return;
    }

    const li = document.createElement("li");
    li.textContent = text;

    // Vazifani bajarilgan deb belgilash
    li.addEventListener("click", function () {
        li.classList.toggle("done");
    });

    // O'chirish tugmasi
    const delBtn = document.createElement("button");
    delBtn.textContent = "❌";

    delBtn.onclick = function (e) {
        e.stopPropagation(); // li click ishlamasligi uchun
        li.remove();
    };

    li.appendChild(delBtn);
    list.appendChild(li);

    taskInput.value = "";
    taskInput.focus();
});