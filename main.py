import subprocess
import sys
import time

def run_script(script_name):
    """Runs a separate python script and waits for it to finish."""
    print(f"\n" + "="*50)
    print(f"🎬 STARTING SCRIPT: {script_name}")
    print("="*50 + "\n")
    
    try:
        # sys.executable ensures we use the exact same 'venv' python we are using now
        subprocess.run([sys.executable, script_name], check=True)
        print(f"\n✅ SUCCESS: {script_name} finished correctly.")
        
    except subprocess.CalledProcessError:
        print(f"\n❌ ERROR: {script_name} crashed or failed.")
        print("🛑 Stopping the pipeline here. Fix the error and try again.")
        sys.exit(1) # Stop everything if step 1 fails

def main():
    total_start = time.time()
    
    # 1. Run The Heavy Lifter (Removes Boxes/Bubbles)
    run_script("rm_speech_bubbles.py")
    
    # 2. Run The Detailer (Removes Floating Text)
    # This will pick up files from 'temp_stage1' automatically
    run_script("rm_text.py")

    elapsed = time.time() - total_start
    print("\n" + "#"*50)
    print(f"🎉 PIPELINE COMPLETE in {elapsed:.2f} seconds.")
    print("#"*50)

if __name__ == "__main__":
    main()