import openai


def generate_project_documentation(code_content, api_key):
    """
    Generates a clean and detailed README for the entire project using the OpenAI GPT-4 API.

    Parameters:
    - code_content (str): The combined code content of the project.
    - api_key (str): The API key for OpenAI.

    Returns:
    - str: Generated README text, formatted and ready to be used as a markdown file.
    """
    openai.api_key = api_key

    # Create a detailed and clean prompt for GPT-4
    prompt = (
        "You are an expert technical writer. Generate a detailed, well-structured, and clean README file for the following software project. "
        "Theimport openai


def generate_project_documentation(code_content, api_key):
    """
    Generates a clean and detailed README for the entire project using the OpenAI GPT-4 API.

    Parameters:
    - code_content (str): The combined code content of the project.
    - api_key (str): The API key for OpenAI.

    Returns:
    - str: Generated README text, formatted and ready to be used as a markdown file.
    """
    openai.api_key = api_key

    # Create a detailed and clean prompt for GPT-4
    prompt = (
        "You are an expert technical writer. Generate a detailed, well-structured, and clean README file for the following software project. "
        "The README should be directly usable as a markdown file without additional markdown formatting or unnecessary sections. "
        "The README should include the following sections:\n\n"
        "1. Project Title and Overview: A clear and concise title for the project, followed by an overview that explains what the project does, its purpose, and the problem it aims to solve.\n\n"
        "2. Features: A detailed list and description of all the main features of the project, explaining how each feature benefits the user.\n\n"
        "3. Installation: Step-by-step instructions on how to install the project, including any prerequisites, dependencies, and configurations required. "
        "These instructions should be comprehensive enough for someone with basic knowledge of the technology stack to follow.\n\n"
        "4. Usage: Detailed examples of how to use the project. This section should cover common use cases and any command-line options, configurations, o"
        "5. Code Structure: An explanation of the structure of the codebase, including the purpose of key directories and files. Detail how the main components interact, and provide an overview of the core classes, functions, or modules.\n\n"
        "6. Contribution Guidelines: Guidelines on how others can contribute to the project, such as coding standards, branch management, and testing procedures.\n\n"
        "7. Testing: Instructions on how to run tests, if the project includes any. Explain what the tests cover and how to interpret the results.\n\n"
        "8. License: Specify the licensing terms under which the project is distributed.\n\n"
        "9. Acknowledgments: Include a section for acknowledgments, where contributors, libraries, or resources that significantly helped with the project are credited.\n\n"
        "10. Additional Sections: Add any other sections that you think would be valuable for this specific project, such as FAQs, troubleshooting tips, or a roadmap for future development.\n\n"
        "Here is the relevant code from the project:\n\n"
        f"{code_content}\n\n"
        "Please analyze this code to generate a README that accurately reflects the project's purpose, structure, and functionality."
    )

    try:
        # Call to OpenAI API using ChatCompletion with GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": "You are a highly skilled assistant that generates comprehensive project documentation."},
                {"role": "user", "content": prompt}
            ]
        )

        documentation = response.choices[0].message['content'].strip()
        return documentation
    except openai.error.OpenAIError as e:
        print(f"Error generating documentation: {e}")
        return None
 README should be directly usable as a markdown file without additional markdown formatting or unnecessary sections. "
        "The README should include the following sections:\n\n"
        "1. Project Title and Overview: A clear and concise title for the project, followed by an overview that explains what the project does, its purpose, and the problem it aims to solve.\n\n"
        "2. Features: A detailed list and description of all the main features of the project, explaining how each feature benefits the user.\n\n"
        "3. Installation: Step-by-step instructions on how to install the project, including any prerequisites, dependencies, and configurations required. "
        "These instructions should be comprehensive enough for someone with basic knowledge of the technology stack to follow.\n\n"
        "4. Usage: Detailed examples of how to use the project. This section should cover common use cases and any command-line options, configurations, o"
        "5. Code Structure: An explanation of the structure of the codebase, including the purpose of key directories and files. Detail how the main components interact, and provide an overview of the core classes, functions, or modules.\n\n"
        "6. Contribution Guidelines: Guidelines on how others can contribute to the project, such as coding standards, branch management, and testing procedures.\n\n"
        "7. Testing: Instructions on how to run tests, if the project includes any. Explain what the tests cover and how to interpret the results.\n\n"
        "8. License: Specify the licensing terms under which the project is distributed.\n\n"
        "9. Acknowledgments: Include a section for acknowledgments, where contributors, libraries, or resources that significantly helped with the project are credited.\n\n"
        "10. Additional Sections: Add any other sections that you think would be valuable for this specific project, such as FAQs, troubleshooting tips, or a roadmap for future development.\n\n"
        "Here is the relevant code from the project:\n\n"
        f"{code_content}\n\n"
        "Please analyze this code to generate a README that accurately reflects the project's purpose, structure, and functionality."
    )

    try:
        # Call to OpenAI API using ChatCompletion with GPT-4
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system",
                 "content": "You are a highly skilled assistant that generates comprehensive project documentation."},
                {"role": "user", "content": prompt}
            ]
        )

        documentation = response.choices[0].message['content'].strip()
        return documentation
    except openai.error.OpenAIError as e:
        print(f"Error generating documentation: {e}")
        return None
