import streamlit as st

st.title("AI in Games")
st.caption("This is an overview of AI being used in Game, with its pros and cons")

st.header("How can it be used in Game?", divider=True)
st.markdown(
    '''Machine learning and trained algorithms are nothing new within the game industry.
    Some of the benefits of utilizing AI would be customized content generation, 
    cheat detection, dynamic player ability matching systems, etc. Generative content creation is a special interest of some of the major gaming companies.  
    For instance, Ubisoft La Forge has launched its GhostWriter Ai tool that helps writers to create original dialogues for its games’ NPCs, and they are also in the process of developing another tool that will generate natural mannerisms for NPCs in matching their given speech and tone. 
'''
)

st.image("https://media.cnn.com/api/v1/images/stellar/prod/231019071157-01-video-games-generative-ai.jpg?q=w_1110,c_fill/f_webp", caption="Ubisoft's speech-to-gesture animation could make NPCs act and react in more natural ways. From Ubisoft La Forge")
st.write("Another potential benefit would be an adapting flagging system in detecting toxic behaviors within the community.However, some obstacles and concerns quickly arise through the utilization of AI systems. ")

st.header("Issues that comes with using AI", divider=True)
st.subheader("Unpredictability")
st.markdown("One of the major issues with the usage of generative AI in games is the unpredictable nature of it, especially during run time. For instance, within the context of NPC dialogues, it can generate completely out-of-character dialogues thus breaking the immersion of the experience.")
st.subheader("Bias")
st.markdown('''Another issue with the utilization of AI would be that the system accommodates the majority of its database, in this case, its player audience. Therefore, it can misinterpret player actions and emotions if said player does not fall within the major group. For instance, the system could mistakenly flag a player who is outperforming other players as cheating, because said player is an outlier within its typical database.''')
st.subheader("Data Collection")
st.write('''Player data collection from game companies is nothing new, as these analytic methods have been used for purposes like bug detection, cheat detection, and gameplay customization. 
         However, the data that were being collected can also be used in order to target susceptible players with purposeful advertisements for in-game purchases. 
         Now, with the introduction of AI, these manipulative advertising tactics can be more easily achieved.''')
st.write('''For instance, Electronic Arts, (EA), was brought to court in California by users who stated that their Difficulty Adjustment Mechanisms had created an illusion of incompetence from users’ teams’ ability to win a match, thus prompting players to purchase more Loot Boxes that might grant them characters with better stats. 
         This undisclosed use of the AI system only benefited EA due to the detriments of its players. ''')

st.header("Your thoughts")
st.subheader("Knowing that your game is using AI and collecting data from you, does it change your overall experience playing it?")

with st.form("user", clear_on_submit=True):
    st.text_area("here is where you put your thoughts")
    submitted = st.form_submit_button("Submit")