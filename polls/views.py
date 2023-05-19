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

        selected_option = request.POST['polls']
        if selected_option == 'option1':
            polls.option_one_count += 1
        elif selected_option == 'option2':
            polls.option_two_count += 1
        elif selected_option == 'option3':
            polls.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form option')

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
