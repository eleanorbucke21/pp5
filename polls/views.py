
from django.shortcuts import render
from django.shortcuts import redirect

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib import messages

from .forms import CreatePollForm
from .models import Poll


def poll(request):
    poll = Poll.objects.all()
    queryset = Poll.objects.filter(approved=1)
    print("IN POLLS VIEW")
    context = {
        'polls': poll
    }
    return render(request, 'polls/polls.html', context)


@login_required
def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    print("IN VOTE VIEW")

    if request.method == 'POST':

        selected_choice = request.POST['poll']
        if selected_choice == 'choice1':
            poll.choice_one_count += 1
        elif selected_choice == 'choice2':
            poll.choice_two_count += 1
        elif selected_choice == 'choice3':
            poll.choice_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form choice')
        poll.save()
        return redirect('success', poll.id)
    context = {
        'poll': poll
    }
    return render(request, 'polls/polls.html', context)


@login_required
def success(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll': poll
    }
    return render(request, 'polls/success.html', context)


@login_required
def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    context = {
        'poll': poll
    }
    return render(request, 'polls/results.html', context)


@login_required
def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            return redirect('poll')
            messages.success(request, 'Your poll is under review!')
    else:
        form = CreatePollForm()
        messages.error(request, 'There was an error Please try again')
    context = {'form': form}
    return render(request, 'polls/create.html', context)
