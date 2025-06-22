from fastapi import APIRouter, HTTPException, BackgroundTasks
from pydantic import BaseModel
from typing import Optional
import os

from app.workers.tasks import generate_video_task, get_task_status

router = APIRouter()

class VideoRequest(BaseModel):
    prompt: str
        fps: Optional[int] = 8
            resolution: str = "512x512"
                duration: int = 4
                    style: Optional[str] = None
                        seed: Optional[int] = None

                        class StatusResponse(BaseModel):
                            status: str
                                video_url: Optional[str] = None
                                    error: Optional[str] = None

                                    @router.post("/generate-video")
                                    def generate_video(req: VideoRequest):
                                        task = generate_video_task.delay(req.dict())
                                            return {"status": "processing", "task_id": task.id}

                                            @router.get("/status/{task_id}", response_model=StatusResponse)
                                            def get_status(task_id: str):
                                                status, url, error = get_task_status(task_id)
                                                    return StatusResponse(status=status, video_url=url, error=error)
