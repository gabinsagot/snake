from snake import eat_snake

def test_eat_snake(queue):
    snake = [(10, 11), (11, 11)]
    count = 2
    eat_snake(snake, count)
    assert snake == [(10, 11), (11, 11), queue]
    assert count == 3

test_eat_snake((12, 11))