import settings


def height_prct(percentage : int) -> int:
    return (settings.HEIGHT / 100) * percentage

def width_prct(percentage : int) -> int:
    return (settings.WIDTH / 100) * percentage
