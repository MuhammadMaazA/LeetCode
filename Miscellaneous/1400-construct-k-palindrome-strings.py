class Solution:
    def canBeValid(s: str, locked: str) -> bool:
    """
    Determines if a parentheses string 's' can be valid by flipping
    characters at 'unlocked' positions (where locked[i] == '0').

    :param s: The parentheses string (consisting of '(' and ')')
    :param locked: A string of the same length as 's' where:
                   '1' indicates the character in 's' is locked (cannot be flipped),
                   '0' indicates the character in 's' is unlocked (can be flipped).
    :return: True if 's' can potentially be rearranged (by flipping
             unlocked parentheses) to form a valid parentheses sequence,
             otherwise False.
    """

    # Stacks to track indices of locked '(' and unlocked characters
    # which could potentially become '(' or ')'.
    stack_locked = []    # Will store indices of '(' that are locked
    stack_unlocked = []  # Will store indices of characters that are unlocked ('0')

    # First pass: Match closing parentheses (')') if possible
    for i in range(len(s)):
        if locked[i] == "0":
            # This character is unlocked; we can decide later if it's '(' or ')'
            # For now, treat it like an open parenthesis '('
            stack_unlocked.append(i)
        elif s[i] == "(":
            # Locked open parenthesis '(' - we must store its index
            stack_locked.append(i)
        else:
            # s[i] is ')'
            # We try to match this ')' with the most recent '(' if possible
            if stack_locked:
                # Prefer to match with a locked '(' if one is available
                stack_locked.pop()
            elif stack_unlocked:
                # Otherwise match with an unlocked '('
                stack_unlocked.pop()
            else:
                # No open parenthesis (locked or unlocked) left to match
                return False

    # At this point, stack_locked contains unmatched locked '('
    # stack_unlocked contains unmatched *unlocked* '('
    #
    # We can potentially flip some unlocked '(' into ')' to match locked '('.
    # We'll pair them off in a second pass if the unlocked index is greater
    # (meaning an unlocked '(' can come after a locked '(' and thus form "()").

    # While both stacks have unmatched '(',
    # try to match locked '(' with unlocked '(' that can be flipped to ')'
    while stack_locked and stack_unlocked and stack_locked[-1] < stack_unlocked[-1]:
        stack_locked.pop()
        stack_unlocked.pop()

    # If there are still locked '(' left that couldn't be matched, fail
    if stack_locked:
        return False

    # Finally, any remaining unmatched unlocked parentheses
    # must be an even number so they can flip/arrange to form valid pairs
    return True if len(stack_unlocked) % 2 == 0 else False
