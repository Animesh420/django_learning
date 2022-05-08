from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .forms import NotesForm
from .models import Notes
from django.http import Http404, HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

class NotesCreateView(CreateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesUpdateView(UpdateView):
    model = Notes
    form_class = NotesForm
    success_url = '/smart/notes'

class NotesDeleteView(DeleteView):
    model = Notes
    success_url = "/smart/notes"
    template_name = 'notes/notes_delete.html'

class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'
    login_url = '/admin'

    def get_queryset(self):
        return self.request.user.notes.all()

# def note_lists(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})


class NoteDetailView(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/notes_detail.html'

# def details(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#         return render(request, 'notes/notes_detail.html', {'note': note})
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")

