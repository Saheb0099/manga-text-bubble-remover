import os
import time
from pathlib import Path
from bubble_tool.bubble_tool import remove_bubble

# ================= CONFIGURATION =================
INPUT_ROOT_FOLDER = "input_manga"
OUTPUT_ROOT_FOLDER = "temp_stage1"  # Temporary holding area

MODEL_TYPE = 0             # 0 = Focus on white shapes/boxes
DETECTION_THRESHOLD = 0.05 # Aggressive low threshold to catch hidden boxes
# =================================================

def main():
    base_dir = Path(__file__).parent
    input_dir = base_dir / INPUT_ROOT_FOLDER
    output_dir = base_dir / OUTPUT_ROOT_FOLDER

    if not input_dir.exists():
        print(f"❌ Error: Input folder '{INPUT_ROOT_FOLDER}' not found!")
        return

    chapter_folders = [f for f in input_dir.iterdir() if f.is_dir()]
    chapter_folders.sort()

    print(f"🏗️  STEP 1: BUBBLE REMOVAL (Model {MODEL_TYPE})")
    print(f"📂 Processing {len(chapter_folders)} chapters...")
    print("-" * 40)

    for i, chapter in enumerate(chapter_folders):
        chapter_name = chapter.name
        print(f"🚀 [{i+1}/{len(chapter_folders)}] Processing: {chapter_name}")

        # Output to: temp_stage1 / Chapter 1
        chapter_out_dir = output_dir / chapter_name
        mask_out_path = chapter_out_dir / "mask"
        clean_out_path = chapter_out_dir / "cleaned"
        
        mask_out_path.mkdir(parents=True, exist_ok=True)
        clean_out_path.mkdir(parents=True, exist_ok=True)

        try:
            remove_bubble(
                src_path=chapter,
                mask_output_path=mask_out_path,
                clean_img_output_path=clean_out_path, # Result goes here
                model_type=MODEL_TYPE,
                detection_th=DETECTION_THRESHOLD
            )
        except Exception as e:
            print(f"❌ Error on {chapter_name}: {e}")

    print("\n✅ STEP 1 COMPLETE. Results are in 'temp_stage1'.")
    print("👉 Now run 'step2_text.py'")

if __name__ == "__main__":
    main()