import csv
import os
from typing import Literal, List, Optional
from pydantic import BaseModel, Field

from pydantic import BaseModel, Field
from typing import List, Literal, Optional


class SurveyResponse(BaseModel):
    """
    Schema for a single synthetic survey response.
    Each field exactly mirrors the Google Form question text and options.
    """

    # 1. Primary role
    primary_role: Literal[
        "Undergraduate Student",
        "Graduate Student / Researcher",
        "Software Developer / Engineer",
        "Data Scientist / AI/ML Engineer",
        "Industry Professional",
        "University Faculty Member",
        "other"
    ] = Field(
        ...,
        description="Primary role."
    )
    primary_role_other: Optional[str] = Field(None, description="If 'other' selected, mention the role.")

    # 2. Years of experience with Python
    years_of_experience_with_python: Literal[
        "Less than 1 year",
        "1–3 years",
        "3–5 years",
        "5–10 years",
        "More than 10 years"
    ] = Field(
        ...,
        description="Years of experience with Python."
    )

    # 3. Domains of Python usage
    domains_of_python_usage: List[Literal[
        "Data Science / Machine Learning",
        "Web Development",
        "Systems / DevOps / Scripting",
        "Research / Academia",
        "Education / Teaching",
        "other"
    ]] = Field(
        ...,
        description="In which domains do you mainly use Python?"
    )


    # 4. Awareness of environmental impact
    awareness_of_environmental_impact: Literal["Yes", "No"] = Field(
        ...,
        description="Before this survey, were you aware of the environmental impact of software (e.g., energy use, carbon emissions)?"
    )

    # 5. Importance of sustainability in development
    importance_of_sustainability_in_development: Literal[
        "Not important",
        "Slightly important",
        "Moderately important",
        "Very important",
        "Extremely important"
    ] = Field(
        ...,
        description="How important do you think it is to consider sustainability when developing software?"
    )

    # 6. Importance of energy efficiency
    importance_of_energy_efficiency_in_runtime_choice: Literal[
        "Neutral",
        "Not important",
        "Somewhat important",
        "Very important"
    ] = Field(
        ...,
        description="How important do you think energy efficiency / carbon footprint should be when choosing a runtime?"
    )

    # 7. Conscious language/library choice for sustainability
    conscious_language_choice_for_sustainability: Literal["Yes", "No", "Not sure"] = Field(
        ...,
        description="Have you ever consciously chosen a programming language, library, or execution model for sustainability reasons?"
    )

    # 8. Python execution models used
    python_execution_models_used: List[Literal[
        "CPython (default Python interpreter)",
        "PyPy (JIT Solution)",
        "Cython (AOT Solution)",
        "ctypes (FFI Solution)",
        "py_compile (Byte Compilation Solution)",
        "other"
    ]] = Field(
        ...,
        description="Which of the following Python execution models have you used? available choices are: (Select all that apply)"
    )

    # 9. Most practical runtime
    most_practical_runtime_for_sustainability: Literal[
        "CPython",
        "PyPy",
        "Cython",
        "ctypes",
        "Not sure"
    ] = Field(
        ...,
        description="In your professional opinion, which runtime is most practical for sustainable large-scale use?"
    )

    # 10. Opinion on integrating C code
    opinion_on_integrating_c_code_for_sustainability: Literal["Yes", "No", "Maybe"] = Field(
        ...,
        description="Do you agree that integrating C code with Python (e.g., via Foreign Function Interfaces like ctypes) provides the most sustainable solution among Python execution methods, by balancing energy efficiency, runtime performance, and ease of development?"
    )

    # 11. Relevance of GreenScore
    relevance_of_greenscore_metric: Literal[
        "Not relevant",
        "Slightly relevant",
        "Moderately relevant",
        "Very relevant"
    ] = Field(
        ...,
        description="Based on your understanding, how relevant do you find GreenScore for evaluating software sustainability?"
    )

    # 12. Combined sustainability score opinion
    opinion_on_combined_sustainability_score: Literal[
        "Strongly disagree",
        "Disagree",
        "Neutral",
        "Agree",
        "Strongly agree"
    ] = Field(
        ...,
        description="Do you think combining energy, carbon, and runtime into one score is effective?"
    )

    # 13. Key sustainability factors
    key_sustainability_factors: List[Literal[
        "Energy consumption",
        "Carbon footprint",
        "Runtime / performance impact",
        "Memory usage",
        "I/O and network activity",
        "Thermal output / cooling requirements",
        "Cost implications"
    ]] = Field(
        ...,
        min_length=1,
        max_length=3,
        description="What factors do you think should be considered in software sustainability metrics? (Select up to 3)"
    )

    # 14. Likelihood of GreenScore influence
    likelihood_greenscore_influences_choices: Literal[
        "Not likely",
        "Slightly likely",
        "Moderately likely",
        "Very likely",
        "Extremely likely"
    ] = Field(
        ...,
        description="How likely is it that a metric like GreenScore would influence your software development choices?"
    )

    # 15. Belief in GreenScore runtime contribution
    opinion_on_best_greenscore_runtime_contributes: Literal["Yes", "No", "Maybe"] = Field(
        ...,
        description="Do you think choosing a Python execution method with the best GreenScore contributes to creating sustainable software?"
    )

    # 16. Suggestions for GreenScore improvements
    suggestions_for_greenscore_improvements: Optional[str] = Field(
        None,
        description="What improvements or additions would you suggest for GreenScore?"
    )

    # 17. Interest in automatic GreenScore feedback tool
    interest_in_greenscore_tool: Literal["Yes", "No", "Maybe"] = Field(
        ...,
        description="Would you be interested in a tool that automatically provides GreenScore feedback for your Python code?"
    )

    # 18. Additional comments
    additional_comments_on_sustainable_software_development: Optional[str] = Field(
        None,
        description="Please share any additional comments or suggestions about sustainable software development."
    )


# The full survey prompt provided by the user
SURVEY_PROMPT = """
You are an experienced software professional with several years of industry experience in one or more domains such as backend development, data science, embedded systems, DevOps, or software engineering.
You are proficient in Python and also have working knowledge of other programming languages such as C and C++.
In addition, you are knowledgeable about green computing principles, energy-efficient software practices, and sustainable Python development.

You are participating in a professional survey about software sustainability, environmental impact, and Python runtime performance and optimization methods.
Please answer the survey questions realistically and professionally, drawing on your background, domain expertise, and experience with large-scale and performance-sensitive software systems.

Your answers should reflect authentic, diverse professional opinions and reasoning, representing perspectives from
"""

def save_to_csv(response_dict: dict, filename: str):
    """
    Appends a single dictionary response to a CSV file.
    If the file does not exist, it creates it and writes headers first.
    Always appends new data to the last row (never overwrites).
    """
    fieldnames = list(response_dict.keys())
    file_exists = os.path.exists(filename)

    # Ensure directory exists (in case filename includes a path)
    os.makedirs(os.path.dirname(filename), exist_ok=True) if os.path.dirname(filename) else None

    # Open in append mode and create if not exists
    with open(filename, mode='a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Write header if the file is new or empty
        if not file_exists or os.stat(filename).st_size == 0:
            writer.writeheader()

        # Write the new data row
        writer.writerow(response_dict)

    print(f"\n✅ Successfully appended a new response to {filename}.")
    print("-" * 50)
    print("Generated Data Snippet:")
    for key, value in response_dict.items():
        preview = str(value)
        print(f"  {key}: {preview[:100]}{'...' if len(preview) > 100 else ''}")
    print("-" * 50)