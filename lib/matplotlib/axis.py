"""
The Axis class, which encapsulates axis and tick objects.
"""

import matplotlib.text as mtext


def _validate_text_kwargs(kwargs):
    """
    Validate that kwargs are valid Text properties.
    
    This function checks if the provided kwargs are valid properties
    that can be applied to Text objects.
    """
    valid_text_properties = {
        'alpha', 'animated', 'backgroundcolor', 'bbox', 'clip_box', 'clip_on',
        'clip_path', 'color', 'family', 'fontfamily', 'fontname', 'fontproperties',
        'fontsize', 'fontstretch', 'fontstyle', 'fontvariant', 'fontweight',
        'gid', 'ha', 'horizontalalignment', 'in_layout', 'label', 'linespacing',
        'ma', 'multialignment', 'path_effects', 'picker', 'position', 'rasterized',
        'rotation', 'rotation_mode', 'size', 'snap', 'stretch', 'style',
        'transform', 'url', 'usetex', 'va', 'variant', 'verticalalignment',
        'visible', 'weight', 'wrap', 'x', 'y', 'zorder'
    }
    
    invalid_kwargs = set(kwargs.keys()) - valid_text_properties
    if invalid_kwargs:
        raise ValueError(f"Invalid Text properties: {invalid_kwargs}")


class Axis:
    """
    Base class for XAxis and YAxis.
    """
    
    def __init__(self):
        self.majorTicks = []
        self.minorTicks = []
    
    def set_ticks(self, ticks, labels=None, *, minor=False, **kwargs):
        """
        Set the locations of the ticks.

        Parameters
        ----------
        ticks : array-like
            List of tick locations.
        labels : array-like, optional
            List of tick labels. If not None, the labels will be updated
            at the same time as the ticks.
        minor : bool, default: False
            If False, set the major ticks; if True, set the minor ticks.
        **kwargs
            `.Text` properties for the labels. These take effect only if you
            pass *labels*. In other cases, please use `~.Axes.tick_params`.

        Notes
        -----
        The mandatory expansion of the view limits is an intentional design
        choice to prevent the surprise of a non-visible tick. If you need
        other limits, you should set the limits explicitly after setting the
        ticks.
        """
        # Validate kwargs are valid Text properties regardless of whether labels are set
        if kwargs:
            _validate_text_kwargs(kwargs)
        
        # Set the tick locations
        if minor:
            self.set_minor_locator(ticks)
        else:
            self.set_major_locator(ticks)
        
        # Set the labels if provided (kwargs only take effect if labels are provided)
        if labels is not None:
            if minor:
                self.set_minor_formatter(labels, **kwargs)
            else:
                self.set_major_formatter(labels, **kwargs)
    
    def set_major_locator(self, ticks):
        """Set the major tick locations."""
        # Implementation would set the actual tick locations
        pass
    
    def set_minor_locator(self, ticks):
        """Set the minor tick locations.""" 
        # Implementation would set the actual tick locations
        pass
    
    def set_major_formatter(self, labels, **kwargs):
        """Set the major tick labels."""
        # Implementation would set the actual tick labels
        pass
    
    def set_minor_formatter(self, labels, **kwargs):
        """Set the minor tick labels."""
        # Implementation would set the actual tick labels
        pass


class XAxis(Axis):
    """The X axis."""
    pass


class YAxis(Axis):
    """The Y axis."""
    pass