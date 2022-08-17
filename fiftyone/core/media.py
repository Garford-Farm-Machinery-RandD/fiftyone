"""
Sample media utilities.

| Copyright 2017-2022, Voxel51, Inc.
| `voxel51.com <https://voxel51.com/>`_
|
"""
import eta.core.video as etav


# Valid media types
VIDEO = "video"
IMAGE = "image"
POINT_CLOUD = "point-cloud"
GROUP = "group"
MEDIA_TYPES = {IMAGE, VIDEO, POINT_CLOUD, GROUP}

# Special media types
MIXED = "mixed"


def get_media_type(filepath):
    """Gets the media type for the given filepath.

    Args:
        filepath: a filepath

    Returns:
        the media type
    """
    if etav.is_video_mime_type(filepath):
        return VIDEO

    if filepath.endswith(".pcd"):
        return POINT_CLOUD

    return IMAGE


class MediaTypeError(TypeError):
    """Exception raised when a problem with media types is encountered."""

    pass


class SelectGroupSliceError(ValueError):
    """Exception raised when a grouped collection is passed to a method that
    expects a primitive media type to be selected.
    """

    def __init__(self, supported_media_types):
        if not isinstance(supported_media_types, str):
            supported_media_types = "/".join(supported_media_types)

        message = (
            "This method does not directly support grouped collections. "
            "You must use `select_group_slice()` to select %s slice(s) to "
            "process"
        ) % supported_media_types

        super().__init__(message)
