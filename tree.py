"""
tree.py - Perfect Windows directory tree to clipboard
No SyntaxWarnings • Uses backslashes • Copies instantly
"""

import sys
from pathlib import Path
import pyperclip

def generate_tree(root: Path) -> str:
    lines = []

    # Root line with Windows backslash at the end
    lines.append(f"{root}\\")
    
    try:
        entries = sorted(root.iterdir(), key=lambda p: (p.is_file(), p.name.lower()))
    except PermissionError:
        lines.append("[Permission Denied]")
        return "\n".join(lines)

    # Directories first, then files
    dirs  = [e for e in entries if e.is_dir()]
    files = [e for e in entries if e.is_file()]
    all_entries = dirs + files

    for i, entry in enumerate(all_entries):
        is_last = (i == len(all_entries) - 1)
        connector = "└── " if is_last else "├── "
        branch = "    " if is_last else "│   "

        if entry.is_dir():
            lines.append(f"{connector}{entry.name}\\")
            # Get subtree
            sub_lines = generate_tree(entry).splitlines()[1:]  # skip its own root line
            for sub in sub_lines:
                if sub.strip():
                    lines.append(branch + sub)
        else:
            lines.append(f"{connector}{entry.name}")

    return "\n".join(lines)

def main():
    if len(sys.argv) != 2:
        print(r'Usage: python tree.py "C:\Your\Folder\Path"')
        sys.exit(1)

    folder_path = Path(sys.argv[1])

    if not folder_path.exists():
        print(f"Error: Folder not found → {folder_path}")
        sys.exit(1)

    tree_text = generate_tree(folder_path)

    pyperclip.copy(tree_text)
    print(tree_text)
    print("\nTree copied to clipboard — paste with Ctrl+V!")

if __name__ == "__main__":
    main()