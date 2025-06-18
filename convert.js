const fs = require('fs');

// Paths
const htmlFilePath = 'index.html';
const jsonFilePath = 'vocabulary.json';
const outputFilePath = "de-bello-gallico.html";

// Read files
let htmlContent = fs.readFileSync(htmlFilePath, 'utf8');
const jsonData = fs.readFileSync(jsonFilePath, 'utf8');

// Create script block
const embeddedScript = `const data = ${jsonData};
vocabulary = data.vocs;
pages = data.pages;
splitSections();
loadHistory();
checkSessionResume();
`;

// Markers
const startMarker = '//<!-- START VOCABULARY EMBED -->';
const endMarker = '//<!-- END VOCABULARY EMBED -->';

// Regex to match between markers
const regex = new RegExp(`${startMarker}[\\s\\S]*?${endMarker}`, 'g');

if (!htmlContent.includes(startMarker) || !htmlContent.includes(endMarker)) {
  console.error(`Markers not found in ${htmlFilePath}. Please add these markers:\n${startMarker}\n${endMarker}`);
  process.exit(1);
}

// Replace block
const newHtmlContent = htmlContent.replace(regex, `${startMarker}\n${embeddedScript}\n${endMarker}`);

// Save output
fs.writeFileSync(outputFilePath, newHtmlContent, 'utf8');

console.log(`Embedded JSON into ${outputFilePath} successfully.`);