import sys
from pathlib import Path

def clean_text(text: str) -> str:
    """Remove unnecessary blank lines and collapse text cleanly."""
    lines = text.splitlines()
    cleaned = []

    for line in lines:
        stripped = line.strip()
        if stripped:        # skip empty lines entirely
            cleaned.append(stripped)

    return "\n".join(cleaned)


def clean_file(input_path: str, output_path: str = None):
    """Read a .txt file, clean it, and write the cleaned output."""
    in_path = Path(input_path)

    if not in_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    text = in_path.read_text(encoding="utf-8")
    cleaned = clean_text(text)

    # If no output path, overwrite original file
    if output_path is None:
        out_path = in_path
    else:
        out_path = Path(output_path)

    out_path.write_text(cleaned, encoding="utf-8")
    print(f"Cleaned file written to: {out_path}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_gaps.py <input_file_path> [output_file_path]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None

    clean_file(input_file, output_file)
