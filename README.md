# Mood-Stabilizers

<br>

## Team Members

1. Mohammad Noor Jebreen

2. Abdelmajed Alabed Alraheem

3. Ahmad Omar A. Shalein

4. laith fayiz abedelrahim hussein

5. yazan ahmad

<br>

## Project management tool

[GitHub Projects](https://github.com/orgs/Mood-Stabilizers-Application/projects/1)

<br>
 * the user stories are in the GitHub Projects tool

## Wire frames

![wire frame](docs/wirefram.png)

[Figma Link](https://www.figma.com/file/0BOvMag0erdU0nF6Sy5yw0/Untitled?node-id=1%3A10)

<br>

## User Stories

 [user story](https://github.com/orgs/Mood-Stabilizers-Application/projects/1)

## [Software Requirements](docs/requirements.md)

<br>
<br>

## Domain Modeling

![Domain Modeling](docs/DomainModeling.jpg)

## Database Schema Diagram

| moodId      | mood |
| ----------- | ----------- |
| id1      | mood       |
| id2   | mood        |

| songId      | song |frequency|
| ----------- | ----------- |-----|
| id1      | song1       |number1|
| id2   | song2        |number2|

| pictureId      | picture |category|
| ----------- | ----------- |-----|
| id1      | Pic1       |Mood1|
| id2   | Pic2      |Mood1|
| id3  | Pic3     |Mood2|

## How to use the app

### *Installation*

Install the following packages:

1. tkinter
2. pygame
3. tensorflow
4. PySimpleGUI
5. opencv-python
6. keras
7. datetime

collecting the data for machine learning:

1. Download FER 2013 Dataset using this link:
[FER2013](https://www.kaggle.com/msambare/fer2013/download)
2. run this command in the terminal : mkdir data
3. extract  the data inside folder data

### How to run this Application

1. Run this command in the terminal: python MoodStablizer/first_page.py

### Run the tests

- Run the following command in the terminal : python3 -m pytest tests
- some tests don't work on github actions, because the github cant reach the device's hardware.