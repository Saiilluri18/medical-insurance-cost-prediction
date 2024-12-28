# Let's inspect the uploaded notebook to extract relevant components like model loading, features, and prediction logic.
import nbformat

# Load the notebook
notebook_path = '/mnt/data/Medical Insurance Cost Prediction Model.ipynb'
with open(notebook_path, 'r', encoding='utf-8') as f:
    notebook_data = nbformat.read(f, as_version=4)

# Extract all code cells
code_cells = [cell for cell in notebook_data['cells'] if cell['cell_type'] == 'code']

# Combine code from all cells to analyze
notebook_code = "\n".join(cell['source'] for cell in code_cells)
notebook_code[:1000]  # Show the first 1000 characters of the notebook content for review.
