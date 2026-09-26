# Illustrations

The illustrations are isometric line art with 2px `#26303F` outlines, flat navy, red, gray, and cream fills, and the 01-heart on devices.

- `source/<category>/` holds the full library: `svg/`, `png/` (2000×2000, transparent), and `previews/` contact sheets.
    - The categories are core-devices, devices-and-tools, gadgets-and-peripherals, and repair-and-setup-scenes.
- `curated/` holds 22 trimmed PNGs, ready for email and web.
    - Rebuild them with `python3 tools/prepare_illustration.py --curated illustrations/curated`.

The full index, with what each image shows and what it's good for, is in [`../skill/binaryheart-design/references/illustrations.md`](../skill/binaryheart-design/references/illustrations.md).
