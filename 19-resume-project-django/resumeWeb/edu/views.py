from django.shortcuts import render

# Create your views here.
def skill(req):
    context = {'skill':'active'}
    return render(req, 'edu/skill.html', context)