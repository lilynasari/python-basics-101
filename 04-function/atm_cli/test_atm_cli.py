from atm_cli import get_input_deposit_money
from atm_cli import get_input_withdraw_money
from atm_cli import process_deposit
from atm_cli import process_withdrawal
from unittest.mock import patch
from atm_cli import init



#对于存钱输入校验函数进行常见异常检测
def test_get_input_deposit_money():
    with patch('builtins.input',side_effect=[' ','-100','50','200']):
        result = get_input_deposit_money()
        assert result == 200.0
        print("pass")

#对于取钱输入校验函数进行常见异常检测
def test_get_input_withdraw_money():
    init(b=1000)
    with patch('builtins.input',side_effect=[' ','-100','100001','2000','90']):
        result = get_input_withdraw_money()
        assert result == 90.0
        print("pass")

test_get_input_deposit_money()
test_get_input_withdraw_money()