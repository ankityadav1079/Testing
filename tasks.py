import os
from celery import Celery
from celery.result import AsyncResult
from dotenv import load_dotenv

from app.models.generator import generate_video_from_prompt
from app.utils.video_io import save_video, convert_to_mp4

load_dotenv()

CELERY_BROKER_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
CELERY_BACKEND_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")

celery = Celery(
    "video_tasks",
        broker=CELERY_BROKER_URL,
            backend=CELERY_BACKEND_URL
            )

            @celery.task(bind=True)
            def generate_video_task(self, params):
                try:
                        video_tensor = generate_video_from_prompt(**params)
                                video_path = save_video(video_tensor, params)
                                        mp4_path = convert_to_mp4(video_path)
                                                return {"status": "completed", "video_url": mp4_path}
                                                    except Exception as e:
                                                            return {"status": "failed", "error": str(e)}

                                                            def get_task_status(task_id):
                                                                result = AsyncResult(task_id, app=celery)
                                                                    if result.state == "PENDING":
                                                                            return "pending", None, None
                                                                                elif result.state == "STARTED":
                                                                                        return "processing", None, None
                                                                                            elif result.state == "SUCCESS":
                                                                                                    data = result.result
                                                                                                            return data.get("status", "completed"), data.get("video_url"), data.get("error")
                                                                                                                elif result.state == "FAILURE":
                                                                                                                        return "failed", None, str(result.result)
                                                                                                                            else:
                                                                                                                                    return result.state.lower(), None, None