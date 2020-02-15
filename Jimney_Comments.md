# CommentClouds

Takes in a Youtube Video Id returns a word cloud of the comment section. Gets data through Youtube Data v3 API.

(MJ - Consider inserting a screenshot of end result)
![nyantocat](https://octodex.github.com/images/nyantocat.gif)

---
## Initial Setup

### 1. Create a Virtual Environment
- A new virtual environment is necessary for streamlit.  You can use whatever virtual environment you prefer, I typically use venv.
  - First create a new directory: `mkdir <dir_name>`
  - Next create a new enviornment: `python3 -m venv <environment_name>`
  - Finally active the new enviornment: `source <environment_name>/bin/activate`

### 2. Test Streamlit Dependency
- You can test streamlit is working by running this command in your directory: `streamlit hello`
- If you do not have streamlit, it can be installed by running: `pip install streamlit`
- The full documentation of streamlit is here https://docs.streamlit.io/

### 3. Connect to Youtube Data v3 API

- Visit https://console.developers.google.com/ and enable the Youtube Data v3 API.
- Save your API key to `.bash_profile`, detailed instructions can be found [here](https://www.youtube.com/watch?v=5iWhQWVXosU)
  - `nano .bash_profile` - Note this example uses nano, but any text editor will work
  - `export YT_KEY="`<youtube_key>`"` - This will be your API key copied from Youtube
  - Ctrl x, type "yes" to save, press enter to keep the file name

### 4. Install Additional Dependencies

- (MJ - Maybe add a quick note what this library is): `pip install --upgrade google-api-python-client`
- (MJ - Ditto above comment): `pip install wordcloud`

---

## How to Run CommentClouds

```
cd <dir_name>
streamlit run StreamlitCommentClouds.py
```
(MJ - I'd suggest adding a comment about what is happening, or maybe show screenshot / example code to demonstrate)