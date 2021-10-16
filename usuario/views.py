import django.views.generic
from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import UsuarioForm


# class PrimeiroAcessoAlunoView(CreateView):
#     template_name = 'registrar_aluno.html'
#     form_class = UsuarioForm
#     success_url = reverse_lazy('painel_login_aluno')


class PainelLoginAlunoView(TemplateView):
    template_name = 'painel_login_aluno.html'

#
# class LogoutView(TemplateView):
#     template_name = 'index.html'


class UsuarioCreate(CreateView):
    template_name = 'registrar_aluno.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('painel_login_aluno')

    # def form_valid(self, form):
        # grupo = get_object_or_404(Group, name="Docentes")
        # url = super().form_valid(form)

        # depois de criar objeto
        # self.object.groups.add(grupo)
        # self.object.save()

        # Perfil.objects.create(usuario=self.object)

        # return url

    # def get_context_data(self, *args, **kwargs):
    #     context = super().get_context_data(*args, **kwargs)
    #
    #     context['titulo'] = 'Registro de novo usuario'
    #     context['botao'] = 'cadastrar'
    #
    #     return context
