"""
One-time setup: generate 20 branded background images using Gemini AI.
Uses your existing GEMINI_API_KEY — no extra cost on AI Studio free tier.
Run: python3 setup_assets.py YOUR_GEMINI_API_KEY
Images saved to assets/images/ — commit them to the repo.
"""

import io
import sys
import time
from pathlib import Path

from PIL import Image

OUTPUT_DIR = Path("assets/images")
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

PROMPTS = [
    "dramatic Scottish highlands landscape at dusk, deep navy and purple tones, no people, cinematic wide shot",
    "rugged Atlantic coastline with crashing waves, dark stormy sky, moody atmosphere, no people",
    "ancient stone cottage surrounded by rolling green hills, golden evening light, no people",
    "misty mountain loch reflection at dawn, silver and navy tones, no people, peaceful",
    "dense ancient oak woodland with dappled sunlight, deep green tones, no people",
    "remote Scottish island aerial view, turquoise water, dramatic clouds, no people",
    "windswept moorland at sunrise, warm orange and navy sky, heather, no people",
    "traditional boutique hotel exterior at twilight, warm glowing windows, no people",
    "narrow cobblestone village street in evening light, golden hour, no people",
    "wild highland river gorge with waterfalls, lush green, dramatic, no people",
    "coastal fishing harbour at dawn with mist, dark moody tones, boats, no people",
    "rolling vineyard hills at sunset, warm amber light, no people, cinematic",
    "remote lighthouse on rocky headland, stormy grey sea, dramatic sky",
    "ancient bluebell woodland, dappled spring light, deep green, no people",
    "mountain pass with dramatic cloud shadows, navy tones, vast landscape, no people",
    "traditional stone farmhouse in winter landscape, frost, muted grey tones, no people",
    "wild meadow with mixed wildflowers, golden hour light, soft bokeh, no people",
    "dramatic sea stack rock formations rising from navy ocean, cinematic, no people",
    "lakeside pine forest at dawn, mist rising from water, deep blue and green tones",
    "historic castle ruins on hilltop at sunset, dramatic clouds, orange sky, no people",
]


def generate_image(prompt: str, filename: str, api_key: str) -> bool:
    try:
        from google import genai
        from google.genai import types

        print(f"  Generating: {filename}...")
        client = genai.Client(api_key=api_key)

        response = client.models.generate_content(
            model="gemini-2.0-flash-exp-image-generation",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["IMAGE"],
            ),
        )

        for part in response.candidates[0].content.parts:
            if part.inline_data:
                img = Image.open(io.BytesIO(part.inline_data.data)).convert("RGB")
                img = img.resize((1920, 1080))
                out_path = OUTPUT_DIR / filename
                img.save(str(out_path), "JPEG", quality=90)
                print(f"  Saved: {out_path} ({out_path.stat().st_size // 1024} KB)")
                return True

        print(f"  No image returned for: {filename}")
        return False

    except Exception as e:
        print(f"  FAILED {filename}: {e}")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 setup_assets.py YOUR_GEMINI_API_KEY")
        print("Get your key at: aistudio.google.com")
        sys.exit(1)

    api_key = sys.argv[1]

    # Install google-genai if needed
    try:
        from google import genai
    except ImportError:
        import subprocess
        print("Installing google-genai...")
        subprocess.run([sys.executable, "-m", "pip", "install", "google-genai", "-q"], check=True)

    print(f"Generating {len(PROMPTS)} background images with Gemini AI...")
    print(f"Output: {OUTPUT_DIR.resolve()}\n")

    success = 0
    for i, prompt in enumerate(PROMPTS):
        filename = f"bg_{i+1:02d}.jpg"
        if (OUTPUT_DIR / filename).exists():
            print(f"  Skipping {filename} (already exists)")
            success += 1
            continue
        ok = generate_image(prompt, filename, api_key)
        if ok:
            success += 1
        time.sleep(1)

    print(f"\nDone: {success}/{len(PROMPTS)} images saved to {OUTPUT_DIR}")
    print("\nNext steps:")
    print("  git add assets/images/")
    print("  git commit -m 'add: Gemini AI background images'")
    print(f"  git push https://nigel-sketch:YOUR_TOKEN@github.com/nigel-sketch/Youtube-Automation-.git main")


if __name__ == "__main__":
    main()
