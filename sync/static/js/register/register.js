swithSection();

function swithSection() {
    const next = document.getElementById("next");
    const prev = document.getElementById("prev");
    const section1 = document.getElementById("section1");
    const section2 = document.getElementById("section2");

    next.addEventListener("click", () => {section1.style.display = "none"; section2.style.display = "block";});
    prev.addEventListener("click", () => {section2.style.display = "none"; section1.style.display = "block";});
}

