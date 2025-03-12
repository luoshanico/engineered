import colorsys

def fade_color(rgb, fade_factor=0.5):
    r, g, b = [x / 255.0 for x in rgb]
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    s *= fade_factor
    r_new, g_new, b_new = colorsys.hls_to_rgb(h, l, s)
    return (int(r_new * 255), int(g_new * 255), int(b_new * 255))
