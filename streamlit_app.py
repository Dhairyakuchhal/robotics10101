import streamlit as st
from audio_recorder_streamlit import audio_recorder
from techgc_voice_commands import *
import base64
import available_commands
from streamlit_float import *
import time

float_init()

@st.cache_data
def load_models(api_key):
    '''
    returns speech_to_text and llm model
    '''
    commands_list = available_commands.commands_list
    stt_model, llm_model = configure_models(api_key)
    convo = start_convo(llm_model, commands_list)
    return stt_model, llm_model, commands_list, convo

# Initialize session state variables
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "stt_model" not in st.session_state:
    st.session_state.stt_model = None
    st.session_state.llm_model = None
    st.session_state.commands_list = None
    st.session_state.convo = None
    st.session_state.api_key = None
    st.session_state.url = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = [{"role": "assistant", "content": "Hi! I'm A.R.M, How may I assist you today?"}]

st.title("Artificial Robotic Manipulator")


if not st.session_state.logged_in:
    api_key = st.sidebar.text_input("Enter API key", type='password')
    flask_url = st.sidebar.text_input("Enter Flask URL")

    if st.sidebar.button("Load Models"):
        if not api_key:
            st.sidebar.error("API key is required!")
        if not flask_url:
            st.sidebar.error("Please enter a URL!")
        else:
            st.session_state.api_key = api_key
            stt_model, llm_model, commands_list, convo = load_models(api_key)
            st.session_state.stt_model = stt_model
            st.session_state.llm_model = llm_model
            st.session_state.commands_list = commands_list
            st.session_state.convo = convo
            st.session_state.url = flask_url
            st.session_state.logged_in = True
            st.success("Models loaded!")
            time.sleep(1)
            st.rerun()

if st.session_state.logged_in:
    # Fixed footer for the recording button
    footer = st.container()
    with footer:
        # stf.float_parent(css="position: fixed; bottom: 0; left: 0; width: 100%; background-color: transparent; padding: 10px;")
        recorded_audio = audio_recorder()
    footer.float("bottom: 0rem;")

    st.sidebar.markdown(available_commands.sidebar_commands_list)
    
    for sender_message in st.session_state.chat_history:
        with st.chat_message(sender_message["role"]):
            st.markdown(f"**{'You' if sender_message['role'] == 'user' else 'A.R.M'}:** {sender_message['content']}")

    if recorded_audio is not None:
        # st.audio(recorded_audio, format="audio/wav")

        # Transcription

        with st.spinner("Transcribing..."):
            transcription = Speech_2_text(recorded_audio, st.session_state.stt_model)
            user_message = transcription['text']
        if user_message:
            st.session_state.chat_history.append({"role": "user", "content": user_message})
            with st.chat_message("user"):
                st.markdown(f'**You:** {user_message}')

            
        # Process Commands & Generate Response
        if st.session_state.chat_history[-1]["role"] != "assistant":
            with st.chat_message("assistant"):
                with st.spinner("Thinking🤔..."):
                    response = process_commands(transcription, st.session_state.commands_list, st.session_state.convo)
                    final_response = response['reply']

                with st.spinner("Generating audio response🗣️..."):
                    speak(final_response) #saves response to ai_reply.wav

                autoplay_audio("ai_reply.wav")
                st.markdown(f'**A.R.M:** {response["reply"]}')
                execute(response['commands'], st.session_state.url)
                

            # Append AI Response to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": final_response})