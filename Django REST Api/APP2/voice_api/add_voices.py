from voices.models import VoiceModel

english_voices = [
    {"name": "English - Standard", "language": "english", "voice_code": "en"},
    {"name": "English - Female 1", "language": "english", "voice_code": "en-au"},
    {"name": "English - Male 1", "language": "english", "voice_code": "en-uk"},
    {"name": "English - Robotic", "language": "english", "voice_code": "en-us"}
]

bangla_voices = [
    {"name": "Bangla - Standard", "language": "bangla", "voice_code": "bn"}
]

for voice in english_voices + bangla_voices:
    VoiceModel.objects.get_or_create(name=voice["name"], language=voice["language"], voice_code=voice["voice_code"])

print("Voice models added successfully!")
