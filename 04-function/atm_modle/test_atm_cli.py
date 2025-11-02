from atm_cli import validate_amount_deposit
from atm_cli import validate_amount_withdraw
from atm_cli import init
import pytest
@pytest.mark.parametrize("deposit_money_str,expected_deposit",
                         [(" ", "空串错误"),
                          ("cdv", "非数字错误"),
                          ("200.009", "精度过多错误"),
                          ("-100","负数/零错误"),
                          ("1000000000000000","金额超限错误"),
                          ("100","合法")])
def test_validate_deposit_money(deposit_money_str,expected_deposit):
    assert validate_amount_deposit(deposit_money_str)==expected_deposit
    print ("pass")
@pytest.mark.parametrize("withdraw_money_str,expected_withdraw",
                         [(" ","空串错误"),
                          ("abc","非数字错误"),
                          ("100.001","精度过多错误"),
                          ("-100","负数/零错误"),
                          ("100000000000000","金额超限错误"),
                          ("1001","余额不足"),
                          ("100","合法")])
def test_validate_withdraw_money(withdraw_money_str,expected_withdraw):
    init(b=1000)
    assert validate_amount_withdraw(withdraw_money_str)==expected_withdraw
    print ("pass")