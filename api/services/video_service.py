from fastapi import UploadFile

async def process_video(file: UploadFile, target_lang: str) -> str:
    return "Video processing is not available in the demo version."
