from django.shortcuts import render

# Create your views here.
def base_view(request):
    return render(request,'testapp/base.html')

def movies_view(request):
    images = ['movies1.jpg', 'movies2.jpg', 'movies3.jpg']
    head_msg = 'Here contains the Movies Info'
    sub_msg = ['Saripoda Sanivaram is a good movie.', 'Planning for Aashiqui-3 with Mahesh sir', "Don't go for movies. Practice Django instead."]
    type = 'movies'
    my_dict = {'images': images, 'head_msg': head_msg, 'sub_msg': sub_msg, 'type': type}
    return render(request, 'testapp/movies.html', my_dict)

def sports_view(request):
    images = ['sports1.jpg', 'sports2.jpg', 'sports3.jpg']
    head_msg = 'Here contains the Sports Info'
    sub_msg = ['Australia won the match against England.', 'Next World Cup is for India.', 'Who is upcoming coach of team India?']
    type = 'sports'
    my_dict = {'images': images, 'head_msg': head_msg, 'sub_msg': sub_msg, 'type': type}
    return render(request, 'testapp/sports.html', my_dict)

def politics_view(request):
    images = ['politics1.jpg', 'politics2.jpg', 'politics3.jpg']
    head_msg = 'Here contains the Politics Info'
    sub_msg = ['Indian prime minister is Narendra Modi.', 'Chief Minister of Odisha is Mohan Charan Majhi', 'BJP won the 2024 general election.']
    type = 'politics'
    my_dict = {'images': images, 'head_msg': head_msg, 'sub_msg': sub_msg, 'type': type}
    return render(request, 'testapp/politics.html', my_dict)