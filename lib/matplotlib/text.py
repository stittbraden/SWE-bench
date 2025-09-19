"""
Text handling and properties for matplotlib.
"""


class Text:
    """
    Handle storing and drawing of text in window or data coordinates.
    """
    
    def __init__(self, **kwargs):
        # Valid text properties that can be set
        self.valid_properties = {
            'alpha', 'animated', 'backgroundcolor', 'bbox', 'clip_box', 'clip_on',
            'clip_path', 'color', 'family', 'fontfamily', 'fontname', 'fontproperties',
            'fontsize', 'fontstretch', 'fontstyle', 'fontvariant', 'fontweight',
            'gid', 'ha', 'horizontalalignment', 'in_layout', 'label', 'linespacing',
            'ma', 'multialignment', 'path_effects', 'picker', 'position', 'rasterized',
            'rotation', 'rotation_mode', 'size', 'snap', 'stretch', 'style',
            'transform', 'url', 'usetex', 'va', 'variant', 'verticalalignment',
            'visible', 'weight', 'wrap', 'x', 'y', 'zorder'
        }
        
        # Set properties from kwargs
        for key, value in kwargs.items():
            if key in self.valid_properties:
                setattr(self, key, value)
            else:
                raise ValueError(f"Invalid Text property: {key}")