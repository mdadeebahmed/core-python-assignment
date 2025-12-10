def search_patients(patients, disease):
  matching_patients = [patients["Name"] for patients in patients if patients["Disease"].lower() == disease.lower()]

  return f'Patients with Flu: {matching_patients}'

patients = [

    {"Name": "Alice", "Age": 30, "Disease": "Flu"},

    {"Name": "Bob", "Age": 45, "Disease": "Diabetes"},

    {"Name": "Charlie", "Age": 35, "Disease": "Flu"}

]

search_disease = "Flu"

print(search_patients(patients, search_disease))