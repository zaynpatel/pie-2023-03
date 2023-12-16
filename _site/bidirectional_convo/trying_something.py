from elevenlabs import clone, generate, play, set_api_key
set_api_key("593e2ea9e6db134739bda2323113efb9")

# voice = clone(
#     name="Alex",
#     files = ["/Users/zaynpatel/the_muncher/bidirectional_convo/test_brad.m4a"]
# )

# audio = generate(text = "I want to talk about different voltage laws today. Let's start with the classic KVL.", voice=voice)

# play(audio)

from elevenlabs import Voice, VoiceSettings, generate

audio = generate(
    text="Hello! My name is Brad and I teach electrical engineering at the Olin College of Engineering. I'm currently umm teaching a class called PIE which is short for Principles of Integrated Engineering and I'm going to talk to one of my students about it today. We're demoing!",
    voice=Voice(
        voice_id='rP93Ilybbe22LT2z1c9k',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)

zayn = generate(
    text="Hello! My name is Zayn. I'm excited to be here with Brad - thanks so much for having me here to demo our PIE project - the Muncherrr",
    voice=Voice(
        voice_id='I6PH5Uewm8CndBWAUhel',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)

audio2 = generate(
    text="Of course Zayn, tell us more about what you've built please.",
    voice=Voice(
        voice_id='rP93Ilybbe22LT2z1c9k',
        settings=VoiceSettings(stability=0.71, similarity_boost=0.5, style=0.0, use_speaker_boost=True)
    )
)


play(audio)
play(zayn)
play(audio2)