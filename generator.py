import os
from dotenv import load_dotenv

load_dotenv()

MODEL_TYPE = os.getenv("MODEL_TYPE", "modelscope")  # "modelscope", "videodiffusion", "videocrafter"
MODEL_ID = os.getenv("MODEL_ID", "damo-vilab/modelscope-text-to-video-synthesis")

def generate_video_from_prompt(prompt, fps=8, resolution="512x512", duration=4, style=None, seed=None, **kwargs):
    # Import locally to avoid loading on worker startup
        if MODEL_TYPE == "modelscope":
                from modelscope.pipelines import pipeline
                        from modelscope.utils.constant import Tasks

                                pipe = pipeline(Tasks.text_to_video_synthesis, MODEL_ID)
                                        # ModelScope uses frames, not seconds
                                                total_frames = fps * duration
                                                        result = pipe({
                                                                    "text": prompt,
                                                                                "fps": fps,
                                                                                            "frames": total_frames,
                                                                                                        "resolution": resolution,
                                                                                                                    "seed": seed,
                                                                                                                                "style": style
                                                                                                                                        })
                                                                                                                                                # result["video"] expected to be np.ndarray [T, H, W, C]
                                                                                                                                                        return result["video"]

                                                                                                                                                            elif MODEL_TYPE == "videocrafter":
                                                                                                                                                                    from diffusers import VideoCrafterPipeline
                                                                                                                                                                            import torch

                                                                                                                                                                                    pipe = VideoCrafterPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float16).to("cuda")
                                                                                                                                                                                            video = pipe(prompt, num_frames=fps*duration, height=int(resolution.split("x")[0]), width=int(resolution.split("x")[1]), seed=seed).videos
                                                                                                                                                                                                    return video

                                                                                                                                                                                                        elif MODEL_TYPE == "videodiffusion":
                                                                                                                                                                                                                from diffusers import StableVideoDiffusionPipeline
                                                                                                                                                                                                                        import torch

                                                                                                                                                                                                                                pipe = StableVideoDiffusionPipeline.from_pretrained(MODEL_ID, torch_dtype=torch.float16).to("cuda")
                                                                                                                                                                                                                                        video = pipe(prompt, num_frames=fps*duration, height=int(resolution.split("x")[0]), width=int(resolution.split("x")[1]), seed=seed).videos
                                                                                                                                                                                                                                                return video

                                                                                                                                                                                                                                                    else:
                                                                                                                                                                                                                                                            raise ValueError("Unsupported MODEL_TYPE: choose 'modelscope', 'videocrafter', or 'videodiffusion'")