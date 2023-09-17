import streamlit as st
from streamlit_extras import grid
import pyperclip
import requests

state = st.session_state

if "quote" not in state:
    state['quote'] =""
if "Author" not in state:
    state["Author"] =""
if "Title" not in state:
    state["Title"] =""
if "URL" not in state:
    state["URL"] ="#"
if "font-style" not in state:
    state["font-style"] ="font-mono"
if "flag" not in state:
    state["flag"] =False


def get_random_quote():
    url = "https://api.quotable.io/quotes/random?minLength=250"
    r = requests.get(url,verify=False)
    data = r.json()[0]
    state['quote'] = data['content']
    state["Author"] = data['author']
    state["Title"] = data['tags'][0]
    state["URL"] = "https://api.quotable.io/random"
    state["flag"] = True

def update_font():
    if state["font-style"] == "font-mono":
        state["font-style"] = "font-sans"
        
    else:
        state["font-style"] = "font-mono"
        
if state["flag"]==False:
    get_random_quote()



code = f'''
<link href="https://cdn.jsdelivr.net/npm/daisyui@3.7.4/dist/full.css" rel="stylesheet" type="text/css" />
<script src="https://cdn.tailwindcss.com"></script>
<div class="{state["font-style"]} flex flex-col max-w-lg m-2 p-4 bg-white border rounded-lg hover:drop-shadow-lg hover:translate-y-1 duration-300">
    <div class="">
        {st.session_state.quote}
    </div>
    <div class="mt-2 flex flex-row justify-end">
        <img class="mt-2 h-8 w-8 rounded-full border-none" src="https://s2.googleusercontent.com/s2/favicons?domain_url={state["URL"]}&sz=64" alt="">
        <div class="flex flex-col w-1/2">
        <p class="font-normal mx-1 truncate">{state["Author"]}</p>
        <p class="font-thin mx-1 truncate ">{state["Title"]}</p>
    </div>
   <div class=" m-2 w-1/2 flex flex-row justify-end">
    <a href="{state["URL"]}" target="_blank">
    <p class="font-normal">Source</p>
    </a>
   </div>
    </div>
</div>
'''

st.set_page_config(page_title="Embeddit",page_icon="favicon.png")
sidebar = st.sidebar

with sidebar:
    gd = grid.grid(1,[1,1],1,1,1)
    gd.text_area('Quote',state['quote'],label_visibility="hidden",key="quote" )
    gd.text_input(label="",label_visibility="hidden",placeholder="Author Name",key="Author")
    gd.text_input(label="",label_visibility="hidden",placeholder="Title",key="Title")
    gd.text_input(label="",label_visibility="hidden",placeholder="https://example.com/intresting-article",key="URL")
    gd.toggle('Monospace',on_change=update_font,value=True)
    with st.expander("View Embed Code"):
        
        st.code(code,language="HTML",line_numbers=True)


st.header('Embeddit: Text Snippets, Your Way!')
st.caption('Craft Minimalist Shareable Embeds from Online Text Sources')



st.components.v1.html(code,width=1000, height=1000)




    

    











