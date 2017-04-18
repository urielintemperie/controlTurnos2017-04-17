from django.conf.urls import url
from . import views
from .views import LoginView

urlpatterns = [
    url(r'^login$', LoginView.as_view()),
    url(r'^logout$', views.logout_view) ,
    url(r'^login$', LoginView.as_view()),
    url(r'^$', views.home),
    url(r"^cambioDia/(?P<dia>\S+)$", views.cambioDia),
    url(r"^changeDay/(?P<dia>\S+)/(?P<medicopk>\S+)", views.changeDay),
    url(r'^nuevoPaciente$', views.nuevoPaciente),
    url(r'^editarPaciente/(?P<pk>[0-9]+)/$', views.editarPaciente),
    url(r'^eliminarPaciente/(?P<pk>[0-9]+)/$', views.eliminarPaciente),
    url(r'^nuevoMedico$', views.nuevoMedico),
    url(r'^editarMedico/(?P<pk>[0-9]+)/$', views.editarMedico),
    url(r'^eliminarMedico/(?P<pk>[0-9]+)/$', views.eliminarMedico),
    url(r'^nuevoTratamiento$', views.nuevoTratamiento),
    url(r'^editarTratamiento/(?P<pk>[0-9]+)/$', views.editarTratamiento),
    url(r'^eliminarTratamiento/(?P<pk>[0-9]+)/$', views.eliminarTratamiento),
    url(r'^nuevoEspecialidad$', views.nuevoEspecialidad),
    url(r'^editarEspecialidad/(?P<pk>[0-9]+)/$', views.editarEspecialidad),
    url(r'^eliminarEspecialidad/(?P<pk>[0-9]+)/$', views.eliminarEspecialidad),
    url(r'^nuevoObraSocial$', views.nuevoObraSocial),
    url(r'^editarObraSocial/(?P<pk>[0-9]+)/$', views.editarObraSocial),
    url(r'^eliminarObraSocial/(?P<pk>[0-9]+)/$', views.eliminarObraSocial),
    url(r'^docAndDay/nuevoTurno/(?P<doc>\S+)/(?P<dia>\S+)$', views.nuevoTurno, name='nuevoTurno'),
    url(r'^editarTurno/(?P<pk>[0-9]+)/$', views.editarTurno),
    url(r'^eliminarTurno/(?P<pk>[0-9]+)/$', views.eliminarTurno),
    url(r'^busquedaPaciente/$', views.busquedaPaciente),
    url(r'^busquedaMedico/$', views.busquedaMedico),
    url(r'^busquedaEspecialidad/$', views.busquedaEspecialidad),
    url(r'^busquedaTratamiento/$', views.busquedaTratamiento),
    url(r'^busquedaObraSocial/$', views.busquedaObraSocial),
    url(r'^dobleForm/$', views.dobleForm),
    url(r'^dobleFormTurno/$', views.dobleFormTurno),
    url(r'^docAndDay/$', views.docAndDay),
    url(r'^turnoNuevoMagia/$', views.turnoNuevoMagia),
    url(r'^formCalendarioJQuery/$', views.formCalendarioJQuery),
    url(r'^creacionTurnoNormal/$', views.creacionTurnoNormal),
]
