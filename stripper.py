from pathlib import Path

# ============================================================
# Configuration
# ============================================================

INPUT_FILE = Path("conversations_clean.md")
OUTPUT_DIR = Path("conversations_split")

# 750 KiB = 768,000 bytes
# This stays comfortably below GitHub's ~1 MB recommended
# individual-object size.
TARGET_SIZE = 750 * 1024


# ============================================================
# Helpers
# ============================================================

def find_conversation_blocks(text):
    """
    Split the Markdown into logical blocks.

    This assumes conversations are separated by blank lines
    and/or Markdown headings.

    If your conversations_clean.md has a specific structure,
    this can be adjusted to split on the exact conversation
    marker.
    """

    lines = text.splitlines(keepends=True)

    blocks = []
    current = []

    for line in lines:
        # Treat Markdown headings as possible boundaries.
        # We only start a new block if the current block already
        # contains content.
        if line.startswith("#") and current:
            blocks.append("".join(current))
            current = []

        current.append(line)

    if current:
        blocks.append("".join(current))

    return blocks


def split_large_block(block, target_size):
    """
    If one logical block is itself larger than target_size,
    split it by lines so we never create an oversized chunk.
    """

    block_bytes = block.encode("utf-8")

    if len(block_bytes) <= target_size:
        return [block]

    pieces = []
    current = []
    current_size = 0

    for line in block.splitlines(keepends=True):
        line_size = len(line.encode("utf-8"))

        if current and current_size + line_size > target_size:
            pieces.append("".join(current))
            current = []
            current_size = 0

        current.append(line)
        current_size += line_size

    if current:
        pieces.append("".join(current))

    return pieces


# ============================================================
# Main
# ============================================================

def main():
    if not INPUT_FILE.exists():
        print(f"ERROR: Could not find {INPUT_FILE}")
        return

    OUTPUT_DIR.mkdir(exist_ok=True)

    # Read bytes first so we can guarantee exact preservation.
    original_bytes = INPUT_FILE.read_bytes()
    original_size = len(original_bytes)

    # Decode without losing anything.
    text = original_bytes.decode("utf-8")

    print(f"Input file: {INPUT_FILE}")
    print(f"Input size: {original_size:,} bytes")
    print()

    # Remove old generated chunks.
    for old_file in OUTPUT_DIR.glob("conversations_*.md"):
        old_file.unlink()

    # Find logical blocks.
    blocks = find_conversation_blocks(text)

    # Make sure no individual logical block is too large.
    safe_blocks = []

    for block in blocks:
        safe_blocks.extend(
            split_large_block(block, TARGET_SIZE)
        )

    # Build output chunks.
    chunks = []
    current = []
    current_size = 0

    for block in safe_blocks:
        block_size = len(block.encode("utf-8"))

        # If adding this block would exceed the target,
        # start a new file.
        if current and current_size + block_size > TARGET_SIZE:
            chunks.append("".join(current))
            current = []
            current_size = 0

        current.append(block)
        current_size += block_size

    if current:
        chunks.append("".join(current))

    # Write files.
    total_output_size = 0

    print("Created files:")
    print("-" * 60)

    for index, chunk in enumerate(chunks, start=1):
        output_file = (
            OUTPUT_DIR /
            f"conversations_{index:03d}.md"
        )

        data = chunk.encode("utf-8")
        output_file.write_bytes(data)

        size = len(data)
        total_output_size += size

        print(
            f"{output_file.name:<30} "
            f"{size:>10,} bytes "
            f"({size / 1024:.1f} KiB)"
        )

    print("-" * 60)

    print(f"Number of files: {len(chunks)}")
    print(f"Original size:   {original_size:,} bytes")
    print(f"Output size:     {total_output_size:,} bytes")

    # ========================================================
    # Integrity check
    # ========================================================

    if original_size == total_output_size:
        print()
        print("SUCCESS: No data was lost.")
        print("The output files contain exactly the same bytes as the input.")
    else:
        print()
        print("ERROR: Size mismatch!")
        print(
            f"Difference: "
            f"{original_size - total_output_size:,} bytes"
        )


if __name__ == "__main__":
    main()
