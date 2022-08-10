# chat/consumers.py
from channels.db import database_sync_to_async
import json
from quiz.models import QuizList
from channels.generic.websocket import AsyncWebsocketConsumer

class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        


        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        print(text_data_json)
        message = text_data_json['message']
        # 선생님id, 퀴즈번호, 문제
        quiz_list = await self.get_quizlist()

        print(quiz_list)
                # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))

    @database_sync_to_async
    def get_quizlist(self):
        return QuizList.objects.all()
# 1 100
# 2 90
# 3 80
# 4 70
# 5 60
# 6 ... 50 ~

# 퀴즈

# quiz_room 테이블

# 선생님, 현재 풀고있는 문제, 방 번호

# 참여 유저 테이블 : 학생, 점수, 방 번호

# 문제 정답 테이블 : 학생

# quiz_answer 테이블

# 추가시간(created_at), 학생fk, 문제번호, 방번호(ondeleteCascade) 값이 추가

# 문제번호로 정렬시켜서 가져온다음에 0~5 점수 차등으로 주고, 6~나머지는 같은점수 부여 

# 문제

# 문제별로 DB에 저장을 하는데 CREATED_AT

# 시작신호 받아서 20초 타이머 걸고, 20초 뒤에는 제출 못하게 하기 AND 신호를 보내서 임베디드에 종료신호 보내서 화면 바뀌게

# 전역변수로 flag  시작신호 오면 True 종료신호 False

# REQUEST오면 문제 DB에서 정답 가져와서 비교

# 정답 테이블 : 문제마다 데이터 추가 - 정답일때만 -> 추가된 시간순으로 정렬

# 정렬해서 가져오고 점수부여하고 데이터 삭제