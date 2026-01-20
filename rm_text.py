import os
import time
from pathlib import Path
from bubble_tool.bubble_tool import remove_bubble

# ================= CONFIGURATION =================
INPUT_ROOT_FOLDER = "temp_stage1"  # Reads from Step 1's output
OUTPUT_ROOT_FOLDER = "output_manga" # Final Destination

MODEL_TYPE = 1             # 1 = Focus on floating text
DETECTION_THRESHOLD = 0.2  # Standard threshold is usually fine for text
# =================================================

def main():
    base_dir = Path(__file__).parent
    input_dir = base_dir / INPUT_ROOT_FOLDER
    output_dir = base_dir / OUTPUT_ROOT_FOLDER

    if not input_dir.exists():
        print(f"❌ Error: Folder '{INPUT_ROOT_FOLDER}' not found!")
        print("👉 Did you run 'step1_bubbles.py' first?")
        return

    # Find chapters in temp_stage1
    chapter_folders = [f for f in input_dir.iterdir() if f.is_dir()]
    chapter_folders.sort()

    print(f"🎨 STEP 2: TEXT CLEANUP (Model {MODEL_TYPE})")
    print(f"📂 Found {len(chapter_folders)} chapters from Step 1...")
    print("-" * 40)

    for i, chapter in enumerate(chapter_folders):
        chapter_name = chapter.name
        
        # CRITICAL: The images we want are inside "temp_stage1/Chapter X/cleaned"
        # We must point the tool to THAT folder, not the chapter root.
        source_images_path = chapter / "cleaned"
        
        if not source_images_path.exists():
            print(f"⚠️ Skipping {chapter_name} (No 'cleaned' folder found from Step 1)")
            continue

        print(f"🧹 [{i+1}/{len(chapter_folders)}] Polishing: {chapter_name}")

        # Output to: output_manga / Chapter 1
        chapter_out_dir = output_dir / chapter_name
        mask_out_path = chapter_out_dir / "mask"
        clean_out_path = chapter_out_dir / "cleaned"
        
        mask_out_path.mkdir(parents=True, exist_ok=True)
        clean_out_path.mkdir(parents=True, exist_ok=True)

        try:
            remove_bubble(
                src_path=source_images_path, # <-- Reading from Step 1 cleaned
                mask_output_path=mask_out_path,
                clean_img_output_path=clean_out_path,
                model_type=MODEL_TYPE,
                detection_th=DETECTION_THRESHOLD
            )
        except Exception as e:
            print(f"❌ Error on {chapter_name}: {e}")

    print("\n🎉 PIPELINE COMPLETE!")
    print(f"👉 Final Cleaned Images: {OUTPUT_ROOT_FOLDER}/[Chapter]/cleaned")

if __name__ == "__main__":
    main()