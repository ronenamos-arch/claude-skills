# Images

## Models and cost (verify on the day - list models first)
```bash
python -c "import json,urllib.request,os;k=os.environ['GOOGLE_API_KEY'];print([m['name'] for m in json.load(urllib.request.urlopen('https://generativelanguage.googleapis.com/v1beta/models?pageSize=200&key='+k))['models'] if 'image' in m['name']])"
```
| Use | Model | Price seen 2026-10 (verify) |
|---|---|---|
| Generate | `gemini-3.1-flash-lite-image` | ~$0.034 / image |
| Edit (targeted fix) | `gemini-3.1-flash-image` | ~$0.045-0.067 / image |
| Fallback | `gemini-2.5-flash-image` | ~$0.039 |

The lite model **ignores edit instructions** - always edit with flash-image. A 48-minute lesson: 47 images +
9 regenerations + 8 edits ≈ $2.5. The key comes from `GOOGLE_API_KEY`, or a `.env` file in the working folder (or the file named by `GOOGLE_ENV_FILE`).

## Prompts
`scenes.py` holds the subject only; `gen_images.py` appends the art style (flat 2D storybook, deep green +
night blue + golden light, scene fills the frame edge to edge) and the era block (MODERN / HISTORIC / ANCIENT; neutral people and period blocks).
Do not ask for "the subject in the right two thirds" - the model leaves blank strips.

## What the cheap model gets wrong (check every image)
Make 2x2 contact sheets at 960x540 per tile, then **crop** every small and background figure:
- Faces or heads covered, cropped or distorted, especially small background figures.
- Extra fingers, merged people, a child with an adult face.
- Logos, flags, uniforms or recognizable real people.
- Stray printed numbers or gibberish Hebrew letters on banners.
- Modern items (phones, cars, glasses) in historic or ancient scenes.

## Fixing
- Composition fine, one detail wrong → `edits.py` + `IMG_MODEL=gemini-3.1-flash-image python edit_images.py name`.
  Say what the detail must **become**: "the small blue cap must become her own brown hair" works;
  "remove the hat" produced a bald figure. `{ATTIRE}` expands to the standard neutral-clothing wording.
- The backup is `build/img_old/<name>_v1.png` and edits always start from it. After regenerating an image,
  rename the old `_v1` first or the edit will be applied to the old picture.
- Many figures wrong, or a structural problem (blank strip) → move the file to `img_old/` and
  regenerate with a sharper prompt ("plain undecorated walls", "exactly three people", "no logos").
