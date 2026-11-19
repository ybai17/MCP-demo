---
name: format-horse-data
description: This is a guide for how to format the data obtained from calling the get_horse_data() tool, such that it will be formatted nicely into a human-readable way.
---

# Formatting horse data guide

The horse data comes with the following data (and their types)
Name (str)
Color (str)
Birth year (int)
Distance aptitudes (an object of str:str pairs)
Track aptitudes (an object of str:str pairs)

The data should be formatted into 3 standard markdown-style tables so that it can easily be viewed in both raw text or in a chatbot-style user interface. An example is provided below.
The first table will include the simpler metadata: the name, color, and the year of the horse.
The second table will include the distance aptitudes.
The third table will include the track aptitudes.

# Example

|      Name      | Color | Birth year |
|----------------|-------|------------|
| Symboli Rudolf | Brown |    1989    |

| Sprint | Mile | Medium | Long |
|--------|------|--------|------|
|    E   |  C   |   A    |   A  |

| Turf | Dirt |
|------|------|
|  A   |  G   |

# Other notes

Do not include any extraneous filler text, and only include the data and markdown text required for the table.
