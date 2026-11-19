---
name: format-race-data
description: This is a guide for how to format the data obtained from calling the get_race_data() tool, such that it will be formatted nicely into a human-readable way.
---

# Formatting race data guide

The race data comes with the following data (and their types):

Name (str)
Distance (int)
Distance type (str)
Track type (str)

The data should be formatted into a standard markdown-style table so that it can easily be viewed in both raw text or in a chatbot-style user interface. An example is provided below.

# Example

|      Name      | Distance (m) | Distance Type | Track Type |
|:--------------:|:------------:|:-------------:|:----------:|
|  Arima Kinen   |     2500     |      Long     |    Turf    |

# Other notes

Do not include any extraneous filler text, and only include the data and markdown text required for the table.
