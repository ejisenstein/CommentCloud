import os
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

#from apiclient.discovery import build
from googleapiclient.discovery import build
from wordcloud import WordCloud, STOPWORDS

api_key = os.environ.get('YT_KEY')
youtube = build('youtube', 'v3', developerKey=api_key)

st.title('Youtube Comment Builder')

streamlit_yt_id = st.text_input("Give Youtube ID", '2MYD5LkXxKg')

#streamlit_stopwords = st.text_area("Remove these words from the wordcloud, make sure to include a comma between each word",
#'stupid, ugly')

#@st.cache
class CommentCloud():
    """Takes in a youtube id
    returns a wordcloud"""

    def __init__(self, YouTube_ID, youtube, stops, file_name):
        self.YouTube_ID = YouTube_ID
        self.api_key = api_key
        self.youtube = youtube

    def GetTopComments(self):
        """Request comments via youtube api, saves under self"""
        self.top_comments = self.youtube.commentThreads().list(
        part="snippet",
        videoId=self.YouTube_ID,
        maxResults = 100).execute()

    def TopCommentsDF(self):
        """Creates a dataframe with the author
        names under Name, comments under Val saved under self"""

        top_comment_list = []
        author_name_list = []

        for i in range(len(self.top_comments['items'])):
            top_comment_list.append(
            self.top_comments['items'][i]['snippet']['topLevelComment']['snippet']['textDisplay'])

            author_name_list.append(
            self.top_comments['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName'])

        self.top_comments_df = pd.DataFrame(list(zip(author_name_list, top_comment_list)),
               columns =['Name', 'Val'])

    def GetTopCommentsWithReplies(self):
        """Create a list of tuples, includes Author and Comment id saved within self"""

        reply_list = []
        for i in range(len(self.top_comments['items'])):
            if self.top_comments['items'][i]['snippet']['totalReplyCount'] != 0:
                reply_list.append((self.top_comments['items'][i]['snippet']['topLevelComment']['snippet']['authorDisplayName'],
                           self.top_comments['items'][i]['id'],
                           self.top_comments['items'][i]['snippet']['totalReplyCount']))

        self.top_comment_num_replies_df = pd.DataFrame(reply_list,
               columns =['Name', 'Parent_ID', 'Num_replies'])

    def CommentRepliesDF(self):
        """Creates dataframe of comment replies saves to self
        """
        comment_replies = []
        for i in self.top_comment_num_replies_df['Parent_ID']:
            local_api_call =  self.youtube.comments().list(part = 'snippet',
                                                           parentId = i).execute()
            for num in range(len(local_api_call['items'])):
                    comment_replies.append((local_api_call['items'][num]['snippet']['authorDisplayName'],
                                local_api_call['items'][num]['snippet']['textDisplay']))

        self.replies_df = pd.DataFrame(comment_replies,
               columns =['Name', 'Val'])

    def AppendReplies(self):
        """Appends top comments df and comment replies df"""

        full_comments = self.top_comments_df['Val']

        self.full_comments = full_comments.append(self.replies_df['Val'])

    def MakeCloud(self, stops, file_name):
        self.stops = stops
        self.file_name = file_name

        total_words_series = self.full_comments.str.lower().str.replace('[^\w\s]', '').str.split()

        total_list = []
        for word_list in total_words_series:
            for word in word_list:
                total_list.append(word)

        text = " ".join(word for word in total_list)

        #self.stops = self.stops.strip()
        #self.split_stops = self.stops.split(',')

        self.wordstops = list(STOPWORDS) + list(self.stops)

        word_cloud = WordCloud(width = 1600,
                               height = 800,
                               stopwords=self.wordstops).generate(text)

        plt.figure( figsize=(20,10), facecolor='k')
        ax = plt.imshow(word_cloud)
        plt.axis("off")

        return ax



        #plt.savefig(self.file_name, facecolor='k', bbox_inches='tight')


youtube_ID = streamlit_yt_id
stops =  'stupid, ugly'
file_name = 'StreamLit.png'

com_cloud = CommentCloud(youtube_ID, youtube, stops, file_name)
com_cloud.GetTopComments()
com_cloud.TopCommentsDF()
com_cloud.GetTopCommentsWithReplies()
com_cloud.CommentRepliesDF()
com_cloud.AppendReplies()
cloud = com_cloud.MakeCloud(stops, file_name)


st.pyplot()

some_text = str(com_cloud.stops)

#st.text(f'return of wordstops {type(some_text)}')

#st.text(f'return of split_stops {com_cloud.split_stops} {type(com_cloud.split_stops)}')


st.markdown('## Created by **Evan James Isenstein**')
st.markdown('Evan is open to Data Science roles, he enjoys Tennessee Titans football, historical novels, and hot chicken')
st.markdown('Evan\'s [LinkedIn Profile:] (https://www.linkedin.com/in/evan-isenstein-54b047a3/)')
st.markdown('Evan\'s [Github] (https://github.com/ejisenstein/)')