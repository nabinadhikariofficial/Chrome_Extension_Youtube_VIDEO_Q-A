from flask import Flask, request, jsonify
from flask_cors import CORS
from youtube_transcript_api import YouTubeTranscriptApi
from ai import gemini_ai

app = Flask(__name__)
CORS(app)

start_prompt = "Here is the Caption of a video with its timestamp of spoken time, Please summarize it for now. I will ask few question Regarding it help me answer it.\n"
formatted_transcript = ''


first = True
chat_ai = gemini_ai()


@app.route('/send_message', methods=['POST'])
def send_message():
    global first
    data = request.get_json()
    user_message = data.get('message')

    if first:
        chat_ai.get_answer(start_prompt + formatted_transcript)
        ai_reply = chat_ai.get_answer(user_message)
        first = False
    else:
        ai_reply = chat_ai.get_answer(user_message)

    return jsonify({'reply': ai_reply})


def trans_data(video_id):
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    transcript_f = ""
    for entry in transcript:
        start_time = entry['start']
        duration = entry['duration']
        text = entry['text']

        start_minutes = int(start_time // 60)
        start_seconds = int(start_time % 60)
        end_time = start_time + duration
        end_minutes = int(end_time // 60)
        end_seconds = int(end_time % 60)
        transcript_f += f"[{start_minutes:02}:{start_seconds:02} - {end_minutes:02}:{end_seconds:02}] {text}"
    return transcript_f


@app.route("/transcript", methods=['GET'])
def get_transcript():
    global first
    global formatted_transcript
    first = True
    chat_ai.clear_history()
    video_id = request.args.get("videoId")
    try:
        formatted_transcript = trans_data(video_id=video_id)
        return "200"
    except Exception as e:
        return "400"


if __name__ == '__main__':
    app.run(debug=True, port=8000)
