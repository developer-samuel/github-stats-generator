def count_up_frames(value_str: str, num_frames: int = 12) -> list[str]:
    """Return list of formatted intermediate values for count-up animation."""
    clean = value_str.rstrip("+").replace(",", "")
    try:
        num = float(clean)
        is_float = "." in clean
    except ValueError:
        return [value_str]
    suffix = "+" if value_str.endswith("+") else ""
    frames = []
    for i in range(num_frames):
        v = num * i / (num_frames - 1)
        s = suffix if (v if is_float else int(v)) > 0 else ""
        if is_float:
            frames.append(f"{v:.1f}{s}")
        else:
            frames.append(f"{int(v):,}{s}")
    frames[-1] = value_str
    return frames


def count_up_svg(
    x: int,
    y: int,
    anchor: str,
    fill: str,
    font_size: int,
    font_weight: str,
    font_family: str,
    value_str: str,
    num_frames: int = 12,
    duration: float = 1.2,
    uid: str = "",
) -> str:
    """Generate stacked <text> elements that animate as a count-up."""
    frames = count_up_frames(value_str, num_frames)
    step = duration / num_frames
    out = ""
    for i, val in enumerate(frames):
        is_last = i == len(frames) - 1
        anim_name = f"cu_stay_{uid}" if is_last else f"cu_flash_{uid}"
        delay = f"{i * step:.3f}s"
        out += (
            f'<text font-family="{font_family}" x="{x}" y="{y}" text-anchor="{anchor}"'
            f' fill="{fill}" font-size="{font_size}" font-weight="{font_weight}"'
            f' opacity="0" style="animation:{anim_name} {step:.3f}s {delay} linear forwards">'
            f"{val}</text>"
        )
    return out


def count_up_css(uid: str) -> str:
    return (
        f"@keyframes cu_flash_{uid}{{0%,99%{{opacity:1}}100%{{opacity:0}}}}"
        f"@keyframes cu_stay_{uid}{{0%,100%{{opacity:1}}}}"
    )
