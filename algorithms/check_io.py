import argparse
import re
import subprocess
import sys


def extract_expected_io(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    expected_input_lines = []
    expected_output_lines = []
    input_mode = False
    output_mode = False
    
    for line in lines:
        if re.match(r'\s*#\s*EXPECTED INPUT:', line):
            input_mode = True
            output_mode = False
            # Process content on the same line after the label, if any.
            content = re.sub(r'\s*#\s*EXPECTED INPUT:\s*', '', line).rstrip()
            if content:
                expected_input_lines.append(content)
            continue
        if re.match(r'\s*#\s*EXPECTED OUTPUT:', line):
            output_mode = True
            input_mode = False
            content = re.sub(r'\s*#\s*EXPECTED OUTPUT:\s*', '', line).rstrip()
            if content:
                expected_output_lines.append(content)
            continue
        
        # When in input or output mode, process only lines starting with '#'
        if input_mode and re.match(r'\s*#', line):
            # Lines following the EXPECTED INPUT label
            content = re.sub(r'\s*#\s?', '', line).rstrip()
            expected_input_lines.append(content)
        elif output_mode and re.match(r'\s*#', line):
            content = re.sub(r'\s*#\s?', '', line).rstrip()
            expected_output_lines.append(content)
        # Exit mode if a non-comment line is encountered
        elif input_mode or output_mode:
            input_mode = False
            output_mode = False

    expected_input = "\n".join(expected_input_lines).strip()
    expected_output = "\n".join(expected_output_lines).strip()
    
    if not expected_input or not expected_output:
        raise ValueError("Could not properly extract EXPECTED INPUT or EXPECTED OUTPUT comments.")
    
    return expected_input, expected_output

def run_code(file_path, input_data):
    try:
        result = subprocess.run(
            [sys.executable, file_path],
            input=input_data.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10
        )
    except subprocess.TimeoutExpired:
        raise TimeoutError("Execution timed out.")
    
    if result.returncode != 0:
        raise RuntimeError(f"Error during code execution:\n{result.stderr.decode('utf-8')}")
    
    return result.stdout.decode('utf-8').strip()

def main():
    parser = argparse.ArgumentParser(description="Compare the actual I/O of a Python script with the expected I/O specified in comments.")
    parser.add_argument("file_path", help="Path to the Python file to test")
    args = parser.parse_args()
    
    try:
        expected_input, expected_output = extract_expected_io(args.file_path)
    except Exception as e:
        print("Failed to extract expected I/O:", e)
        sys.exit(1)
    
    print("Extracted EXPECTED INPUT:")
    print(expected_input)
    print("\nExtracted EXPECTED OUTPUT:")
    print(expected_output)
    
    try:
        actual_output = run_code(args.file_path, expected_input)
    except Exception as e:
        print("Code execution failed:", e)
        sys.exit(1)
    
    print("\nActual output:")
    print(actual_output)
    
    if actual_output == expected_output:
        print("\nTest Passed: Actual output matches expected output.")
    else:
        print("\nTest Failed: Actual output does not match expected output.")

if __name__ == "__main__":
    main()
