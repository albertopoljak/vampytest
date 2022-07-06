from .. import assert_subtype

from vampytest import revert, raising


def test_assert_subtype():
    """
    Tests whether `subtype` assertion succeeds.
    """
    assert_subtype(bool, int)


@revert()
def test_assert_subtype_reverted():
    """
    Tests whether `subtype` assertion fails.
    """
    assert_subtype(bool, str)


@raising(TypeError)
def test_assert_subtype_incorrect_type():
    """
    Tests whether `subtype` assertion raises when type parameter is incorrect.
    """
    assert_subtype(bool, 1)


@revert()
def test_assert_subtype_incorrect_checked():
    """
    Tests whether `subtype` assertion fails when the checked value's type is incorrect.
    """
    assert_subtype(1, int)
