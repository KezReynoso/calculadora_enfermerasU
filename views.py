from django.shortcuts import render
from django.views import View
from .forms import CalculatorForm

class Index(View):
    def get(self, request):
        form = CalculatorForm()
        return render(request, 'calculadora/index.html',{'form': form})


    def post(self, request):
        form = CalculatorForm(request.POST)

        if form.is_valid():
            turnos_de_12hrs = int(form.cleaned_data['turnos_de_12hrs'])
            horas_sueltas = int(form.cleaned_data['horas_sueltas'])
            costo_por_turno = form.cleaned_data['costo_por_turno']
            costo_por_horas_sueltas = form.cleaned_data['costo_por_horas_sueltas']
            costo_cliente = turnos_de_12hrs * costo_por_turno + horas_sueltas * costo_por_horas_sueltas
            
            context = {
                'costo_cliente': costo_cliente,
                'turnos_de_12hrs': turnos_de_12hrs,
                'horas_sueltas': horas_sueltas,
                'costo_por_turno' : costo_por_turno,
                'costo_por_horas_sueltas': costo_por_horas_sueltas,

            }

        return render(request, 'calculadora/resultado.html', context)