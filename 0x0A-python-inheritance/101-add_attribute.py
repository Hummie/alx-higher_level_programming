def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object.

    Args:
        obj: The object to which the attribute should be added.
        attr_name: The name of the new attribute.
        attr_value: The value to assign to the new attribute.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attr_name, attr_value)
