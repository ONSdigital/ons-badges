from jinja2 import Template

SVG = """
<svg width="{{new_global_width}}" height="20px" xmlns="http://www.w3.org/2000/svg">
    <g id="ons-badge">
        <g id="middle">
            <rect id="background" x="{{new_background_x}}" y="0" width="13.572" height="20" style="fill:#fff;"/>
        </g>
        <g id="left">
            <path id="left-shape" d="{{new_left_shape}}" style="fill:#a8bd3a;"/>
            <g id="left-text-section">
                <text x="3.893px" y="14.039px" style="font-family: monospace; font-weight:400;font-size:11.315px;fill:#000000;">
                    {{left_text}}
                </text>
            </g>
        </g>
        <g id="right">
            <path id="right-shape" d="{{new_right_shape}}" fill="{{bg}}"/>
            <g id="right-text-section">
                <text x="{{new_right_text_x}}" y="14.039px" style="font-family: monospace; font-weight:400;font-size:11.315px;" fill="{{fg}}">
                    {{right_text}}
                </text>
            </g>
        </g>
    </g>
</svg>
"""


def calculate_text_width(text: str) -> float:
    """
    Calculate the width of a block of text in svg units
    """
    char_width = 7.5
    return len(text) * char_width


def calculate_background_x(left_shift: float) -> float:
    """
    Calculate the new x position of the background
    :param left_shift: float - the width of the left text
    :return: float - the new x position in svg units
    """
    return 4.744 + left_shift


def calculate_left_shape(left_shift: float) -> str:
    """
    Calculate the new shape of the left section
    :param left_shift: float - the width of the left text
    :return: str - the new shape in svg path format
    """
    new_top = 11.018 + left_shift
    new_bottom = 0.58 + left_shift
    new_start = 4.744 + left_shift
    return f"M{new_start},20l-{new_bottom},-0c-2.3,-0 -4.164,-1.864 -4.164,-4.164l0,-11.672c0,-2.3 1.864,-4.164 4.164,-4.164l{new_top},0l-10.438,20Z"


def calculate_right_shape(left_shift: float, right_shift: float) -> str:
    """
    Calculate the new shape of the right section
    :param left_shift: float - the width of the left text
    :param right_shift: float - the width of the right text
    :return: str - the new shape in svg path format
    """
    new_top = 0.58 + right_shift
    new_bottom = 11.018 + right_shift
    new_start = 18.315 + left_shift
    return f"M{new_start},0l{new_top},0c2.299,-0 4.164,1.864 4.164,4.164l-0,11.672c-0,2.3 -1.865,4.164 -4.164,4.164l-{new_bottom},-0l10.438,-20Z"


def calculate_right_text_x(left_shift: float) -> float:
    """
    Calculate the new x position of the right text
    :param left_shift: float - the width of the left text
    :return: float - the new x position in svg units
    """
    return 20.464 + left_shift


def calculate_global_width(left_shift: float, right_shift: float) -> float:
    """
    Calculate the new width of the svg
    :param left_shift: float - the width of the left text
    :param right_shift: float - the width of the right text
    :return: float - the new width in svg units
    """
    return 24 + left_shift + right_shift


def generate_svg(left_text: str, right_text: str, bg: str, fg: str) -> str:
    """
    Generate SVG with the given text and colour
    :param left_text: str - the text to display on the left
    :param right_text: str - the text to display on the right
    :param bg: str - the background colour of the right section
    :param fg: str - the text colour of the right section
    """

    left_shift = calculate_text_width(left_text)
    right_shift = calculate_text_width(right_text)

    new_background_x = calculate_background_x(left_shift)
    new_left_shape = calculate_left_shape(left_shift)
    new_right_shape = calculate_right_shape(left_shift, right_shift)
    new_right_text_x = calculate_right_text_x(left_shift)
    new_global_width = calculate_global_width(left_shift, right_shift)

    template = Template(SVG)
    return template.render(
        left_text=left_text,
        right_text=right_text,
        bg=bg,
        fg=fg,
        new_background_x=new_background_x,
        new_left_shape=new_left_shape,
        new_right_shape=new_right_shape,
        new_right_text_x=new_right_text_x,
        new_global_width=new_global_width
    )
