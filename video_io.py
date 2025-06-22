import os
import uuid
import numpy as np
import imageio
import subprocess

def save_video(video_tensor, params):
    # video_tensor: numpy array [T, H, W, C]
        video_id = str(uuid.uuid4())
            out_dir = "outputs"
                os.makedirs(out_dir, exist_ok=True)
                    raw_path = os.path.join(out_dir, f"{video_id}.gif")
                        imageio.mimsave(raw_path, (video_tensor * 255).astype(np.uint8), format="GIF", fps=params.get("fps", 8))
                            return raw_path

                            def convert_to_mp4(input_path):
                                mp4_path = input_path.replace(".gif", ".mp4")
                                    cmd = [
                                            "ffmpeg",
                                                    "-y",
                                                            "-i", input_path,
                                                                    "-movflags", "faststart",
                                                                            "-pix_fmt", "yuv420p",
                                                                                    "-vf", "scale=trunc(iw/2)*2:trunc(ih/2)*2",
                                                                                            mp4_path
                                                                                                ]
                                                                                                    subprocess.run(cmd, check=True)
                                                                                                        return "/" + mp4_path  # for static file serving

                                                                                                        def fetch_video_url(task_id):
                                                                                                            for ext in [".mp4", ".gif"]:
                                                                                                                    possible = os.path.join("outputs", f"{task_id}{ext}")
                                                                                                                            if os.path.exists(possible):
                                                                                                                                        return "/" + possible
                                                                                                                                            return None