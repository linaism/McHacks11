import assemblyai as aai

aai.settings.api_key = "KEY"
transcriber = aai.Transcriber()

def on_data(transcript: aai.RealtimeTranscript):
  if not transcript.text:
    return

  if isinstance(transcript, aai.RealtimeFinalTranscript):
    print(transcript.text, end="\r\n")
  else:
    print(transcript.text, end="\r")

def on_error(error: aai.RealtimeError):
  print("An error occured:", error)

transcriber = aai.RealtimeTranscriber(
  on_data=on_data,
  on_error=on_error,
  sample_rate=44_100,
)

transcriber.connect()

microphone_stream = aai.extras.MicrophoneStream()
transcriber.stream(microphone_stream)

transcriber.close()