from pathlib import Path


class Constant:
    width = 100
    height = 100
    fps = 300.0
    background_color = (209, 213, 69)
    text_color = (188, 69, 213)
    video_duration = 3
    font_path = Path(__file__).parent / "Symbola.ttf"

    def calculate_step(self, text_size: int) -> float:
        return (text_size - self.width // 4) / (int(self.fps) * 3)

    @staticmethod
    def calculate_font_size(len_text: int) -> int:
        return 75 - (len_text - 1) // 10 * 10
