from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .forms import DoctorForm, PatientForm, DoctorUpdateForm, DoctorIdForm, PatientIdForm, PatientUpdateForm, DepartmentForm
from .models import Doctor, Patient, Department


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                # Authentication failed
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    # Your dashboard logic here
    return render(request, 'dashboard.html')


@login_required
def view_doctors(request):
    doctors = Doctor.objects.all()
    return render(request, 'view_doctors.html', {'doctors': doctors})


@login_required
def delete_doctor(request):
    if request.method == 'POST':
        d_id = request.POST.get('d_id', '')  # Access the 'd_id' value
        try:
            # Get the doctor using the submitted d_id
            doctor = get_object_or_404(Doctor, d_id=d_id)  # Use the correct field name

            # Get additional information if needed
            doctor_name = doctor.name  # Example: Get the doctor's name

            # Delete the doctor
            doctor.delete()

            # Redirect to the view doctors page after deletion
            return redirect('view_doctors')
        except Doctor.DoesNotExist:
            error_message = f'Doctor with ID {d_id} does not exist.'
            return render(request, 'delete_failure.html', {'error_message': error_message})

    return render(request, 'delete_doctor.html')


def delete_failure(request):
    return render(request, 'delete_failure.html')


@login_required
def update_doctors(request, d_id):
    doctor = get_object_or_404(Doctor, d_id=d_id)
    if request.method == 'POST':
        form = DoctorUpdateForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect(
                'view_doctors')  # Replace 'success_url' with the URL where you want to redirect after a successful update
    else:
        form = DoctorUpdateForm(instance=doctor)
    return render(request, 'update_doctor_form.html', {'form': form})


@login_required
def get_doctor_id(request):
    if request.method == 'POST':
        form = DoctorIdForm(request.POST)
        if form.is_valid():
            d_id = form.cleaned_data['doctor_id']
            doctor = get_object_or_404(Doctor, d_id=d_id)
            return render(request, 'update_doctor_details.html', {'doctor': doctor})
    else:
        form = DoctorIdForm()
    return render(request, 'get_doctor_id.html', {'form': form})


@login_required
def get_patient_id(request):
    if request.method == 'POST':
        form = PatientIdForm(request.POST)
        if form.is_valid():
            p_id = form.cleaned_data['p_id']
            patient = get_object_or_404(Patient, p_id=p_id)
            return render(request, 'update_patient_details.html', {'patient': patient})
    else:
        form = PatientIdForm()
    return render(request, 'get_patient_id.html', {'form': form})


@login_required
def view_patients(request):
    patients = Patient.objects.all()
    return render(request, 'view_patients.html', {'patients': patients})


@login_required
def delete_patient(request):
    if request.method == 'POST':
        p_id = request.POST.get('p_id', '')  # Access the 'p_id' value
        try:
            # Get the patient using the submitted p_id
            patient = get_object_or_404(Patient, p_id=p_id)  # Use the correct field name

            # Get additional information if needed
            patient_name = patient.name  # Example: Get the patient's name

            # Delete the patient
            patient.delete()

            # Redirect to the view patients page after deletion
            return redirect('view_patients')
        except Patient.DoesNotExist:
            error_message = f'Patient with ID {p_id} does not exist.'
            return render(request, 'delete_patient.html', {'error_message': error_message})

    return render(request, 'delete_patient.html')


@login_required
def update_patients(request, p_id):
    patient = get_object_or_404(Patient, p_id=p_id)
    if request.method == 'POST':
        form = PatientUpdateForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            return redirect(
                'view_patients')  # Replace 'success_url' with the URL where you want to redirect after a successful update
    else:
        form = PatientUpdateForm(instance=patient)
    return render(request, 'update_patient_form.html', {'form': form})


@login_required
def create_patients(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Change the redirect URL as needed
    else:
        form = PatientForm()

    return render(request, 'create_patient.html', {'form': form})


@login_required
def create_doctors(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Change the redirect URL as needed
    else:
        form = DoctorForm()

    return render(request, 'create_doctor.html', {'form': form})



@login_required
def view_departments(request):
    departments = Department.objects.all()
    return render(request, 'view_departments.html', {'departments': departments})



@login_required
def create_departments(request):
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Change the redirect URL as needed
    else:
        form = DepartmentForm()

    return render(request, 'create_departments.html', {'form': form})


@login_required
def delete_department(request):
    if request.method == 'POST':
        id = request.POST.get('id', '')  # Access the 'id' value
        try:
            # Get the department using the submitted id
            department = get_object_or_404(Department, id=id)

            # Get additional information if needed
            department_name = department.name  # Example: Get the department's name

            # Delete the department
            department.delete()

            # Redirect to the view departments page after deletion
            return redirect('view_departments')
        except Department.DoesNotExist:
            error_message = f'Department with ID {id} does not exist.'
            return render(request, 'delete_failure.html', {'error_message': error_message})
    else:
        # Handle the case when the request method is not POST
        return render(request, 'delete_department.html')