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

newchild = page.children.add_new(TextBlock, title=date + ' - ' + time + ' | ' + query)
newchild.checked = True