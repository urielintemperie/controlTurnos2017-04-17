from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib.auth import login, authenticate, logout
from .forms import *
import datetime
from .models import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

"Pagina Inicio"
@login_required
def home(request):
    today=str(datetime.date.today())
    return redirect('/cambioDia/'+today)
    #lo redirijo directamente a cambioDia con el dia que es para que ya me cargue los turnos
'''
    if request.method == 'POST':
        form = turnoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoTurno')
    else:
        form = turnoForm()

    #form = turnoForm()
    today=datetime.date.today()
    medicos= Medico.objects.all()
    return render(request, 'aplicacionTurnos/home.html', {'today':today.isoformat(), 'medicos':medicos,'form':form})
    #return render(request, 'aplicacionTurnos/home.html', {'today':today.isoformat(), 'medicos':medicos})
'''

@login_required
def dobleForm(request):
    '''if request.method == 'POST':
        form = turnoForm(request.POST)
        if form.is_valid():
            turno = form.save(commit=True)
            #return redirect('/nuevoTurno')
            #return redirect('/cambioDia/'+str(turno.horario.dia))
    else:
        form = turnoForm()'''
    if request.method == 'POST':
        formPaciente = pacienteForm(request.POST, prefix="p")
        formObraSocial = obraSocialForm(request.POST, prefix="os")

        if formPaciente.is_valid() and formObraSocial.is_valid():
            paciente = formPaciente.save(commit=False)
            paciente.estaActivo = True
            paciente.obraSocial = formObraSocial.save()
            paciente.save()
            return redirect('/nuevoPaciente')
    else:
        formPaciente = pacienteForm(prefix="p")
        formObraSocial = obraSocialForm(prefix="os")
        '''
    if request.method == 'POST':

        form = obraSocialForm(request.POST, prefix="os")
        if form.is_valid():
            obraSocial = form.save(commit=True)
            #return redirect('/nuevoObraSocial')
    else:
        form = obraSocialForm(prefix="os")
    if request.method == 'POST':
        formPaciente = pacienteForm(request.POST, prefix="p")
        if formPaciente.is_valid():
            paciente = formPaciente.save(commit=True)
            paciente.estaActivo = True
            paciente.obraSocial = obraSocial
            paciente.save()
            #return redirect('/nuevoPaciente')
    else:
        formPaciente = pacienteForm(prefix="p")
        '''
    return render(request, 'aplicacionTurnos/dobleForm.html', {'formObraSocial': formObraSocial, 'formPaciente':formPaciente})

@login_required
def dobleFormTurno(request):
    if request.method == 'POST':
        formTurno = turnoForm(request.POST, prefix="t")
        formHorario = horarioTurnoForm(request.POST, prefix="h")
        print(formTurno.data['t-medico'])
        if formTurno.is_valid() and formHorario.is_valid():
            turno = formTurno.save(commit=False)
            turno.horario = formHorario.save()
            turno.save()
            return redirect('/')
        '''
        if formTurno.is_valid():
            print(formTurno.data['t-medico'])
            idMedico=formTurno.data['t-medico']
            formHorario = horarioTurnoForm(medico_id=idMedico,request.POST, prefix="h")
            if formHorario.is_valid():
                turno = formTurno.save(commit=False)
                turno.horario = formHorario.save()
                turno.save()
                return redirect('/')
        '''
    else:
        formTurno = turnoForm(prefix="t")
        formHorario = horarioTurnoForm(prefix="h")
    return render(request, 'aplicacionTurnos/dobleFormTurno.html', {'formTurno': formTurno, 'formHorario':formHorario})

@login_required
def cambioDia(request, dia):
    if request.method == 'POST':
        form = turnoForm(request.POST)
        if form.is_valid():
            turno = form.save(commit=True)
            #return redirect('/nuevoTurno')
            return redirect('/cambioDia/'+str(turno.horario.dia))
    else:
        form = turnoForm()
    turnos = Turno.objects.filter(dia=dia, estaActivo=True)
    medicos= Medico.objects.filter(estaActivo = True)
    return render(request, 'aplicacionTurnos/home.html', {'today':dia, 'turnos':turnos, 'medicos':medicos, 'form':form})
    #return render(request, 'aplicacionTurnos/home.html', {'today':dia})


#changeDay filtra tambien por medico, falta reparar calendario
@login_required
def changeDay(request, dia, medicopk):
    if request.method == 'POST':
        form = turnoForm(request.POST)
        if form.is_valid():
            turno = form.save(commit=True)
            #return redirect('/nuevoTurno')
            return redirect('/cambioDia/'+str(turno.horario.dia))
    else:
        form = turnoForm()
    turnos = Turno.objects.filter(horario__dia= dia, estaActivo = True, medico__pk=medicopk)
    medicos= Medico.objects.filter(estaActivo = True)
    return render(request, 'aplicacionTurnos/home.html', {'today':dia, 'turnos':turnos, 'medicos':medicos, 'form':form})


'''
def cambioDia(request, dia, medicopk):

    if request.method == 'POST':
        form = turnoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoTurno')
    else:
        form = turnoForm()
    turnos = Turno.objects.filter(medico__pk= medicopk, horario__dia= dia, estaActivo = True)
    medicos= Medico.objects.filter(estaActivo = True)
    return render(request, 'aplicacionTurnos/home.html', {'today':dia, 'turnos':turnos, 'medicos':medicos, 'medicoSeleccionado':medicopk, 'form':form})
    #return render(request, 'aplicacionTurnos/home.html', {'today':dia})
'''

"ABM Paciente"
@login_required
def nuevoPaciente(request):
    pacientes = Paciente.objects.filter(estaActivo = True).order_by('apellido')
    if request.method == 'POST':
        form = pacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=True)
            paciente.estaActivo = True
            paciente.save()
            return redirect('/nuevoPaciente')
    else:
        form = pacienteForm()
    return render(request, 'aplicacionTurnos/nuevoPaciente.html', {'form': form, 'pacientes':pacientes})

@login_required
def editarPaciente(request, pk):
    paciente = Paciente.objects.get(pk=pk)
    if request.method == 'POST':
        form = pacienteForm(request.POST, instance = paciente)
        if form.is_valid():
            paciente.estaActivo = True
            paciente = form.save(commit=True)
            return redirect('/nuevoPaciente')
    else:
        form = pacienteForm(instance = paciente)
    return render(request, 'aplicacionTurnos/editarPaciente.html',{'form':form})

@login_required
def eliminarPaciente(request , pk):
    paciente = Paciente.objects.get(pk=pk)
    paciente.estaActivo = False
    paciente.save()
    return redirect ('aplicacionTurnos.views.nuevoPaciente')

"ABM Medico"
@login_required
def nuevoMedico(request):
    medicos = Medico.objects.filter(estaActivo = True).order_by('apellido')
    if request.method == 'POST':
        form = medicoForm(request.POST)
        if form.is_valid():
            medico = form.save(commit=True)
            medico.estaActivo = True
            medico.save()
            #form.estaActivo = True
            #form.save(commit=True)
            return redirect('/nuevoMedico')
    else:
        form = medicoForm()
    #return redirect('/')
    return render(request, 'aplicacionTurnos/nuevoMedico.html',{'form':form, 'medicos':medicos})

@login_required
def editarMedico(request, pk):
    medico = Medico.objects.get(pk=pk)
    if request.method == 'POST':
        form = medicoForm(request.POST, instance = medico)
        if form.is_valid():
            medico.estaActivo = True
            medico = form.save(commit=True)
            return redirect('/nuevoMedico')
        '''
        if 'eliminar' in request.POST:
            medico.delete()
            return redirect('/nuevoMedico')
        elif form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoMedico')
        '''
        '''
        if form.is_valid():
            form.save(commit=True)
            return redirect('/')
            #return redirect('/nuevoMedico')
        else:
            return redirect('/')
        '''
    else:
        form = medicoForm(instance = medico)
    return render(request, 'aplicacionTurnos/editarMedico.html',{'form':form})

@login_required
def eliminarMedico(request , pk):
    medico = Medico.objects.get(pk=pk)
    medico.estaActivo = False
    medico.save()
    return redirect ('aplicacionTurnos.views.nuevoMedico')

"ABM Tratamiento"
@login_required
def nuevoTratamiento(request):
    tratamientos = Tratamiento.objects.filter(estaActivo = True).order_by('nombre')
    if request.method == 'POST':
        form = tratamientoForm(request.POST)
        if form.is_valid():
            tratamiento = form.save(commit=True)
            tratamiento.estaActivo = True
            tratamiento.save()
            return redirect('/nuevoTratamiento')
    else:
        form = tratamientoForm()
    return render(request, 'aplicacionTurnos/nuevoTratamiento.html',{'form':form, 'tratamientos':tratamientos})

@login_required
def editarTratamiento(request, pk):
    tratamiento = Tratamiento.objects.get(pk=pk)
    if request.method == 'POST':
        form = tratamientoForm(request.POST, instance = tratamiento)
        if form.is_valid():
            tratamiento.estaActivo = True
            form.save(commit=True)
            return redirect('/nuevoTratamiento')
    else:
        form = tratamientoForm(instance = tratamiento)
    return render(request, 'aplicacionTurnos/editarTratamiento.html',{'form':form})

@login_required
def eliminarTratamiento(request , pk):
    tratamiento = Tratamiento.objects.get(pk=pk)
    tratamiento.estaActivo = False
    tratamiento.save()
    return redirect ('aplicacionTurnos.views.nuevoTratamiento')

"ABM obraSocial"
@login_required
def nuevoObraSocial(request):
    obrasSociales = ObraSocial.objects.filter(estaActivo = True).order_by('nombre')
    if request.method == 'POST':
        form = obraSocialForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoObraSocial')
    else:
        form = obraSocialForm()
    return render(request, 'aplicacionTurnos/nuevoObraSocial.html',{'form':form, 'obrasSociales':obrasSociales})

@login_required
def editarObraSocial(request, pk):
    obraSocial = ObraSocial.objects.get(pk=pk)
    if request.method == 'POST':
        form = obraSocialForm(request.POST, instance = obraSocial)
        if form.is_valid():
            obraSocial = form.save(commit=False)
            obraSocial.save()
            return redirect('aplicacionTurnos.views.nuevoObraSocial')
        '''
        if 'eliminar' in request.POST:
            obraSocial.delete()
            return redirect('/editarObraSocial')
        elif form.is_valid():
            form.save(commit=True)
            return redirect('/editarObraSocial')
        '''
    else:
        form = obraSocialForm(instance = obraSocial)
    return render(request, 'aplicacionTurnos/editarObraSocial.html',{'form':form})

@login_required
def eliminarObraSocial(request , pk):
    obraSocial = ObraSocial.objects.get(pk=pk)
    obraSocial.estaActivo = False
    obraSocial.save()
    return redirect ('aplicacionTurnos.views.nuevoObraSocial')

"ABM Especialidad"

@login_required
def nuevoEspecialidad(request):
    especialidades = Especialidad.objects.filter(estaActivo = True).order_by('nombre')
    if request.method == 'POST':
        form = especialidadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoEspecialidad')
    else:
        form = especialidadForm()
    return render(request, 'aplicacionTurnos/nuevoEspecialidad.html',{'form':form, 'especialidades':especialidades})

@login_required
def editarEspecialidad(request, pk):
    especialidad = Especialidad.objects.get(pk=pk)
    if request.method == 'POST':
        form = especialidadForm(request.POST, instance = especialidad)
        if form.is_valid():
            especialidad = form.save(commit=False)
            especialidad.save()
            return redirect('aplicacionTurnos.views.nuevoEspecialidad')
        '''
        if 'eliminar' in request.POST:
            especialidad.delete()
            return redirect('/editarEspecialidad')
        elif form.is_valid():
            form.save(commit=True)
            return redirect('/editarEspecialidad')
        '''
    else:
        form = especialidadForm(instance = especialidad)
    return render(request, 'aplicacionTurnos/editarEspecialidad.html',{'form':form})

@login_required
def eliminarEspecialidad(request , pk):
    especialidad = Especialidad.objects.get(pk=pk)
    especialidad.estaActivo = False
    especialidad.save()
    return redirect ('aplicacionTurnos.views.nuevoEspecialidad')

"AMB Turno"
@login_required
def docAndDay(request):
    medicos = Medico.objects.all()
    if request.method == 'POST':
        doc = request.POST.get('doc')
        dia = request.POST.get('date')
        return redirect('nuevoTurno/{doc}/{dia}'.format(doc=doc, dia=dia))
#        return nuevoTurno(request, doc, dia)
    else:
        return render(request, 'aplicacionTurnos/docAndDay.html', {'medicos':medicos})

@login_required
def nuevoTurno(request, doc, dia):
    diaDeLaSemana = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    doctor = Medico.objects.get(pk=doc)
    turnos_doc = Turno.objects.filter(estaActivo=True, pk=doc, horario__isnull=True).order_by('horario')

    doc_horario = doctor.horario.filter(dia=diaDeLaSemana[datetime.datetime.strptime(dia, '%Y-%m-%d').date().weekday()])
    horarios = []
    for horario in doc_horario:
        doc_inicio = getattr(horario, 'horaInicio')
        doc_fin = getattr(horario, 'horaFin')
        horarios = crearHorarios(horarios, doc_inicio, doc_fin)

    if request.method == 'POST':

        lista_horarios = request.POST.getlist('hour')
        for h in lista_horarios:
            form = turnoForm(request.POST, initial={
            'medico':doctor,
            'especialidad':doctor.espec,
            'dia':datetime.datetime.strptime(dia, '%Y-%m-%d').date(),
            'horarios':h
            })
            if form.is_valid():
                form.save(commit=True)
                return redirect('/nuevoTurno')
    else:
        turnos = Turno.objects.filter(estaActivo = True).order_by('horario')
        form = turnoForm(initial={
        'medico':doctor,
        'especialidad':doctor.espec,
        'dia':dia,
        'horarios':horarios
        })
        return render(request, 'aplicacionTurnos/nuevoTurno.html', {'form': form, 'turnos':turnos, 'horarios':horarios})

@login_required
def editarTurno(request, pk):
    Turno.objects.filter(estaActivo=True).exists()
    turno = Turno.objects.get(pk=pk)
    if request.method == 'POST':
        form = turnoForm(request.POST, instance = turno)
        if form.is_valid():
            turno = form.save(commit=False)
            turno.save()
            print ("turno modificado")
            diaTurno = str(turno.horario.dia)
            return redirect('/cambioDia/'+diaTurno)
        '''
        if 'eliminar' in request.POST:
            turno.delete()
            return redirect('/nuevoTurno')
        elif form.is_valid():
            form.save(commit=True)
            return redirect('/nuevoTurno')
        '''
    else:
        form = turnoForm(instance = turno)
    #return render(request, 'aplicacionTurnos/editarTurno.html',{'form':form})
    return render(request, 'aplicacionTurnos/editarTurnoPopUp.html',{'form':form})

@login_required
def eliminarTurno(request , pk):
    turno = Turno.objects.get(pk=pk)
    diaTurno = str(turno.horario.dia)
    turno.estaActivo = False
    turno.save()
    #return redirect ('/nuevoTurno')
    # redirije al mismo dia desde el que se borro el turno
    return redirect ('/cambioDia/'+diaTurno)

"Login with Model User of django"
class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated():
            return redirect('/')
        else:
            form = LoginForm()
            return render(request, 'aplicacionTurnos/login.html', {'form': form})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=User.objects.get(username= request.POST['username']), password=request.POST['password'])
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'aplicacionTurnos/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')

@login_required
def busquedaPaciente(request):
    #pacientes = Paciente.objects.order_by('apellido')
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(dni__icontains=query)
        )
        #Ademas de los filtros del qset, filtro por si el paciente esta activo o no
        results = Paciente.objects.filter(qset,estaActivo=True).distinct()
    else:
        return redirect('aplicacionTurnos.views.nuevoPaciente')
    if request.method == 'POST':
        form = pacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=True)
            paciente.estaActivo = True
            paciente.save()
            return redirect('/nuevoPaciente')
    else:
        form = pacienteForm()
    return render(request, 'aplicacionTurnos/nuevoPaciente.html', {'form': form, 'pacientes':results})

@login_required
def busquedaMedico(request):
    #pacientes = Paciente.objects.order_by('apellido')
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(nombre__icontains=query) |
            Q(apellido__icontains=query) |
            Q(dni__icontains=query) |
            Q(especialidad__nombre__icontains=query)
        )
        #Ademas de los filtros del qset, filtro por si el paciente esta activo o no
        results = Medico.objects.filter(qset,estaActivo=True).distinct()
    else:
        return redirect('aplicacionTurnos.views.nuevoMedico')
    if request.method == 'POST':
        form = medicoForm(request.POST)
        if form.is_valid():
            medico = form.save(commit=True)
            medico.estaActivo = True
            medico.save()
            return redirect('/nuevoMedico')
    else:
        form = medicoForm()
    return render(request, 'aplicacionTurnos/nuevoMedico.html',{'form':form, 'medicos':results})

@login_required
def busquedaEspecialidad(request):
    #pacientes = Paciente.objects.order_by('apellido')
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )
        #Ademas de los filtros del qset, filtro por si el paciente esta activo o no
        results = Especialidad.objects.filter(qset).distinct()
    else:
        return redirect('aplicacionTurnos.views.nuevoEspecialidad')
    if request.method == 'POST':
        form = especialidadForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('aplicacionTurnos.views.nuevoEspecialidad')
    else:
        form = especialidadForm()
    return render(request, 'aplicacionTurnos/nuevoEspecialidad.html',{'form':form, 'especialidades':results})

@login_required
def busquedaTratamiento(request):
    #pacientes = Paciente.objects.order_by('apellido')
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )
        #Ademas de los filtros del qset, filtro por si el paciente esta activo o no
        results = Tratamiento.objects.filter(qset).distinct()
    else:
        return redirect('aplicacionTurnos.views.nuevoTratamiento')
    if request.method == 'POST':
        form = tratamientoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('aplicacionTurnos.views.nuevoTratamiento')
    else:
        form = tratamientoForm()
    return render(request, 'aplicacionTurnos/nuevoTratamiento.html',{'form':form, 'tratamientos':results})

@login_required
def busquedaObraSocial(request):
    #pacientes = Paciente.objects.order_by('apellido')
    query = request.GET.get('q','')
    if query:
        qset = (
            Q(nombre__icontains=query)
        )
        #Ademas de los filtros del qset, filtro por si el paciente esta activo o no
        results = ObraSocial.objects.filter(qset).distinct()
    else:
        return redirect('aplicacionTurnos.views.nuevoObraSocial')
    if request.method == 'POST':
        form = obraSocialForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('aplicacionTurnos.views.nuevoObraSocial')
    else:
        form = obraSocialForm()
    return render(request, 'aplicacionTurnos/nuevoObraSocial.html',{'form':form, 'obrasSociales':results})

def crearHorarios(horarios,inicio, fin):
    sec_inicio = getSeconds(inicio)
    sec_fin = getSeconds(fin)
    #horarios = []
    h = sec_inicio
    while (h < sec_fin):
        horarios.append(datetime.timedelta(seconds=h))
        h = h + 900
    return horarios

def getSeconds(a):
    hora = a.hour*3600
    minuto = a.minute*60
    segundo = a.second
    time = hora + minuto + segundo
    return time

def turnoNuevoMagia(request):
    form = turnoNuevoMagiaForm()
    return render(request, 'aplicacionTurnos/turnoNuevoMagia.html', {'form':form})

def formCalendarioJQuery(request):
    if request.method == "POST":
            f = DateRangeForm(request.POST)
            if f.is_valid():
                c = f.save(commit = False)
                c.end_date = timezone.now()
                c.save()
    else:
        f = DateRangeForm()
        '''f = DateRangeForm()
        args = {}
        args.update(csrf(request))
        args['form'] = f'''


    return render(request, 'aplicacionTurnos/trial_balance.html', {
        'form': f
    })

'''
def creacionTurnoNormal(request):
    if request.method == "POST":
            form = CreacionTurnoNormalForm(request.POST)
            if form.is_valid():
                turno = form.save(commit=True)
                return redirect('aplicacionTurnos.views.home')
    else:
        form = CreacionTurnoNormalForm()
    return render(request, 'aplicacionTurnos/creacionTurnoNormal.html', {'form': form})
'''

def creacionTurnoNormal(request):
    if request.method == "POST":
            #form = CreacionTurnoNormalForm(request.POST)
            form = turnoNuevoMagiaForm(request.POST)
            if form.is_valid():
                turno = form.save(commit=True)
                return redirect('aplicacionTurnos.views.home')
                '''post = form.save(commit=False)
                post.author = request.user
                post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)'''
    else:
        form = turnoNuevoMagiaForm()
    return render(request, 'aplicacionTurnos/turnoNuevoMagia.html', {'form': form})
