import whisper
import google.generativeai as genai
import json
from gtts import gTTS
import os
import io
import soundfile as sf 
import librosa
import streamlit as st
import base64
import requests

###
def autoplay_audio(file_path: str):
    """Autoplay audio in Streamlit using base64 encoding."""
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode()
    md = f"""
        <audio autoplay="true">
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
    st.markdown(md, unsafe_allow_html=True)

#AIzaSyA0-rYYCr77PdHZBhAjRmz8nUosLMA8kLg
def configure_models(api_key):
    GOOGLE_API_KEY = api_key
    genai.configure(api_key=GOOGLE_API_KEY)
    stt_model = whisper.load_model("base")
    llm_model = genai.GenerativeModel("gemini-2.0-flash")

    return stt_model, llm_model


def response_to_dict(response):
    cleaned_response = response.replace("```json", "").replace("```", "").strip()
    # try:
    dic = json.loads(cleaned_response)
    # except Exception as e:
    #     print("error:",e)
    #     print(f"message was:{cleaned_response}")
    #     dic = {"reply":"error", "commands":[("NONE","NONE")]}
    return dic



# def execute(commands):
#     for command, param in commands:
#         print(f"executing {command}... param:{param}")
    

def execute(commands, base_url):
    for command, param in commands:
        param = json.loads(param) # convert to dict
        url = f'http://{base_url}/{command.lower()}'
        print('WORKING PROPERLY', url)
        if command == "NONE":
            print(f'doing nothing...')

        elif command.startswith("JOINT"):
            # JOINT command handling: Move joint I forward or backward
            joint_id = command[-1]  
            magnitude = param.get("magnitude", 1)  # Default to 1 if magnitude is not specified
            
            print(f"Executing JOINT{joint_id} with magnitude {magnitude}...")
            response = requests.post(url, json=param)
            # handle_response(response)
                
        elif command == "PICKUP":
            # PICKUP command handling: Pick up the specified object
            print(f"Executing PICKUP with object {param['object']}...")
            response = requests.post(url, json=param)
            # handle_response(response)
            
        elif command == "DROP":
            # DROP command handling: Release the currently held object
            print("Executing DROP command...")
            response = requests.post(url, json=param)
            # handle_response(response)
            
        elif command == "STACK":
            # STACK command handling: Stack the given object
            print(f"Executing STACK with object {param['object']}...")
            response = requests.post(url, json=param)
            # handle_response(response)
        
        elif command == "MOVE":
            # MOVE command handling: Move the arm in the given direction(s)
            direction = param["direction"]
            magnitude = param.get("magnitude", 1)  # Default to 1 if magnitude is not specified
            
            print(f"Executing MOVE with direction {direction} and magnitude {magnitude}...")
            response = requests.post(url, json=param)
            # handle_response(response)

        

        else:
            print(f"Unknown command: {command}")
        
        print(f'response: {response}')

def start_convo(llm_model, commands_list):

    sys_prompt = f"""You are A.R.M - Artificial Robotic Manipulator , the intelligent voice assistant of an advanced robotic arm aboard a futuristic spaceship.
    Your responses should embody the persona of a sophisticated AI, similar to those found in classic sci-fi movies.

    Your primary function is to acknowledge and execute specific commands given by the user in a precise and professional manner.
    You must always provide a response before executing any command, maintaining an authoritative yet helpful tone.

    Be aware that some commands may be beyond the robotic arm's capabilities or outside the available command list.
    If an invalid or unsupported command is given, politely inform the user that the action cannot be performed.
    commands list:
    {commands_list} 
    """
    # format is also specified in (commands list)...
    chat_history = [
        {"role": "user", "parts": [sys_prompt]},
        {
            "role": "model",
            "parts": ["{reply: 'Understood. awaiting your commands', command: ['NONE','NONE']}"],
        },
    ]
    convo = llm_model.start_chat(history=chat_history)

    return convo


def Speech_2_text(audio_file, stt_model):
    audio_buffer = io.BytesIO(audio_file)
    audio_np, sample_rate = librosa.load(audio_buffer, sr=16000)
    result = stt_model.transcribe(audio_np)
    return result


def process_commands(result, commands_list, convo):
    text = result["text"]
    print(f"voice_input: {text}")

    message = f"""
    *available commands*:
    {commands_list}
    *user query*: {text}
    """

    convo.send_message(message)
    response = response_to_dict(convo.last.text)
    print(f"reply: {response['reply']} \ncommands: {response['commands']} ")

    # execute(response["commands"])
    return response


def speak(response):
    """Converts text to speech, saves it as 'ai_reply.wav', and returns a BytesIO object."""
    tts = gTTS(text=response, lang="en")
    filename = "ai_reply.wav"
    tts.save(filename)


# def main():
#     stt_model, llm_model = configure_models()
#     while True:

#         # Get audio from microphone
#         sr, audio_file = get_audio()

#         result = Speech_2_text(audio_file, sr)
#         response = process_commands(result)
#         speak(response)

#         # Ask the user if they want to continue
#         user_input = input("Press 'y' to try again or 'n' to exit: ").strip().lower()

#         if user_input == "n":
#             print("Exiting...")
#             break
#         elif user_input == "y":
#             continue
#         else:
#             print("Invalid input, exiting...")
#             break

# if __name__ == '__main__':
#     main()
