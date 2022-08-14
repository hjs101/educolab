# chat/consumers.py
from channels.db import database_sync_to_async
import json
from accounts.models import UserInfo
from quiz.models import QuizList, QuizQuestions
from channels.generic.websocket import AsyncWebsocketConsumer
from .models import QuizRoom, QuizUser, QuizAnswer
from .serializers import QuizRoomSerializer,QuizUserSerializer
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
        message = text_data_json['message']
        send_message = text_data_json['message']
        nickname = ""
        if message == "방 생성":
            print("방 생성")
            id = text_data_json['id']
            room_num = text_data_json['room_num']
            quiz_num = text_data_json['quiz_num']
            data = {
                'teacher':id,
                'roomnum':room_num,
                'quiz':quiz_num
                }
            send_message = await self.create_room(data)
        elif message == "퀴즈 시작":
            print("퀴즈 시작")
        elif message == "학생 정답":
            print("학생 정답")
        elif message == "문제 종료":
            print("문제 종료")
        elif message == "다음 문제":
            print("다음 문제")
        elif message == "결과 보기":
            print("결과 보기")
        elif message == "퀴즈 종료":
            id = text_data_json['id']
            room_num = text_data_json['room_num']
            data = {
                'teacher':id,
                'roomnum':room_num
            }
            send_message = await self.room_delete(data)
        elif message == "학생 입장":
            print("학생 입장")
            id = text_data_json['id']
            room_num = text_data_json['room_num']
            data = {
                'student':id,
                'roomnum':room_num
                }
            resp = await self.join_student(data)
            send_message = resp['message']
            nickname = resp['nickname']
        elif message == "학생 퇴장":
            print("학생 퇴장")
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': send_message,
                'nickname' : nickname,
                'proc_pk' : proc_pk
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        nickname = event['nickname']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'nickname' : nickname
        }))

    @database_sync_to_async
    def room_delete(self, data):
        quiz_room = QuizRoom.objects.get()
        quiz_room.delete()
        return "삭제 성공"
    @database_sync_to_async
    def create_room(self, data):
        quizroom_serializer = QuizRoomSerializer(data=data)
        teacher = UserInfo.objects.get(username=data['teacher'])
        if teacher.userflag != 1:
            return "선생님이 아닙니다."
        quiz = QuizList.objects.get(id=data['quiz'])
        if quizroom_serializer.is_valid(raise_exception=True):
            quizroom_serializer.save(teacher=teacher, quiz=quiz)
        return "등록 성공"
    @database_sync_to_async
    def join_student(self, data):
        isRoom = QuizRoom.objects.filter(roomnum=data['roomnum']).exists()
        if not isRoom:
            return "방이 없네요"
        quiz_room = QuizRoom.objects.get(roomnum=data['roomnum'])
        student = UserInfo.objects.get(username=data['student'])
        quiz_userserializer = QuizUserSerializer(data=data)
        if quiz_userserializer.is_valid(raise_exception=True):
            quiz_userserializer.save(student=student, room=quiz_room)
        if student.wear_title is not None:
            nick ="[" +  student.wear_title.title +  "]"+ student.name
        else :
            nick = student.name
        return {"message":"등록 성공", "nickname":nick}
    @database_sync_to_async
    def answer_submit(self, data):
        isRoom = QuizRoom.objects.filter(roomnum=data['roomnum']).exists()
        if not isRoom:
            return "방이 없네요"
        quiz_room = QuizRoom.objects.get(roomnum=data['roomnum'])
        student = UserInfo.objects.get(username=data['student'])
        quiz_userserializer = QuizUserSerializer(data=data)
        if quiz_userserializer.is_valid(raise_exception=True):
            quiz_userserializer.save(student=student, room=quiz_room)
        return "등록 성공"
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