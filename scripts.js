async function fetchJSONData(file) {
    try {
        const res = await fetch(file);
        if (!res.ok) {
            throw new Error(`HTTP error! Status: ${res.status}`);
        }
        return await res.json(); // Returns parsed JSON data
    } catch (error) {
        console.error("Unable to fetch data:", error);
        return null; // Return null in case of an error
    }
}

// Use async/await when calling the function
(async () => {
    const vocabulary = await fetchJSONData("./vocabulary.json");
    if (vocabulary) {
        let vocIndex = 0;
        let voc = vocabulary[vocIndex];
        const frontsideElement = document.getElementById("frontside")
        frontsideElement.innerHTML = voc.latin;

        const lines = voc.german.split("\n"); // Split the German text into lines
        const backsideElement = document.getElementById("backside");
        backsideElement.innerHTML = ""; // Clear existing content

        if (voc.grammar_info) {
            const p = document.createElement("p");
            p.id = "backside-line";
            p.textContent = voc.grammar_info; 
            backsideElement.appendChild(p);
        }

        lines.forEach(line => {
            const p = document.createElement("p");
            p.id = "backside-line";
            p.textContent = line;
            backsideElement.appendChild(p);
        });
    }
})();

// Wait until DOM is fully loaded
document.addEventListener("DOMContentLoaded", () => {
    const wrongButton = document.getElementById("voc-wrong");
    const correctButton = document.getElementById("voc-correct");

    wrongButton.addEventListener("click", () => {
        console.log("Marked as wrong");
        // Add your logic here (e.g., highlight red, count wrong answers, etc.)
    });

    correctButton.addEventListener("click", () => {
        console.log("Marked as correct");
        // Add your logic here (e.g., go to next word, store result, etc.)
    });
});


