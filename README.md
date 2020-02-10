# CommentCloud
Takes in a Youtube Video Id returns a word cloud of the comment section. Gets data through Youtube Data v3 API

## Instructions

### 1. Create new repository and initialize/activate a virtual environment. <br /> You can use whatever virtual environment you prefer, I typically use venv.

```
mkdir <dir_name>

python3 -m venv <environment_name>

source <environment_name>/bin/activate  
```

A new virtual environment is necessary for streamlit.

### 2. Test streamlit dependency.

```
pip install streamlit
```

The full documentation of streamlit is here https://docs.streamlit.io/

You can test streamlit is working with this command in your directory.

```
streamlit hello
```

### 3. Enable Youtube Data v3 API

Visit https://console.developers.google.com/ and enable the Youtube Data v3 API.

Copy key

### 4. Hide Key in Environment Variables

```
nano .bash_profile //Do not need to use nano, but it is helpful

export YT_KEY="<youtube_key>"
```
(ctrl x, yes to save, enter to keep file name)

Instructions available here: https://www.youtube.com/watch?v=5iWhQWVXosU


### 5. Install other dependencies

```
pip install --upgrade google-api-python-client
pip install wordcloud
```

### 6. Run code

```
cd <dir_name>
streamlit run StreamlitCommentClouds.py
```
