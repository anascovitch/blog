
# Create your views here.

from .forms import ImagePostForm
from django.shortcuts import render, redirect,get_object_or_404
from .forms import CustomUserCreationForm,CustomUserChangeForm, ImagePostForm
from django.contrib.auth.models import Group
from .forms import ImagePostForm
from .models import CustomUser, ImagePost
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.urls import reverse
from django.http import Http404
from django.contrib.auth.views import PasswordChangeView #PasswordResetView, PasswordResetConfirmView
from django.views.generic import TemplateView
from django.urls import reverse_lazy


# url = reverse('monapp:profile_view')

# Vue pour la page d'accueil
def home(request):
    context = {}
    # Vous pouvez ajouter plus de contexte si nécessaire, par exemple :
    context['latest_posts'] = ImagePost.objects.all().order_by('-date_creation')[:5]
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            # Assurez-vous que le groupe existe, et ajoutez l'utilisateur au groupe
            group_name = "Abonné"  # Remplacez par le nom de votre groupe
            group, created = Group.objects.get_or_create(name=group_name)
            user.groups.add(group)

            return redirect('home')
    else:
        form = CustomUserCreationForm()

    return render(request, 'register.html', {'form': form})




@login_required
def upload_image(request):
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.auteur= request.user
            post.save()
            
            return redirect('monapp:profile_view', username=request.user.username)  # Redirect to a success page
    else:
        form = ImagePostForm()
    return render(request, 'upload_image.html', {'form': form})


def feed(request):
    # Afficher les posts dans l'ordre de création
    posts = ImagePost.objects.all().order_by('-date_creation')
    return render(request, 'feed.html', {'posts': posts})

def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    posts = ImagePost.objects.filter(auteur=user)
    return render(request, 'user_profile.html', {'user_profile': user, 'posts': posts})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('monapp:user_profile', username=request.user.username)
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})

# Vue pour afficher le profil utilisateur et ses posts
User = get_user_model()

@login_required
def profile_view(request, username):
    # Vérifier que le username correspond à l'utilisateur connecté
    if username != request.user.username:
        raise Http404("Page non trouvée.")

    user = get_object_or_404(User, username=username)
    posts = ImagePost.objects.filter(auteur=user)
    return render(request, 'profile.html', {'user': user, 'posts': posts})

def edit_post(request, post_id):
    post = get_object_or_404(ImagePost, id=post_id, auteur=request.user)
    if request.method == 'POST':
        form = ImagePostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('monapp:user_profile', username=request.user.username)
    else:
        form = ImagePostForm(instance=post)
    
    return render(request, 'edit_post.html', {'form': form, 'post': post})

# Vue pour afficher les détails d'un post
def post_detail(request, post_id):
    post = get_object_or_404(ImagePost, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

# Vue pour supprimer un post
# @login_required
# @require_POST
# def delete_post(request, post_id):
#     post = get_object_or_404(ImagePost, id=post_id)
    
#     # Vérifiez que l'utilisateur connecté est l'auteur du post
#     if request.user == post.auteur:
#         post.delete()
#         messages.success(request, "Le post a été supprimé avec succès.")
#         return redirect('home')  # Redirigez vers la page d'accueil ou la liste des posts
#     else:
#         messages.error(request, "Vous n'avez pas la permission de supprimer ce post.")
#         return redirect('monapp:post_detail',post_id=post.id)
    
#     return render(request, 'delete_post.html', {'post': post})
    
# # Vue pour confirmer la suppression d'un post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(ImagePost, id=post_id)

    if request.method == 'POST':
        # Vérifiez que l'utilisateur connecté est l'auteur du post
        if request.user != post.auteur:
            messages.error(request, "Vous n'avez pas la permission de supprimer ce post.")
            return redirect('home')
        if request.method == 'POST':
            post.delete()
            messages.success(request, "Le post a été supprimé avec succès.")
        return redirect('monapp:profile_view', username=request.user.username)

    return render(request, 'delete_post.html', {'post': post})



@login_required
def profile_redirect(request):
    # Récupérer le nom d'utilisateur de l'utilisateur connecté
    username = request.user.username
    # Rediriger vers la vue de profil de l'utilisateur avec le bon username
    return redirect('user_profile.html', username=username)

@login_required
def login_redirect(request):
    return redirect('monapp:user_profile', username=request.user.username)

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'change_password.html'
    success_url = '/password_change_done/'  # Redirigez vers une URL appropriée après le changement
    
def password_change_done(request):
    return render(request, 'password_change_done.html')

class PasswordChangeDoneView(TemplateView):
    template_name = 'password_change_done.html'
    
    
def custom_logout(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté avec succès.")
    return render(request, 'logout.html')

# class CustomPasswordResetView(PasswordResetView):
#     template_name = 'password_reset.html'
#     email_template_name = 'password_reset_email.html'
#     success_url = 'password_reset_confirm.html'
    
    
# class CustomPasswordResetConfirmView(PasswordResetConfirmView):
#     template_name = 'password_reset_confirm.html'  # Spécifiez votre template personnalisé
#     success_url = reverse_lazy('password_reset_done')  # Redirection après la réinitialisation réussie
#     # Vous pouvez personnaliser d'autres aspects si nécessaire

#     def form_valid(self, form):
#         # Logique personnalisée en cas de validation réussie du formulaire
#         messages.success(self.request, "Votre mot de passe a été réinitialisé avec succès.")
#         return super().form_valid(form)