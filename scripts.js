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
        console.log(voc);
        document.getElementById("latin").innerHTML = voc.latin;

        const lines = voc.german.split("\n"); // Split the German text into lines
        const germanElement = document.getElementById("german-field");
        germanElement.innerHTML = ""; // Clear existing content

        lines.forEach(line => {
            const p = document.createElement("p");
            p.id = "german";
            p.textContent = line;  // Set the text of the <p> element
            germanElement.appendChild(p);  // Append the <p> to the #german element
        });
    }
})();
