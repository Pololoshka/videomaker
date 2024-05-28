from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from .constants import Constant


def create_video(video_name: str, text: str, const: Constant, dir_name: str) -> Path:
    filename = f"{dir_name}/{video_name}.mp4"
    font_size = const.calculate_font_size(len_text=len(text))

    out_scr = cv2.VideoWriter(
        filename=filename,
        fourcc=cv2.VideoWriter_fourcc(*"mp4v"),  # type: ignore  # noqa: PGH003
        fps=const.fps,
        frameSize=(const.width, const.height),
    )

    frame = np.zeros((const.width, const.height, 3), dtype=np.uint8)
    x, y = const.width / 10, const.height // (font_size // 5)

    pillow_font = ImageFont.truetype(font=const.font_path, size=font_size)

    step = const.calculate_step(text_size=pillow_font.getbbox(text=text)[2])
    for _ in range(const.video_duration * int(const.fps)):
        frame.fill(0)
        x -= step

        frame[:] = const.background_color

        img = Image.fromarray(frame)
        draw = ImageDraw.Draw(img)

        draw.text(xy=(x, y), text=text, font=pillow_font, fill=const.text_color)

        frame = np.array(img)
        out_scr.write(frame)

    out_scr.release()
    return Path(filename)
