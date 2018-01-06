from optparse import OptionParser

# 문자
OPEN_PARENTHESES = '('
CLOSE_PARENTHESES = ')'
PLUS = '+'
MINUS = '-'
MULTIPLY = '*'
DIVIDE = '/'

OPERATOR_RANKS = {
    MULTIPLY: 4,
    DIVIDE: 4,
    PLUS: 2,
    MINUS: 2,
    OPEN_PARENTHESES: 1,
    CLOSE_PARENTHESES: -1
}

CALCULATOR = {
    MULTIPLY: lambda l, r: l * r,
    DIVIDE: lambda l, r: l / r,
    PLUS: lambda l, r: l + r,
    MINUS: lambda l, r: l - r,
}


def is_stored_high_or_equal(stored_op, current_op):
    stored_rank = OPERATOR_RANKS.get(stored_op, -1)
    current_rank = OPERATOR_RANKS.get(current_op, -1)
    return stored_rank > current_rank or stored_rank == current_rank


def to_postfix(expression):
    postfix_expression = []
    stored_operators = []
    stored_digit = '' #두 자리 이상 숫자 쌓을려고

    for char in expression:
        if char.isdigit():
            stored_digit += char
        else:
            if char not in OPERATOR_RANKS.keys():
                continue

            if stored_digit:
                postfix_expression.append(int(stored_digit))
                stored_digit = ''

            if char == OPEN_PARENTHESES:
                stored_operators.append(char)

            elif char == CLOSE_PARENTHESES:
                while True:
                    stored_op = stored_operators.pop()
                    if stored_op == OPEN_PARENTHESES:
                        break
                    postfix_expression.append(stored_op)
                # reversed_stored_op = stored_operators[::-1]
                # slice_point = reversed_stored_op.index(OPEN_PARENTHESES)
                # postfix_expression.extend(reversed_stored_op[:slice_point])
                # sliced = reversed_stored_op[slice_point + 1:]
                # sliced.reverse()
                # stored_operators = sliced[:]

            else:
                while stored_operators and \
                        is_stored_high_or_equal(stored_operators[-1], char):
                    postfix_expression.append(stored_operators.pop())
                stored_operators.append(char)

    if stored_digit:
        postfix_expression.append(int(stored_digit))

    # 
    stored_operators.reverse()
    postfix_expression.extend(stored_operators)
    return postfix_expression


def eval_postfix(postfix_expression):
    store = []

    for char in postfix_expression:
        if isinstance(char, int):
            store.append(char)
        else:
            right_num = store.pop()
            left_num = store.pop()
            store.append(CALCULATOR[char](left_num, right_num))
    return store[0]


if __name__ == '__main__':
    parser = OptionParser()
    parser.add_option("-t", "--test",
                      action="store_true", dest="test", default=False,
                      help="testing this code")

    options, _ = parser.parse_args()

    if options.test:
        examples = (
            '11 - 7 - 1',
            '11 - 20-1',
            '11 - (20-1)',
            '1+20-1',
            '110+2*2',
            '((40+4)*5)/2',
            '(40+4) * (5 / 2)',
            '(10+20)*(3-1)'
        )
        for input_expression in examples:
            postfix = to_postfix(input_expression)
            result = eval_postfix(postfix)
            print('postfix expression: {}'.format(postfix))
            print('calculation result : {} = {}'.format(input_expression,
                                                        result))
    else:
        while True:
            input_expression = input("Enter the arithmetic expression: ")
            if not input_expression:
                break
            postfix = to_postfix(input_expression)
            result = eval_postfix(postfix)
            print('calculation result : {} = {}'.format(input_expression,
                                                        result))
```