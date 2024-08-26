import os

# Map of file extensions to programming languages
LANGUAGE_MAP = {
    '.py': 'Python',
    '.java': 'Java',
    '.js': 'JavaScript',
    '.cpp': 'C++',
    '.cs': 'C#',
    # Add more languages as needed
}

def parse_code(directory):
    code_content = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            _, ext = os.path.splitext(file)
            language = LANGUAGE_MAP.get(ext)
            if language:
                with open(file_path, 'r') as f:
                    code_content.append(f"\n# {file_path}\n\n{f.read()}")
            # Ignore files that are not in LANGUAGE_MAP
    return "\n".join(code_content)