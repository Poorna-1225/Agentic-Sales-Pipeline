import asyncio
import os

from dotenv import load_dotenv  
load_dotenv()

os.environ['LIVEKIT_API_KEY'] = os.getenv('LIVEKIT_API_KEY')
os.environ['LIVEKIT_URL'] = os.getenv('LIVEKIT_URL')
os.environ['LIVEKIT_API_SECRET'] = os.getenv('LIVEKIT_API_SECRET')
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')
os.environ['model_name'] = 'gpt-3.5-turbo'



from livekit.agents import AutoSubscribe, JobContext, WorkerOptions, cli,llm
from livekit.agents.voice_assistant import VoiceAssistant
from livekit.plugins import openai, silero

from api import AssistantFnc



async def entrypoint(ctx: JobContext):
    initial_ctx = llm.ChatContext().append(
        role = "system",
        text = (
            "You are a voice assistant created by Livekit. Your interface with users will be voice."
            "You should use short and concise responses, and avoiding usage of unpronouncable punctuation."
        ),
    )

    await ctx.connect(auto_subscribe=AutoSubscribe.AUDIO_ONLY)
    fnc_ctx = AssistantFnc()

    assistant = VoiceAssistant(
        vad = silero.VAD.load(),
        stt= openai.STT(),
        llm = openai.LLM(model='gpt-3.5-turbo'),
        tts = openai.TTS(voice='fable'),
        chat_ctx= initial_ctx,
        fnc_ctx = fnc_ctx,
    )

    assistant.start(ctx.room)

    await asyncio.sleep(1)
    await assistant.say("Hello,I'm Livekit Voice Assistant & How can I help you today?", allow_interruptions= True)



if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc = entrypoint))