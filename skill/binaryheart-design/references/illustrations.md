# Illustrations

The BinaryHeart illustration library is isometric line art with 2px dark outlines (`#26303F`), flat fills, and the brand navy and red.
The 01-heart logo appears on screens, stickers, and labels, drawn on illustration cream `#FDF6EA`.
Every PNG has a transparent background.

## How to use them

- Use one hero illustration per piece, plus small icons for list rows.
    - Don't collage many scenes together.
- Place them on cream, white, or a navy tile.
    - Dark-bodied devices (towers, terminals) read best on a navy tile with 12-14px padding.
- Never recolor them, add drop shadows, or crop through the device.
- In email, use the `curated/` PNGs, hosted at public URLs.
    - For print, embed the PNG (or SVG from `full/`) as base64.
- Need a different size? Run `python3 scripts/prepare_illustration.py SRC OUT --max 640`.
- If nothing fits, draw a new one in the same style: isometric at 30 degrees, 2px `#26303F` outlines, flat navy, red, gray, and cream fills, with a small 01-heart sticker.
    - Otherwise, ask the user for more from the source set.

## Curated set (`assets/illustrations/curated/`, trimmed PNGs)

| File | Max px | Shows | Good for |
|---|---|---|---|
| `laptop-teardown.png` | 800 | Open laptop mid-repair, tools and screws laid out | Recruitment hero, "hands-on repair" |
| `knolling-parts.png` | 800 | Parts neatly laid out on a blue mat | Announcement or workshop hero |
| `open-test-bench.png` | 800 | Open-air PC test bench with cables and GPU | Hardware or tech-heavy pieces |
| `gpu-service.png` | 800 | Graphics card being cleaned and repasted | Advanced repair, tech recruiting |
| `phone-teardown.png` | 800 | Phone opened with suction cup and picks | Phone repair drives |
| `refurb-bundle.png` | 800 | Refurbished computer set ready to donate | Donation drives, impact stories |
| `triple-monitor.png` | 800 | Three-monitor coding setup | Software team, OpenClaw cluster |
| `video-call-corner.png` | 800 | Desk setup mid video call | Remote help, community outreach |
| `laptop.png` | 480 | Open laptop with the heart logo on screen | General-purpose icon, availability or sign-up sections |
| `retro-computer.png` | 480 | Beige retro computer with a terminal | History, "since 2016", terminal direction |
| `tower-pc.png` | 480 | Navy tower PC with a side window | Hardware |
| `smartphone.png` | 480 | Phone showing the BinaryHeart app | Social, sign-up, Discord |
| `floppy-stack.png` | 480 | Stack of floppy disks with a heart label | Fun accents, data security |
| `donation-box.png` | 480 | Open box holding a donated device | Operations, donations |
| `tower-open-repair.png` | 480 | Open tower being repaired on a mat | Hardware card in "What we do" |
| `green-terminal.png` | 480 | Monitor showing a green terminal | Software card in "What we do" |
| `laptop-refurb-progress.png` | 480 | Laptop showing a refurbishment progress bar | Status and progress updates |
| `phone-cracked-repair.png` | 480 | Cracked phone mid-repair | Repair drives |
| `precision-kit.png` | 480 | Precision screwdriver kit | "What to expect" and "what to bring" |
| `toolbox.png` | 480 | Toolbox | Training, workshops |
| `parts-box.png` | 480 | Box of spare parts | Inventory, operations |
| `tablet-videocall.png` | 480 | Tablet in a folio case on a video call | Device recipients, education |

## Full library (`assets/illustrations/full/`, which is `illustrations/source/` in the repo)

This folder may be missing in the lightweight build.
Each category has `png/` (2000×2000 transparent, where available), `svg/`, and `previews/` contact sheets (open these first to browse).

### core-devices

- `svg/01-laptop.svg`
- `svg/02-retro-computer.svg`
- `svg/03-tower-pc.svg`
- `svg/04-smartphone.svg`
- `svg/05-floppy-stack.svg`
- `svg/06-donation-box.svg`
- Preview sheets: `previews/preview-sheet.png`

### devices-and-tools

- `svg/laptops/laptop-01-navy-code.svg`
- `svg/laptops/laptop-02-closed-stickers.svg`
- `svg/laptops/laptop-03-dashboard.svg`
- `svg/laptops/laptop-04-retro-trackball.svg`
- `svg/laptops/laptop-05-refurb-progress.svg`
- `svg/misc/cd-stack.svg`
- `svg/misc/parts-box.svg`
- `svg/misc/tool-01-screwdriver.svg`
- `svg/misc/tool-02-soldering-station.svg`
- `svg/misc/tool-03-precision-kit.svg`
- `svg/misc/tool-04-multimeter.svg`
- `svg/misc/tool-05-toolbox.svg`
- `svg/monitors/setup-01-home-office.svg`
- `svg/monitors/setup-02-dual-monitor.svg`
- `svg/monitors/setup-03-green-terminal.svg`
- `svg/monitors/setup-04-all-in-one.svg`
- `svg/monitors/setup-05-docked-laptop.svg`
- `svg/phones/phone-01-upright-lockscreen.svg`
- `svg/phones/phone-02-back-camera.svg`
- `svg/phones/phone-03-flip-phone.svg`
- `svg/phones/phone-04-cracked-repair.svg`
- `svg/phones/phone-05-charging-dock.svg`
- `svg/tablets/tablet-01-folio-videocall.svg`
- `svg/tablets/tablet-02-drawing-stylus.svg`
- `svg/tablets/tablet-03-keyboard-cover.svg`
- `svg/tablets/tablet-04-rugged-kids.svg`
- `svg/tablets/tablet-05-ereader-stand.svg`
- `svg/towers/tower-01-beige-90s.svg`
- `svg/towers/tower-02-cream-mesh.svg`
- `svg/towers/tower-03-open-repair.svg`
- `svg/towers/tower-04-red-cube.svg`
- `svg/towers/tower-05-olive-triple-fan.svg`
- Preview sheets: `previews/all-32.png`, `previews/laptops.png`, `previews/misc.png`, `previews/monitors.png`, `previews/phones.png`, `previews/tablets.png`, `previews/towers.png`

### gadgets-and-peripherals

- `svg/01-smartwatch.svg`
- `svg/02-earbuds.svg`
- `svg/03-headphones.svg`
- `svg/04-controller.svg`
- `svg/05-handheld.svg`
- `svg/06-router.svg`
- `svg/07-ssd.svg`
- `svg/08-usb.svg`
- `svg/09-keyboard.svg`
- `svg/10-mouse.svg`
- `svg/11-webcam.svg`
- `svg/12-speaker.svg`
- `svg/13-printer.svg`
- `svg/14-vr.svg`
- `svg/15-camera.svg`
- `svg/16-gpu.svg`
- `svg/17-ram.svg`
- `svg/18-cpu.svg`
- `svg/19-monitor.svg`
- `svg/20-nas.svg`
- `svg/21-powerbank.svg`
- `svg/22-hdd.svg`
- `svg/23-console.svg`
- `svg/24-projector.svg`
- `svg/25-phone.svg`
- Preview sheets: `previews/binaryheart-devices-preview.png`

### repair-and-setup-scenes

- `svg/repair-and-parts/repair-01-open-test-bench.svg`
- `svg/repair-and-parts/repair-02-laptop-teardown.svg`
- `svg/repair-and-parts/repair-03-board-on-antistatic-bag.svg`
- `svg/repair-and-parts/repair-04-drives-and-adapter.svg`
- `svg/repair-and-parts/repair-05-phone-teardown.svg`
- `svg/repair-and-parts/repair-06-case-full-cabling.svg`
- `svg/repair-and-parts/repair-07-keyboard-switches.svg`
- `svg/repair-and-parts/repair-08-knolling-parts.svg`
- `svg/repair-and-parts/repair-09-retro-computer-open.svg`
- `svg/repair-and-parts/repair-10-gpu-service.svg`
- `svg/setups-no-desk/setup-06-ultrawide-gaming.svg`
- `svg/setups-no-desk/setup-07-monitor-arm-laptop.svg`
- `svg/setups-no-desk/setup-08-compact-retro.svg`
- `svg/setups-no-desk/setup-09-triple-monitor.svg`
- `svg/setups-no-desk/setup-10-glass-tower-rig.svg`
- `svg/setups-no-desk/setup-11-video-call-corner.svg`
- `svg/setups-no-desk/setup-12-laptop-on-books.svg`
- `svg/setups-no-desk/setup-13-refurb-bundle.svg`
- `svg/setups-no-desk/setup-14-eighties-amber.svg`
- `svg/setups-no-desk/setup-15-navy-all-in-one.svg`
- Preview sheets: `previews/repair-and-parts.png`, `previews/setups-no-desk.png`

