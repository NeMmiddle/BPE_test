def find_fake_basket(n, w, d, p) -> int:
    sum_ = (n - 1) * n / 2
    total = sum_ * w
    number_basket = int(abs(p - total) / d)

    return number_basket


print(find_fake_basket(36, 30, 19, 19000))


def test_passing():
    assert find_fake_basket(36, 30, 19, 19000) == 5
    assert find_fake_basket(100, 50, 42, 251323) == 91
    assert find_fake_basket(10, 30, 20, 1423) == 3
