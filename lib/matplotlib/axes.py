"""
The Axes class, which encapsulates the plotting area and its components.
"""

from .axis import XAxis, YAxis, _validate_text_kwargs


class Axes:
    """
    The Axes contains most of the figure elements: Axis, Tick, Line2D, Text,
    Polygon, etc., and sets the coordinate system.
    """
    
    def __init__(self):
        self.xaxis = XAxis()
        self.yaxis = YAxis()
    
    def set_xticks(self, ticks, labels=None, *, minor=False, **kwargs):
        """
        Set the xaxis' tick locations and optionally tick labels.

        If necessary, the view limits of the Axis are expanded so that all
        given ticks are visible.

        Parameters
        ----------
        ticks : array-like
            List of tick locations.  The axis `~.Axis.Locator` is replaced by
            `~.ticker.FixedLocator`.

            Some tick formatters will not label arbitrary tick positions;
            e.g. log formatters only label decade ticks by default. In
            such a case you can set a formatter explicitly on the axis
            using `~.Axis.set_major_formatter` or provide formatted
            *labels* yourself.
        labels : array-like, optional
            List of tick labels. If not None, the `~.Axis.Formatter` is
            replaced by `~.ticker.FixedFormatter`.
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
        
        # Delegate to the xaxis
        self.xaxis.set_ticks(ticks, labels=labels, minor=minor, **kwargs)
    
    def set_yticks(self, ticks, labels=None, *, minor=False, **kwargs):
        """
        Set the yaxis' tick locations and optionally tick labels.

        If necessary, the view limits of the Axis are expanded so that all
        given ticks are visible.

        Parameters
        ----------
        ticks : array-like
            List of tick locations.  The axis `~.Axis.Locator` is replaced by
            `~.ticker.FixedLocator`.

            Some tick formatters will not label arbitrary tick positions;
            e.g. log formatters only label decade ticks by default. In
            such a case you can set a formatter explicitly on the axis
            using `~.Axis.set_major_formatter` or provide formatted
            *labels* yourself.
        labels : array-like, optional
            List of tick labels. If not None, the `~.Axis.Formatter` is
            replaced by `~.ticker.FixedFormatter`.
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
        
        # Delegate to the yaxis
        self.yaxis.set_ticks(ticks, labels=labels, minor=minor, **kwargs)
    
    def tick_params(self, **kwargs):
        """
        Change the appearance of ticks, tick labels, and gridlines.
        
        This method should be used instead of kwargs when setting tick
        properties without providing labels.
        """
        # Implementation would modify tick appearance
        pass