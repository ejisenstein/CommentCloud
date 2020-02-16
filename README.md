# CommentCloud
Takes in a Youtube Video Id returns a word cloud of the comment section. Gets data through Youtube Data v3 API

![](comment_builder.gif)

---
## Initial Setup

### 1. Create a Virtual Environment in a New Directory
A new virtual environment is necessary for streamlit. You can use
whatever virtual environment you prefer, I typically use venv
- First create a new directory: `mkdir <dir_name>`
- Create a new environment `python3 -m venv <env_name>`
- Activate the new environment `source <env_name>/bin/activate`

You will need to activate the virtual environment every time you quit the terminal or leave the virtual environment.

To tell whether your environment is active, the environment name should be visible in
parentheses in the first line of your terminal command.

### 2. Install and Test Streamlit Dependency
- With your active virtual environment, install streamlit with this command `pip install streamlit`
- `You can test streamlit is working by running this command` `streamlit hello`
- Full documentation of streamlit is here: https://docs.streamlit.io/   

### 3. Connect to YouTube Data v3 API

- Visit [here](https://console.developers.google.com/) to enable the Youtube Data v3 API.
  - You need to have a project open, if you don't please create one  
  - Search for YouTube Data API v3 in the searchbar at the top  
  - Click Enable  
  - Click Create Credentials  
  - Under **Which API are you using?**, click YouTube Data API v3  
  - Under **Where will you be calling the API from** Click Web Browser(JavaScript)  
  - Under **What data will you be accessing?** click public data  
  - Click **What credentials do I need**  
  - Copy the API Key

### 4. Save your API key to your bash.

- Go back to your home directory with the command `cd ~`
- To access your bash use this command `nano .bash_profile`
  - You do not need to use nano, vim works fine also
- In your bash add `export YT_KEY="<youtube_key"`
- Follow these commands to save the key to your bash
  - Control X
  - Type "yes" to save
  - Press enter

### 5. Clone and add CommentCloud to your repository.
Assuming you have installed git and have github account, navigate to your directory
- Run `git init` to initialize a git repository
- On the github page for CommentCloud click the green button that says clone or download,
  -Make sure it says Clone with HTTPS
  -Copy the link
- Back in your terminal, while inside your repository run the command `git clone <link>`

### 6. Install other dependencies

Again make sure that your virtual environment is active, if not run the `source <env_name>/bin/activate` again

Install these dependencies within your virtual environment_name

- matplotlib: visualization and graphing `pip install matplotlib`
- Google API client `pip install --upgrade google-api-python-client`
- WordCloud `pip install wordcloud`

### 7. How to run CommentCloud

```
cd <dir_name>
source <env_name>/bin/activate //if virtual environment is inactive
cd CommentCloud
streamlit run StreamLitCommentClouds.py
```


**Final Notes**
If you have any issues, specifically regarding the API Key, you can save the api key directly in StreamlitCommentClouds.py in the line:

`api_key = os.environ.get('YT_KEY')`

change it to

`api_key = <api_key>`

It's better practice to hide the key, but this will work. Make sure not to put an API Key in anything you upload to github!

**What the Code Does**
This program pulls top comments and their replies and puts them into a word cloud using the YouTube Data v3 API.

The two main api methods used are
- commentThreads().list: This lists all the top comments to a video by YouTube ID
- comments().list: This lists all the replies based on the parentID of a comment.

This program is built from a python class I created called comment cloud, the comment responses are broken into individual words, then put into a word cloud generator. 

Finally this code uses streamlit to create a simple web app where you can enter a youtube id and it will return a wordcloud of the responses
