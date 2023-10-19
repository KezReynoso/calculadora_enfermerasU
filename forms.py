from django import forms

class CalculatorForm(forms.Form):
    turnos_de_12hrs = forms.FloatField()
    costo_por_turno = forms.FloatField()
    horas_sueltas = forms.FloatField()
    costo_por_horas_sueltas = forms.FloatField()