from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse


# Create your views here.

def home(request):
    
    db = get_db()
    patient_id = 0

    # 1. mood
    retrieved_emotion = find_emotion_by_patient_id(db, patient_id)

    # truncate emotion length to 30 days
    if len(retrieved_emotion) > 30: 
        retrieved_emotion = retrieved_emotion[len(
            retrieved_emotion) - 30: len(retrieved_emotion)]

    # init mood dict
    diction["mood"] = {"time": ["0000-00-00"] * 30, "yvalue": {}}
    diction["mood"]["yvalue"] = {"neutral": [0] * 30, "happiness": [0] * 30,
                                 "sadness": [0] * 30, "surprise": [0] * 30, "anger": [0] * 30}
    index = 0

    # fill in the dictionary
    for feature in retrieved_emotion:
        if (index < 30 - len(retrieved_emotion)):
            index = index + 1
            continue
        time = feature["time"]
        neutral = feature["neutral"]
        happiness = feature["happiness"]
        sadness = feature["sadness"]
        surprise = feature["surprise"]
        anger = feature["anger"]
        
        diction["mood"]["time"][index] = time
        diction["mood"]["neutral"][index] = neutral
        diction["mood"]["happiness"][index] = happiness
        diction["mood"]["sadness"][index] = sadness
        diction["mood"]["surprise"][index] = surprise
        diction["mood"]["anger"][index] = anger
        index = index + 1

    print(retrieved_emotion)

    # 2. game
    retrieved_game = find_game_by_patient_id(db, patient_id)

    # truncate emotion length to 30 days
    if len(retrieved_game) > 30:
        retrieved_game = retrieved_game[len(
            retrieved_game) - 30: len(retrieved_game)]

    # init mood dict
    diction["game"] = {"time": ["0000-00-00"] * 30, "yvalue": {}}
    diction["game"]["yvalue"] = {"WordSearch": [0] * 30, "TileMatching": [0] * 30,
                                 "Brown-Peterson": [0] * 30}
    index = 0

    # fill in the dictionary
    for feature in retrieved_game:
        if (index < 30 - len(retrieved_game)):
            index = index + 1
            continue
        time = feature["time"]
        word_search = feature["WordSearch"]
        tile_matching = feature["TileMatching"]
        brown_Peterson = feature["Brown-Peterson"]

        diction["game"]["time"][index] = time
        diction["game"]["yvalue"]["WordSearch"][index] = word_search
        diction["game"]["yvalue"]["TileMatching"][index] = tile_matching
        diction["game"]["yvalue"]["Brown-Peterson"][index] = brown_Peterson
        index = index + 1

    print(retrieved_game)

    # biometric
    retrieved_biometric = find_biometric_by_patient_id(db, patient_id)
    
    # truncate emotion length to 30 days
    if len(retrieved_biometric) > 30:
        retrieved_biometric = retrieved_biometric[len(
            retrieved_biometric) - 30: len(retrieved_biometric)]

    # 3. blood
    diction["blood"] = {"time": ["0000-00-00"] * 30, "yvalue": {}}
    diction["blood"]["yvalue"] = {"systolic": [0] * 30, "diastolic": [0] * 30}
    
    # 4. heartrate
    diction["heartrate"] = {"time": ["0000-00-00"] * 30, "yvalue": [0] * 30}
   
    # 5. tremor1
    diction["tremor1"] = {"time": ["0000-00-00"] * 30, "yvalue": [0] * 30}
    
    # 6. tremor2
    diction["tremor2"] = {"time": ["0000-00-00"] * 30, "yvalue": [0] * 30}

    # fill in the dictionary
    for feature in retrieved_biometric:
        if (index < 30 - len(retrieved_biometric)):
            index = index + 1
            continue
        time = feature["time"]

        blood = feature["blood"]
        systolic = blood["systolic"]
        diastolic = blood["diastolic"]

        heartrate_value = feature["heartrate"]
        tremor1_value = feature["tremor1"]
        tremor2_value = feature["tremor2"]

        diction["blood"]["time"][index] = time
        diction["blood"]["yvalue"]["systolic"][index] = systolic
        diction["blood"]["yvalue"]["diastolic"][index] = diastolic

        diction["heartrate"]["time"][index] = time
        diction["heartrate"]["yvalue"][index] = heartrate_value

        diction["tremor1"]["time"][index] = time
        diction["tremor1"]["yvalue"][index] = tremor1_value

        diction["tremor2"]["time"][index] = time
        diction["tremor2"]["yvalue"][index] = tremor2_value

        index = index + 1

    print(diction["blood"])
    print(diction["heartrate"])
    print(diction["tremor1"])
    print(diction["tremor2"])
    
    # return HttpResponse(json.dumps(diction), content_type='application/json')
    return render(request, 'caregiver/index.html')


def todo(request):
    return render(request, 'caregiver/todo.html')


def calendar(request):
    return render(request, 'caregiver/calendar.html')


def metrics(request):
    return render(request, 'caregiver/metrics.html')


def exercises(request):
    return render(request, 'caregiver/exercises.html')


def survey(request):
    return render(request, 'caregiver/survey.html')


def login(request):
    return render(request, 'caregiver/login.html')

def register(request):
    return render(request, 'caregiver/register.html')


@login_required
def metric_display(request):
    db = get_db()

    accel_id = find_accel_by_id(1)
    # verify data
    retrieved_accel = []
    print("accel_id to find: ", accel_id)
    retrieved_emotion = find_emotion_by_patient_id(db, accel_id)
    print(retrieved_emotion)
    
    
    # diction = {}
    # owner = Profile.objects.get(user=request.user)
    # print("owner", owner)
    # followers = owner.follower.values_list("id", flat=True).distinct()
    # print("followers all ", followers)
    # print("posts all ", Post.objects.all())
    # posts = Post.objects.filter(user__in=followers)
    # items = Item.objects.filter(post_id__in=posts)
    # diction["mood"] = '{ "name":"John", "age":30, "city":"New York"}'
    # diction['game'] = '{ "name":"John", "age":30, "city":"New York"}'

    return HttpResponse(json.dumps(diction), content_type='application/json')
