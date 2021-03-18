from notion.client import NotionClient
from notion.block import TextBlock
from datetime import date
from datetime import datetime
import sys

now = datetime.now()
today = date.today()
date = today.strftime("%d/%m/%Y")
time = now.strftime("%H:%M")

# Get content from Alfred
# query = sys.argv[1]
sys.argv.pop(0)
query = ' '.join(sys.argv)

# Obtain the `token_v2` value by inspecting your browser cookies on a logged-in (non-guest) session on Notion.so
client = NotionClient(token_v2="YOUR NOTION API KEY")

# Replace this URL with the URL of the page you want to edit
page = client.get_block("YOUR NOTION PAGE URL")
last = client.get_block(page.children[-1].id)

# The today page exist we add the entry to that page
if last.title == date:
    current = last.children.add_new(TextBlock, title=time + ' | ' + query)
    current.checked = True

# The today page doesn't exist we create it and add the entry
else:
    newPage = page.children.add_new(PageBlock, title=date)
    newPage.checked = True
    newCurrent = newPage.children.add_new(TextBlock, title=time + ' | ' + query)
    newCurrent.checked = True