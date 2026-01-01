# 🇫🇷 French Language Learning Resources

An interactive web-based French learning platform designed for English speakers. This project provides comprehensive resources for learning French verbs, adjectives, nouns, and phrases through an intuitive interface.

🌐 **Live Site:** [https://djustind.github.io/French/](https://djustind.github.io/French/)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Learning Modules](#learning-modules)
- [How to Use](#how-to-use)
- [Technical Details](#technical-details)
- [Data Structure](#data-structure)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project is a comprehensive French learning resource hosted on GitHub Pages. It includes interactive HTML pages with dynamically loaded content from JSON files, allowing learners to:

- Study 50+ French verbs with complete conjugation tables
- Learn adjectives with gender and number agreement rules
- Build vocabulary with nouns organized by category
- Practice with example sentences and phrases

All content is organized to facilitate self-paced learning with English translations and contextual examples.

## ✨ Features

### 🔤 Verb Conjugator
- **50+ Essential French Verbs** including the most commonly used irregular verbs
- **Complete Conjugation Tables** across multiple tenses and moods:
  - Present (Présent)
  - Past (Passé Composé, Imparfait)
  - Future (Futur Simple, Futur Proche)
  - Conditional (Conditionnel)
  - Subjunctive (Subjonctif)
- **Aspect Variations**: Simple, Continuous, Perfect, and Perfect Continuous forms
- **Interactive Selector**: Choose verb, time frame, and aspect to display specific conjugations
- **Example Sentences**: Each conjugation includes usage examples with English translations
- **Subject Information**: Detailed grammatical information for each pronoun

### 🎨 Adjectives Module
- **Multiple Categories**:
  - Colors (Couleurs)
  - Size (Taille)
  - BAGS adjectives (Beauty, Age, Goodness, Size) - special adjectives that come before nouns
  - Common descriptive adjectives
- **Gender and Number Agreement**: Shows all four forms (masculine/feminine, singular/plural)
- **Position Rules**: Indicates whether adjectives come before or after nouns
- **Form Changes**: Explains how the adjective changes for each gender/number combination
- **Example Phrases**: Practical usage examples with translations

### 📚 Nouns Module
- **Categorized Vocabulary**:
  - Animals (Animaux)
  - Food and Drinks (Nourriture)
  - House and Furniture (Maison)
  - Family Members (Famille)
- **Article Included**: Shows proper article usage (le/la/l'/les)
- **Singular and Plural Forms**: Learn irregular plural formations
- **Visual Support**: Image placeholders for visual learning

### 💬 Phrases and Sentences
- Common greetings and expressions
- Daily life vocabulary
- Travel-related phrases
- Grammar notes (e.g., negation rules)
- Interactive exercises with fill-in-the-blank activities

## 📁 Project Structure

```
French/
├── index.html                      # Main landing page (if exists)
├── verbes_français.html            # Verb conjugation explorer
├── adjectifs_français.html         # Adjectives learning module
├── noms_français.html              # Nouns vocabulary builder
├── phrases_et_sentences.html       # Phrases and sentences practice
├── style.css                       # Shared stylesheet
├── README.md                       # This file
├── directory_map.txt               # Project structure reference
│
├── verbes_français.json            # Verb index (50 verbs)
├── adjectifs_français.json         # Adjectives category index
├── noms_français.json              # Nouns category index
│
├── verbes/                         # Individual verb conjugation files
│   ├── être.json                   # to be (most important irregular verb)
│   ├── avoir.json                  # to have
│   ├── faire.json                  # to do/make
│   ├── aller.json                  # to go
│   ├── pouvoir.json                # to be able to/can
│   ├── vouloir.json                # to want
│   ├── savoir.json                 # to know
│   ├── devoir.json                 # to have to/must
│   ├── prendre.json                # to take
│   ├── voir.json                   # to see
│   ├── venir.json                  # to come
│   ├── parler.json                 # to speak
│   ├── manger.json                 # to eat
│   └── ... (45 more verbs)
│
├── adjectifs/                      # Adjective category files
│   ├── couleurs.json               # Color adjectives
│   ├── taille.json                 # Size adjectives
│   ├── bags.json                   # BAGS rule adjectives
│   └── descriptifs.json            # Common descriptive adjectives
│
├── noms/                           # Noun category files
│   ├── animaux.json                # Animals
│   ├── plantes.json                # Plants
│   └── ... (other categories)
│
└── images/                         # Image resources for vocabulary
```

## 📖 Learning Modules

### Verbes Français (French Verbs)

The verb module includes **50 essential French verbs**, carefully selected based on frequency of use:

**Irregular Verbs** (Most Common):
- être (to be), avoir (to have), faire (to do/make), aller (to go)
- pouvoir (can), vouloir (to want), savoir (to know), devoir (must)
- prendre (to take), voir (to see), venir (to come), dire (to say)
- mettre (to put), connaître (to know), croire (to believe), lire (to read)
- écrire (to write), vivre (to live), suivre (to follow), boire (to drink)
- tenir (to hold), offrir (to offer), ouvrir (to open)

**Regular Verbs** (-er, -ir, -re conjugations):
- parler (to speak), manger (to eat), donner (to give), trouver (to find)
- regarder (to watch), passer (to pass), travailler (to work), penser (to think)
- aimer (to love/like), demander (to ask), rester (to stay), sembler (to seem)
- choisir (to choose), attendre (to wait), répondre (to answer), entendre (to hear)
- rendre (to return), perdre (to lose), partir (to leave), sortir (to go out)

Each verb includes:
- Full conjugation across 5+ tenses
- 4 aspects per tense (where applicable)
- English translations for every form
- Example sentences demonstrating usage
- Grammar notes for irregular forms

### Adjectifs Français (French Adjectives)

Learn adjective agreement rules with organized categories:

**Categories Available**:
1. **Couleurs (Colors)**: rouge, bleu, vert, jaune, noir, blanc, etc.
2. **Taille (Size)**: grand, petit, gros, long, large, etc.
3. **BAGS Rule**: Adjectives that typically come BEFORE the noun
   - Beauty: beau, joli
   - Age: jeune, vieux, nouveau
   - Goodness: bon, mauvais, gentil
   - Size: grand, petit, gros
4. **Descriptifs (Descriptive)**: Common adjectives for everyday use

**What You Learn**:
- All 4 forms: masculine singular, feminine singular, masculine plural, feminine plural
- Position in sentence (before or after noun)
- Regular vs. irregular patterns
- Examples in context

### Noms Français (French Nouns)

Vocabulary building with practical categories:

**Available Categories**:
- **Animaux (Animals)**: Common animals with articles
- **Nourriture (Food)**: Food and drink vocabulary
- **Maison (House)**: Household items and furniture
- **Famille (Family)**: Family member terms
- **Plantes (Plants)**: Common plants and flowers

Each noun entry includes:
- Proper article (le/la/l'/les)
- Singular and plural forms
- Image reference for visual learning
- Gender indication through articles

### Phrases et Sentences

Practice real-world French with:
- Common greetings and introductions
- Everyday expressions
- Travel phrases
- Grammar explanations (negation, question formation)
- Interactive fill-in-the-blank exercises
- Audio placeholders for pronunciation practice

## 🚀 How to Use

### Online Access

Simply visit [https://djustind.github.io/French/](https://djustind.github.io/French/) to access the learning modules directly in your browser.

### Navigation

1. Open any of the main HTML files:
   - [verbes_français.html](verbes_français.html) - For verb conjugations
   - [adjectifs_français.html](adjectifs_français.html) - For adjectives
   - [noms_français.html](noms_français.html) - For nouns
   - [phrases_et_sentences.html](phrases_et_sentences.html) - For phrases

2. Use the dropdown menus and selectors to choose:
   - Specific verbs, adjectives, or noun categories
   - Time frames and aspects (for verbs)
   - Categories (for adjectives and nouns)

3. Content loads dynamically from JSON files
4. Study the examples, translations, and grammatical notes

### Local Development

To run locally:

```bash
# Clone the repository
git clone https://github.com/DjustinD/French.git

# Navigate to the directory
cd French

# Open any HTML file in your browser
# No build process required - pure HTML/CSS/JavaScript
```

## 🔧 Technical Details

### Technology Stack
- **Frontend**: Pure HTML5, CSS3, and Vanilla JavaScript
- **Data Format**: JSON for structured content
- **Hosting**: GitHub Pages
- **No Dependencies**: No frameworks or libraries required

### Data-Driven Architecture

The project uses a modular JSON-based architecture:

1. **Index Files**: Main JSON files list available categories/verbs
2. **Detail Files**: Individual JSON files contain full data for each item
3. **Dynamic Loading**: JavaScript fetches and renders JSON data on demand
4. **Separation of Concerns**: Content (JSON) separated from presentation (HTML/CSS)

### Browser Compatibility

Works in all modern browsers:
- Chrome/Edge (latest)
- Firefox (latest)
- Safari (latest)
- Mobile browsers supported

## 📊 Data Structure

### Verb JSON Structure

```json
{
  "infinitive": "être",
  "english": "to be",
  "irregular": true,
  "conjugations": {
    "présent": {
      "name": "Présent (Present)",
      "aspects": {
        "simple": {
          "name": "Présent Simple",
          "forms": {
            "je": {
              "form": "suis",
              "english": "I am",
              "sentence": "Je suis étudiant.",
              "sentenceEnglish": "I am a student."
            }
          }
        }
      }
    }
  }
}
```

### Adjective JSON Structure

```json
{
  "masculinSingular": "rouge",
  "femininSingular": "rouge",
  "masculinPlural": "rouges",
  "femininPlural": "rouges",
  "english": "red",
  "position": "après",
  "irregular": false,
  "formChanges": {
    "femSing": "no change",
    "mascPlur": "+ s",
    "femPlur": "+ s"
  },
  "examples": [
    {
      "french": "une voiture rouge",
      "english": "a red car"
    }
  ]
}
```

### Noun JSON Structure

```json
{
  "singular": "le chat",
  "plural": "les chats",
  "image": "images/chat.jpg"
}
```

## 🤝 Contributing

Contributions are welcome! Ways to contribute:

1. **Add More Verbs**: Create new verb JSON files following the existing structure
2. **Expand Vocabulary**: Add new noun categories or adjective types
3. **Improve Examples**: Add more example sentences and usage contexts
4. **Add Audio**: Record pronunciation audio files
5. **Add Images**: Contribute images for vocabulary items
6. **Fix Errors**: Correct any grammatical or translation errors
7. **Enhance UI**: Improve styling and user experience

### How to Contribute

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-verbs`)
3. Make your changes following the existing JSON structure
4. Test your changes locally
5. Commit your changes (`git commit -m 'Add 10 new verbs'`)
6. Push to your branch (`git push origin feature/new-verbs`)
7. Open a Pull Request

## 📝 License

This project is open source and available for educational purposes. Feel free to use, modify, and distribute for learning French.

## 🎓 Learning Tips

1. **Start with Verbs**: Focus on être and avoir first, as they're used in compound tenses
2. **Practice Daily**: Spend 15-20 minutes daily on one module
3. **Use Examples**: Read the example sentences aloud to practice pronunciation
4. **Learn BAGS Rule**: Master the adjectives that come before nouns
5. **Build Vocabulary**: Learn nouns with their articles from the start
6. **Review Regularly**: Revisit earlier lessons to reinforce learning

## 📧 Contact

Created by [DjustinD](https://github.com/DjustinD)

For questions, suggestions, or issues, please open an issue on the GitHub repository.

---

**Bonne chance avec votre apprentissage du français!** (Good luck with your French learning!)
