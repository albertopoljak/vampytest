__all__ = ('AssertionValueEvaluationFalse', 'assert_false', 'assert_not')

from .assertion_conditional_base import AssertionConditionalBase1Value

from scarletio import copy_docs


class AssertionValueEvaluationFalse(AssertionConditionalBase1Value):
    """
    Asserts whether the value evaluates to `False`.
    
    Attributes
    ----------
    state : `str`
        The condition's state.
    exception : `None`, `BaseException`
        Exception raised by the condition if any.
    value_1 : `Any`
        First value to assert.
    """
    __slots__ = ()
    
    @copy_docs(AssertionConditionalBase1Value.invoke_condition)
    def invoke_condition(self):
        return not self.value_1


assert_false = AssertionValueEvaluationFalse
assert_not = AssertionValueEvaluationFalse
