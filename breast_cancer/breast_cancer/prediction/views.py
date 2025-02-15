# prediction/views.py
from django.shortcuts import render
from .agents import predict  # Import the prediction function


# View for prediction
def predict_view(request):
    if request.method == 'POST':
        # Get input data from the form
        input_data_str = request.POST['features']

        # Convert the comma-separated string to a list of floats
        input_data = [float(x) for x in input_data_str.split(',')]

        # Make prediction using the agent
        result = predict(input_data)

        # Display the result
        if result == 1:
            prediction_result = 'Cancerous'
        else:
            prediction_result = 'Not Cancerous'

        return render(request, 'prediction/result.html', {'result': prediction_result})

    return render(request, 'prediction/form.html')
