# Française Verbs

A web-based French verb conjugation reference tool with interactive examples and comprehensive tense coverage.

## Overview

Française Verbs is a single-page web application that displays French verb conjugations across all major tenses and aspects. Each conjugation includes example sentences with English translations, making it ideal for language learners and reference.

## Features

- **Comprehensive Conjugations**: Covers présent, passé, and futur time frames
- **Multiple Aspects**: Simple, continuous (continu), compound (composé), imperfect (imparfait), pluperfect (plus-que-parfait), literary past (passé simple), near future (proche), and future perfect (antérieur)
- **Example Sentences**: Every conjugation includes a French sentence with English translation
- **Interactive Selection**: Dropdown verb selector with dynamic aspect buttons
- **Accessibility**: ARIA attributes for screen reader compatibility
- **Browser Read Aloud**: Optimized for use with browser Read Aloud features
- **JSON-Based**: Easy to extend with additional verbs

## Included Verbs

Currently includes 11 French verbs (mix of regular and irregular):
- **aller** (to go)
- **avoir** (to have)
- **devoir** (to have to / must)
- **dire** (to say / to tell)
- **être** (to be)
- **faire** (to do / to make)
- **parler** (to speak / to talk)
- **pouvoir** (to be able to / can)
- **prendre** (to take)
- **savoir** (to know)
- **vouloir** (to want)

## Getting Started

### Prerequisites

- A modern web browser (Chrome, Firefox, Safari, Edge)
- Python 3.x (for local HTTP server)

### Running Locally

1. **Clone or download** this repository to your local machine

2. **Start a local HTTP server** in the project directory:
   `ash
   cd path/to/project
   python -m http.server 8000
   `

3. **Open your browser** and navigate to:
   `
   http://localhost:8000/Française.verbs.v2.html
   `

> **Note**: A local server is required due to CORS restrictions when loading JSON files from the file system.

## File Structure

`
.
 README.md                      # This file
 Française.verbs.v2.html        # Main application (current version)
 Française.verbs.html           # Legacy version (v1)
 verbes_français.json           # Master list of all available verbs
 aller.json                     # Individual verb conjugation files
 avoir.json
 devoir.json
 dire.json
 être.json
 faire.json
 parler.json
 pouvoir.json
 prendre.json
 savoir.json
 vouloir.json
`

## JSON Data Format

### Master List (verbes_français.json)

`json
{
  "verbs": [
    {
      "infinitive": "avoir",
      "english": "to have",
      "irregular": true,
      "file": "avoir.json"
    }
  ]
}
`

### Individual Verb Files

Each verb file contains:
- Infinitive form and English translation
- Irregular status
- Conjugations organized by time frame (présent, passé, futur)
- Each time frame contains aspects (simple, continu, composé, etc.)
- Each aspect includes all pronoun forms (je, tu, il/elle, on, nous, vous, ils/elles)
- Example sentences with translations for every form

Example structure:
`json
{
  "infinitive": "avoir",
  "english": "to have",
  "irregular": true,
  "conjugations": {
    "présent": {
      "name": "Présent (Present)",
      "aspects": {
        "simple": {
          "name": "Présent Simple",
          "description": "Simple present tense",
          "forms": {
            "je": {
              "form": "ai",
              "english": "I have",
              "sentence": "J'ai un chat.",
              "sentenceEnglish": "I have a cat."
            }
          }
        }
      }
    }
  }
}
`

## Usage

1. **Select a verb** from the dropdown menu
2. **Choose a time frame** (Présent, Passé, or Futur)
3. **Select an aspect** using the buttons that appear
4. **View conjugations** with example sentences
5. **Use browser Read Aloud** to hear pronunciations (select the conjugation table content)

## Adding New Verbs

To add a new verb to the application:

1. Create a new JSON file following the format of existing verb files
2. Add an entry to `verbes_français.json` in alphabetical order
3. Ensure all required fields are present (infinitive, english, irregular, conjugations)
4. Include all time frames (présent, passé, futur) with appropriate aspects

## Technical Details

- **Pure JavaScript**: No frameworks or dependencies required
- **Responsive Design**: Works on desktop and mobile browsers
- **CSS Styling**: Clean, readable interface with hover effects
- **Accessibility**: ARIA attributes throughout for screen reader support

## Browser Compatibility

- Chrome/Edge (recommended)
- Firefox
- Safari
- Any modern browser with ES6+ support

## Known Issues

- Header navigation may still be read by some browser Read Aloud implementations despite ARIA attributes

## Future Enhancements

- Additional verbs (subjunctive mood, conditional, etc.)
- Audio pronunciations
- Verb search/filter functionality
- Mobile app version
- Quiz/practice mode
- Conjugation tables export (PDF, print)

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository
2. Create a new verb JSON file or improve existing ones
3. Test with the application
4. Submilocally using a Python HTTP server

## License

This project is provided as-is for educational purposes.

## Acknowledgments

Created for French language learners and enthusiasts. Special thanks to all contributors and testers.

---

**Version**: 2.0  
**Last Updated**: December 31, 2025
