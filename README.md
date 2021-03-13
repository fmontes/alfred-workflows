![8494bb95617b5dfcbc32784512bdbd10](https://user-images.githubusercontent.com/751424/111052762-85e48580-8423-11eb-8297-a810389fa927.jpg)

# Alfred Workflows
[Alfred](https://www.alfredapp.com/) is a prodyctivity app for Mac that boosts your efficiency with hotkeys, keywords, text expansion and more.

You can extend Alfred functionality with [Workflows](https://www.alfredapp.com/workflows/), which allows you to write code to create your own custom integrations and tooling.

## Workflows 
In this repo you can find the workflows I created for myself.

### Notion
Contains all the workflows I use to interact with my Notion account.

It uses [notion-py](https://github.com/jamalex/notion-py) unofficial Python 3 client for Notion.so API v3.

#### Journal Entry

I like to keep a log of all the activities I do every day, not only for work but for everything.

I create this workflow as a shortcut to add an entry to my log in a Notion page easily.

**How it works?**
1. Trigger Alfred
2. Type nj
3. Type what you want to entry and hit enter.
4. That's it

It will add your entry with the date and time.

**Download**
[Notion.alfredworkflow](https://github.com/fmontes/alfred-workflows/raw/master/notion/Notion.alfredworkflow)

**Code**
[/notion/journal-entry.py](https://github.com/fmontes/alfred-workflows/blob/master/notion/journal-entry.py)
