# ClinRx-ICU-CCU Nutrition Support Engine

def nutrition_assessment(patient):

    recommendations = []

    if patient.get("nutrition_route") == "enteral":
        recommendations.append({
            "area": "Enteral Nutrition",
            "action": "Monitor feeding tolerance and medication compatibility"
        })

    if patient.get("nutrition_route") == "parenteral":
        recommendations.append({
            "area": "Parenteral Nutrition",
            "action": "Monitor glucose, electrolytes, triglycerides and liver function"
        })

    if patient.get("propofol_infusion"):
        recommendations.append({
            "issue": "Propofol lipid contribution",
            "action": "Consider total lipid/calorie assessment"
        })

    return recommendations
