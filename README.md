# CommentClouds
Takes in a Youtube Video Id returns a word cloud of the comment section. Gets data through Youtube Data v3 API

![](comment_builder.gif)


## Instructions

When I use <dir_name> or anything with <> it means that you can choose what to name it.


### 1. Open up terminal, create new repository   


```
mkdir <dir_name>
```

### 2. initialize a virtual environment
You can choose whatever virtual environment you prefer, I use venv
```
cd <dir_name>
python3 -m venv <environment_name>
```
A good name for a virtual environment is ENV but you can name it whatever you want.

### 3. Activate the virtual environment
```
source <environment_name>/bin/activate  
```
**Note**

You will need to activate your virtual environment every time you sign out.
To tell whether your environment is active, the enviroment name should be visible in
parentheses in the first line of your terminal command.

### 4. Install streamlit

```
pip install streamlit
```

The full documentation of streamlit is here https://docs.streamlit.io/

### 5. Test stream
```
streamlit hello
```
You can use control + c to exit the streamlit app whenever you need.
### 6. Enable Youtube Data v3 API

Visit https://console.developers.google.com/ and enable the Youtube Data v3 API.

a. You need to have a project open, if you don't please create one  
b. Search for YouTube Data API v3 in the searchbar at the top  
c. Click Enable  
d. Click Create Credentials  
e. Under **Which API are you using?**, click YouTube Data API v3  
f. Under **Where will you be calling the API from** Click Web Browser(JavaScript)  
g. Under **What data will you be accessing?** click public data  
h. Click **What credentials do I need**  
i. Copy the API Key  

Lets

### 7. Hide Key in Environment Variables

Go back to your home directory, you can use this command

```
cd ~
```

Then use this command to access your bash

```
nano .bash_profile //Do not need to use nano, but it is helpful
```

After entering your bash please enter this code. Instead of showing you an actual
key, !API KEY! will refer to your actual API key.

```
export YT_KEY="!API KEY!"
```
Use these commands to get save the code within your bash.
(ctrl x, yes to save, enter to keep file name)

Instructions available here: https://www.youtube.com/watch?v=5iWhQWVXosU

### 8 download code from github, put it into your directory.

Assuming you have an activated github account and are signed in. Also assuming you
have git.

```
```

git init

clone or download

copy the link

git clone <link>



### 9. Install other dependencies

```
pip install matplotlib
pip install --upgrade google-api-python-client
pip install wordcloud
```

### 10. Run code

```
cd <dir_name>
streamlit run StreamlitCommentClouds.py
```
