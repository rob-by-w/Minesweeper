import settings


def height_prct(percentage):
    return int(settings.HEIGHT * (percentage / 100))


def width_prct(percentage):
    return int(settings.WIDTH * (percentage / 100))
