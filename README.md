# Kling-like AI Video Generator (Backend)

A production-ready, GPU-enabled FastAPI backend for AI video generation using SOTA models (ModelScope, VideoCrafter, Stable Video Diffusion), built with Celery, Redis, and Docker.

## Features

- **Async video generation endpoint** (`POST /api/generate-video`) with task queue
- **Status check endpoint** (`GET /api/status/{task_id}`)
- **Supports ModelScope, VideoCrafter, Stable Video Diffusion**
- **Outputs MP4 videos, ready for web/mobile**
- **GPU-ready, Dockerized, and scalable**
- Modular for future upgrades: AnimateDiff, Real-ESRGAN, Bark/ElevenLabs, watermarking, etc.

## Usage

### 1. Clone & Configure

```bash
git clone <this-repo>
cd backend
cp .env.example .env
# Edit .env as needed (choose model, GPU config, etc.)
```

### 2. Build and Launch (with GPU)

```bash
docker-compose up --build
```

### 3. API Endpoints

- **POST /api/generate-video**

  ```json
    {
        "prompt": "A cat dancing in space",
            "fps": 8,
                "resolution": "512x512",
                    "duration": 4,
                        "style": "anime",
                            "seed": 42
                              }
                                ```

                                  Returns: `{ "status": "processing", "task_id": "<id>" }`

                                  - **GET /api/status/{task_id}**

                                    Returns: `{ "status": "completed", "video_url": "/outputs/<id>.mp4" }`

                                    ### 4. Swagger UI

                                    Visit [http://localhost:8000/docs](http://localhost:8000/docs) for API documentation.

                                    ---

                                    ## For Future Upgrades

                                    - Add AnimateDiff, Real-ESRGAN, Bark, watermarking by extending `app/models/generator.py` and `utils/video_io.py`.

                                    ---

                                    ## License

                                    MIT