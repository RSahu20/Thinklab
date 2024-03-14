from django.shortcuts import render, redirect
from .forms import UploadFileForm,CellInformationForm
from impedance import preprocessing
from impedance.models.circuits import CustomCircuit
import matplotlib
matplotlib.use('Agg')
from .models import GeneratedID

import matplotlib.pyplot as plt
from impedance.visualization import plot_nyquist
import os

def generate_id(request):
    generated_id = 'elementId'

   
    GeneratedID.objects.create(image_id=generated_id)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            csv_data = request.FILES['csv_file']
            frequencies, Z = preprocessing.readCSV(csv_data)
            
            # Preprocess data if necessary
            frequencies, Z = preprocessing.ignoreBelowX(frequencies, Z)
            
            # Define impedance model
            circuit = 'R0-p(R1,C1)-p(R2-Wo1,C2)'
            initial_guess = [.01, .01, 100, .01, .05, 100, 1]
            circuit = CustomCircuit(circuit, initial_guess=initial_guess)
            
            # Fit impedance model to data
            circuit.fit(frequencies, Z)
            
            # Extract fit parameters
            fit_parameters = circuit.parameters_
            
            # Generate fit impedance data
            Z_fit = circuit.predict(frequencies)



           
            # Visualize the fit
            fig, ax = plt.subplots()
            plot_nyquist(Z, fmt='o', scale=10, ax=ax)
            plot_nyquist(Z_fit, fmt='-', scale=10, ax=ax)
            plt.legend(['Data', 'Fit'])
            
            # Save the plot to a file
            plot_file = 'fit_plot.png'
            plot_path = os.path.join('media', plot_file)  # Assuming 'media' is your media root directory
            plt.savefig(plot_path)
            
            # Calculate State-of-the-Health (SoH) percentage
            current_rb_index = 0  # Assuming 'Rb' is the first parameter
            current_rb = fit_parameters[current_rb_index]
            
            max_rb = 0.1  # Example maximum resistance value
            soh_percentage = (current_rb / max_rb) * 100
            degraded_percentage = 100 - soh_percentage
             # Define min and max values for parameters
            min_values = [0.01, 0.001, 1, 0.001, 0.01,100, 0.1]
            max_values = [0.1, 0.011, 50, 0.015, 1, 300,0.4]
            parameter_names = ['R0', 'R1', 'C1', 'R2', 'Wo1,0','Wo0,1','C2']
            explanation=['Electrolyte resistance','Resistance due to SEI layer','Capacitance due to SEI layer',
                        'electrode–electrolyte interface',
                        'Double-layer capacitance','Frequency-dependent Warburg impedance models','']
            # Combine parameter names, values, min, and max values
            #parameters = zip(['R0', 'R1', 'C1', 'R2', 'Wo1,0','Wo0,1','C2'], fit_parameters, min_values, max_values)
            context = {
             'parameters': zip(parameter_names, fit_parameters,explanation,min_values,max_values),
             'soh_percentage': soh_percentage,
             'plot_file':plot_path,
             'degraded_percentage':degraded_percentage
                }
            
            # Pass parameters to template
            #context = {'parameters': parameters}
            
            # Pass the fit parameters, plot path, and SoH to the result page
            return render(request, 'results.html', context)
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})

def result_page(request):
    return render(request, 'results.html')

def upload_cell_information(request):
    if request.method == 'POST':
        form = CellInformationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')  # Redirect to a success page after saving
    else:
        form = CellInformationForm()
    return render(request, 'upload_cell_information.html', {'form': form})
