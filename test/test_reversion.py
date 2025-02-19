import unittest
from PyReversionEngine import ReversionEngine

reversion_engine = ReversionEngine()


def apply(word, rule):
    """Apply the rule to the given word"""
    reversion_engine.change_rules([rule])
    return list(reversion_engine.apply(word))[0][0]


class ReversionTest(unittest.TestCase):
    def test_toggle_case(self):
        self.assertEqual(apply('P@SSw0RD', 't'), 'p@ssW0rd')

    def test_toggle_n(self):
        self.assertEqual(apply('p@sSW0rd', 'T3'), 'p@ssW0rd')

    def test_reverse(self):
        self.assertEqual(apply('dr0Wss@p', 'r'), 'p@ssW0rd')

    def test_duplicate(self):
        self.assertEqual(apply('p@ssW0rdp@ssW0rd', 'd'), 'p@ssW0rd')

    def test_duplicate_n(self):
        self.assertEqual(apply('p@ssW0rdp@ssW0rdp@ssW0rd', 'p2'), 'p@ssW0rd')

    def test_reflect(self):
        self.assertEqual(apply('p@ssW0rddr0Wss@p', 'f'), 'p@ssW0rd')

    def test_rotate_left(self):
        self.assertEqual(apply('@ssW0rdp', '{'), 'p@ssW0rd')

    def test_rotate_right(self):
        self.assertEqual(apply('dp@ssW0r', '}'), 'p@ssW0rd')

    def test_append(self):
        self.assertEqual(apply('p@ssW0rd1', '$1'), 'p@ssW0rd')
        self.assertEqual(apply('p@ssW0rd1', '$2'), 'p@ssW0rd1')

    def test_prepend(self):
        self.assertEqual(apply('1p@ssW0rd', '^1'), 'p@ssW0rd')
        self.assertEqual(apply('1p@ssW0rd', '^2'), '1p@ssW0rd')

    # def test_truncate_left(self):
    #     self.assertEqual(apply('p@ssW0rd', '['), '@ssW0rd')

    # def test_truncate_right(self):
    #     self.assertEqual(apply('p@ssW0rd', ']'), 'p@ssW0r')

    def test_delete_n(self):
        self.assertEqual(apply('p@ssW0rd', 'D3'), 'p@ssW0rd')

    # def test_extract_range(self):
    #     self.assertEqual(apply('p@ssW0rd', 'x04'), 'p@ss')

    # def test_omit_range(self):
    #     self.assertEqual(apply('p@ssW0rd', 'O12'), 'psW0rd')

    def test_insert(self):
        self.assertEqual(apply('p@ss!W0rd', 'i4!'), 'p@ssW0rd')
        self.assertEqual(apply('p@ss!W0rd', 'i41'), 'p@ss!W0rd')

    # def test_overwrite(self):
    #     self.assertEqual(apply('p@ssW0rd', 'o3$'), 'p@s$W0rd')

    # def test_truncate_n(self):
    #     self.assertEqual(apply('p@ssW0rd', "'6"), 'p@ssW0')

    # def test_replace(self):
    #     self.assertEqual(apply('p@ssW0rd', 'ss$'), 'p@$$W0rd')

    # def test_purge(self):
    #     self.assertEqual(apply('p@ssW0rd', '@s'), 'p@W0rd')

    def test_duplicate_first_n(self):
        self.assertEqual(apply('ppp@ssW0rd', 'z2'), 'p@ssW0rd')

    def test_duplicate_last_n(self):
        self.assertEqual(apply('p@ssW0rddd', 'Z2'), 'p@ssW0rd')

    def test_duplicate_all(self):
        self.assertEqual(apply('pp@@ssssWW00rrdd', 'q'), 'p@ssW0rd')

    # def test_extract_memory(self):
    #     self.assertEqual(apply('p@ssW0rd', 'lMX428'), 'p@ssw0rdw0')
    #
    # def test_append_memory(self):
    #     self.assertEqual(apply('p@ssW0rd', 'uMl4'), 'p@ssw0rdP@SSW0RD')
    #
    # def test_prepend_memory(self):
    #     self.assertEqual(apply('p@ssW0rd', 'rMr6'), 'dr0Wss@pp@ssW0rd')
    #
    # def test_memorize(self):
    #     self.assertEqual(apply('p@ssW0rd', 'lMuX084'), 'P@SSp@ssw0rdW0RD')

    # def test_swap_front(self):
    #     self.assertEqual(apply('p@ssW0rd', 'k'), '@pssW0rd')
    #
    # def test_swap_back(self):
    #     self.assertEqual(apply('p@ssW0rd', 'K'), 'p@ssW0dr')
    #
    # def test_swap_n(self):
    #     self.assertEqual(apply('p@ssW0rd', '*34'), 'p@sWs0rd')
    #
    # def test_bitwise_left(self):
    #     self.assertEqual(apply('p@ssW0rd', 'L2'), 'p@æsW0rd')
    #
    # def test_bitwise_right(self):
    #     self.assertEqual(apply('p@ssW0rd', 'R2'), 'p@9sW0rd')
    #
    # def test_ascii_increment(self):
    #     self.assertEqual(apply('p@ssW0rd', '+2'), 'p@tsW0rd')
    #
    # def test_bitwise_decrement(self):
    #     self.assertEqual(apply('p@ssW0rd', '-1'), 'p?ssW0rd')
    #
    # def test_replace_n_plus(self):
    #     self.assertEqual(apply('p@ssW0rd', '.1'), 'psssW0rd')
    #
    # def test_replace_n_minus(self):
    #     self.assertEqual(apply('p@ssW0rd', ',1'), 'ppssW0rd')
    #
    # def test_duplicate_front(self):
    #     self.assertEqual(apply('p@ssW0rd', 'y2'), 'p@p@ssW0rd')
    #
    # def test_duplicate_back(self):
    #     self.assertEqual(apply('p@ssW0rd', 'Y2'), 'p@ssW0rdrd')
    #
    # def test_title(self):
    #     self.assertEqual(apply('p@ssW0rd w0rld', 'E'), 'P@ssw0rd W0rld')
    #
    # def test_title_space(self):
    #     self.assertEqual(apply('p@ssW0rd-w0rld', 'e-'), 'P@ssw0rd-W0rld')
    #
    # def test_title_nth(self):
    #     self.assertEqual(apply('pass-word', '30-'), 'pass-Word')

    # def test(self):
    #     self.assertEqual(apply('mycomputer', 'O02'), 'computer')
    #     self.assertEqual(apply('mycomputer', 'O02$1'), 'computer1')
    #     self.assertEqual(apply('Q12q34Q56', 'lD6'), 'q12q3456')
    #     self.assertEqual(apply('789632145', 'D0}'), '58963214')
    #     self.assertEqual(apply('xiaoweiwei', 'swfO94'), 'xiaofeifei')
    #     self.assertEqual(apply('434118', 'o33o7@'), '434318')
    #     self.assertEqual(apply('4210021837', 'O46z2'), '444210')
    #     self.assertEqual(apply('123123wo', 'i8iD6'), '123123oi')


if __name__ == '__main__':
    unittest.main()
