from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.routes import video

app = FastAPI(
    title="Kling-like AI Video Generator API",
        description="Generate videos from text prompts using SOTA models. Async, GPU-ready, Docker deployable.",
            version="1.0.0"
            )

            app.add_middleware(
                CORSMiddleware,
                    allow_origins=["*"],
                        allow_methods=["*"],
                            allow_headers=["*"],
                            )

                            # Static video file serving
                            app.mount("/outputs", StaticFiles(directory="outputs"), name="outputs")

                            # Register routers
                            app.include_router(video.router, prefix="/api")
