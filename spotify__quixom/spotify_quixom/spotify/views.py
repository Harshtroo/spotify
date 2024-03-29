from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView,
    FormView,
)
from django.contrib.auth.views import LoginView, LogoutView
from .form import (
    SignUpForm,
    LoginForm,
    SongForm,
    CreatePlayListForm,
    UpdatePlayListForm,
    AddToFavouriteForm,
)
from .models import User, Song, Favourite, PlayList
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.contrib.auth.models import Group, Permission
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Count

class Home(TemplateView):
    """Home page view"""
    template_name = "home.html"


class Login(LoginView):
    """Login page view"""

    form_class = LoginForm
    template_name = "login.html"
    success_url = reverse_lazy("home")


class Logout(LogoutView):
    """logout class"""
    pass


class SingUp(CreateView):
    """SignUp page view"""

    model = User
    template_name = "sing_up.html"
    form_class = SignUpForm
    success_url = reverse_lazy("login")

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            user = form.save()
            user.save()

            user_role = user.role
            group = Group.objects.get(name=user_role)
            user.groups.add(group.id)
            return HttpResponseRedirect(self.success_url)
        return render(request, "sing_up.html", {"form": form})


class SongCreate(SuccessMessageMixin, CreateView):
    template_name = "create_song.html"
    form_class = SongForm
    success_url = reverse_lazy("song_list")
    success_message = "successfully create song"

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            return self.form_valid(form)
        return render(request, self.template_name, {"form": form})


class SongList(LoginRequiredMixin, ListView):
    template_name = "song_list.html"
    context_object_name = "songs"
    queryset = Song.objects.filter(is_deleted=False)
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        favourite_count = Favourite.objects.filter(user=self.request.user).aggregate(Count("songs")).get("songs__count")
        song_active = Song.objects.values("is_deleted").annotate(total_songs=Count("id")).order_by("is_deleted")

        song_val = song_active[0]["total_songs"]
        if Favourite.objects.filter(user=self.request.user).exists():
            song_obj = Favourite.objects.filter(user=self.request.user)
            song_id_list = []
            for song in song_obj.first().songs.all():
                song_id_list.append(song.id)
            context["song_id_list"] = song_id_list
            context["addplaylistform"] = AddToFavouriteForm
            context["createplaylistform"] = CreatePlayListForm
            context["favourite_count"] = favourite_count
            context["song_count"] =song_val
        return context



class SongUpdate(SuccessMessageMixin, UpdateView):
    """song updatge view"""

    model = Song
    form_class = SongForm
    template_name = "create_song.html"
    success_url = reverse_lazy("song_list")
    success_message = "successfully edit song"

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            super(SongUpdate, self).post(request, *args, **kwargs)
            return redirect(self.success_url)
        return render(request, self.template_name, {"form": form})


class SongDelete(SuccessMessageMixin, DeleteView):
    """song delete view"""

    model = Song
    success_url = reverse_lazy("song_list")
    success_message = "successfully delete song"

    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist("checkbox_ids[]")
        if selected_ids:
            Song.objects.filter(id__in=selected_ids).update(is_deleted=True)
            messages.success(request, self.success_message)
        return JsonResponse({"messages": "success"})


class AddToFavourite(CreateView):
    """song add to favourite"""

    model = Favourite

    def post(self, request, *args, **kwargs):
        song_id = self.request.POST.get("song_id")
        obj, create = Favourite.objects.get_or_create(user=self.request.user)
        if obj.songs.filter(id=song_id).exists():
            obj.songs.remove(Song.objects.get(id=song_id))
            context = {
                "is_added": False,
                "message": "Song Removed!",
                "song_id": song_id,
            }
        else:
            obj.songs.add(Song.objects.get(id=song_id))
            context = {
                "is_added": True,
                "message": "Song Added!",
                "song_id": song_id,
            }
        obj.save()
        return JsonResponse(context)


class FavouriteList(ListView):
    model = Favourite
    template_name = "favorite_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        context["fav"] = Favourite.objects.filter(user=self.request.user)
        return context


class CreatePlayList(SuccessMessageMixin, CreateView):
    form_class = CreatePlayListForm
    template_name = "play_list.html"
    success_url = reverse_lazy("song_list")
    success_message = "successfully create playlist"

    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST or None)
        if form.is_valid():
            self.object = form.save(commit=False)
            self.object.user = self.request.user
            self.object.save()
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {"form": form})


class ShowPlayList(LoginRequiredMixin, ListView):
    model = PlayList
    template_name = "show_play_list.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user"] = self.request.user
        if PlayList.objects.filter(user=self.request.user).exists():
            context["playlist"] = PlayList.objects.filter(user=self.request.user)
        return context


class UpdatePlayList(UpdateView):
    model = PlayList
    form_class = UpdatePlayListForm
    template_name = "play_list.html"
    success_url = reverse_lazy("show_playlist")

    def get(self, request, *args, **kwargs):
        playlist = self.get_object()
        form = self.form_class(instance=playlist)
        return render(request, self.template_name, {"form": form})


    def post(self, request, *args, **kwargs):
        form = self.form_class(self.request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        return render(request, self.template_name, {"form": form})


class DeletePlayList(DeleteView):
    model = PlayList
    success_url = reverse_lazy("show_playlist")

    def post(self, request, *args, **kwargs):
        PlayList.objects.filter(id=kwargs["pk"]).delete()
        return HttpResponseRedirect(self.success_url)


class AddToPlaylist(LoginRequiredMixin, CreateView, ListView):
    form_class = AddToFavouriteForm
    success_url = reverse_lazy("show_playlist")

    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist("selected_ids[]")
        id_playlist = request.POST.get("id_playlist")
        # if id_playlist == '':
        #     messages.warning(request,"please select any one playlist")
        playlist = get_object_or_404(PlayList, id=id_playlist)

        songs = Song.objects.filter(id__in=selected_ids)
        if len(songs) == 0:
            messages.warning(request, "Please select at least one song.")
            return redirect(self.success_url)

        for song in songs:
            if song in PlayList.objects.all():
                messages.warning(request, f"The song '{song.name}' is already in the playlist.")
        playlist.songs.add(*songs)
        return redirect(self.success_url)


class MulSongCreatePlaylist(LoginRequiredMixin, CreateView):
    model = PlayList
    form_class = CreatePlayListForm
    success_url = reverse_lazy("show_playlist")

    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist("selected_ids[]")
        songs = Song.objects.filter(id__in=selected_ids)
        playlist_name = request.POST.get("form")

        if PlayList.objects.filter(name__icontains=playlist_name).exists():
            messages.warning(request, "This playlist name already exists.")
            return redirect(self.success_url)
        create_playlist = PlayList.objects.create(name=playlist_name, user=self.request.user)
        create_playlist.songs.add(*selected_ids)
        return redirect(self.success_url)


class RemovePlayListSongs(DeleteView):
    form_class = AddToFavouriteForm
    success_url = reverse_lazy("show_playlist")

    def post(self, request, *args, **kwargs):
        selected_ids = request.POST.getlist("selected_ids[]")
        id_playlist = request.POST.get("id_playlist")
        print("id_playlist", id_playlist)
        songs = Song.objects.filter(id__in=selected_ids)
        playlist = get_object_or_404(PlayList, id=id_playlist)

        # for song in songs:
        #     if song in PlayList.objects.all():
        #         messages.warning(request, f"The song '{song.name}' is already in the playlist.")
        for value in selected_ids:
            playlist.songs.remove(value)
        return redirect(self.success_url)
