from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .forms import CreatePollForm
from .models import Poll


def polls(request):
    polls = Poll.objects.all()
    queryset = Poll.objects.filter(approved=1)
    context = {
        'polls': polls
    }
    return render(request, 'polls/polls.html', context)


@login_required
def results(request, polls_id):
    polls = polls.objects.get(pk=polls_id)

    context = {
        'polls': polls
    }
    return render(request, 'polls/results.html', context)


@login_required
def vote(request, polls_id):
    polls = Poll.objects.get(pk=polls_id)

    if request.method == 'POST':

        selected_choice = request.POST['polls']
        if selected_choice == 'choice1':
            polls.choice_one_count += 1
        elif selected_choice == 'choice2':
            polls.choice_two_count += 1
        elif selected_choice == 'choice3':
            polls.choice_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form choice')

        polls.save()

        return redirect('results', polls.id)

    context = {
        'polls': poll
    }
    return render(request, 'polls/vote.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)

        if form.is_valid():
            form.save(commit=False)

            return redirect('polls')
    else:
        form = CreatePollForm()

    context = {'form': form}
    return render(request, 'polls/create.html', context)
