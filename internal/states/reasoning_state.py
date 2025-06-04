



class ToolValidationError(Exception):
    """Raised when tool parameters are invalid."""

    pass


class DependencyError(Exception):
    """Raised when there are issues with step dependencies."""

    pass
